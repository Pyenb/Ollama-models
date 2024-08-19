#!/bin/bash

# Function to check command success
check_success() {
    if [ $? -ne 0 ]; then
        echo "$1"
        exit 1
    fi
}

# Function to display help message
show_help() {
    cat << EOF
Usage: ${0##*/} [OPTIONS]

Options:
  -m, --model-name    Name of the model to pull and backup (e.g. "moondream", "gemma2:2b", "llama3.1:70b").
  -d, --dest-folder   Path to the destination folder where the tar.gz file will be moved.
  -f, --model-folder  Path to the Ollama model folder (default: /usr/share/ollama/.ollama/models).
  -h, --help          Display this help message and exit.

If no options are provided, the script will display this help message.

Examples:
  ${0##*/} -m moondream -d /path/to/backup -f /custom/path/to/models
  ${0##*/} -m llama3.1 -d /home/pyenb/Daten/Backups/Ollama/models
EOF
}

# Default values
MODEL_NAME=""
OLLAMA_ROOT="/usr/share/ollama/.ollama"
MODEL_FOLDER="${OLLAMA_ROOT}/models"
DEST_FOLDER=""

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -m|--model-name)
            MODEL_NAME="$2"
            shift 2
            ;;
        -d|--dest-folder)
            DEST_FOLDER="$2"
            shift 2
            ;;
        -f|--model-folder)
            MODEL_FOLDER="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Validate required arguments
if [ -z "$MODEL_NAME" ] || [ -z "$DEST_FOLDER" ]; then
    echo "Error: Both model name and destination folder are required."
    show_help
    exit 1
fi

TAR_FILE_NAME="${MODEL_NAME}.tar.gz"

# Check if file already exists in the destination folder
if [ -e "${DEST_FOLDER}/${TAR_FILE_NAME}" ]; then
    echo "${TAR_FILE_NAME} already exists in the destination folder. Exiting..."
    exit 0
fi

# Pull the Ollama model
echo "Pulling the Ollama model: ${MODEL_NAME}..."
ollama pull "${MODEL_NAME}"
check_success "Failed to pull the model."

# Check if the model folder exists
if [ ! -d "$MODEL_FOLDER" ]; then
    echo "Model folder not found."
    exit 1
fi

if [ -e "${OLLAMA_ROOT}/${TAR_FILE_NAME}" ]; then
    echo "${TAR_FILE_NAME} already exists in the Ollama root folder. Skipping the compression step..."
else
    # Compress the model folder
    echo "Compressing the model folder..."
    cd "$MODEL_FOLDER/.." || exit 1

    # Create the tar.gz file
    tar -cf - "$(basename "$MODEL_FOLDER")" \
        | pv -s $(du -sb "$MODEL_FOLDER" | cut -f1) \
        | pigz > "${TAR_FILE_NAME}"
    check_success "Failed to compress the model folder."
fi

# Move the tar.gz file to the destination folder using rclone
echo "Moving the compressed file..."
rclone move "${OLLAMA_ROOT}/${TAR_FILE_NAME}" "${DEST_FOLDER}/" --progress
check_success "Failed to move the compressed file."

# Delete the original model folder contents
read -p "Press Enter to continue with deletion or Ctrl+C to cancel..."

echo "Deleting the original model folder contents..."
rm -rf "$MODEL_FOLDER/blobs" "$MODEL_FOLDER/manifests"
check_success "Failed to delete the model folder contents."

echo "Model moved and cleaned up successfully."

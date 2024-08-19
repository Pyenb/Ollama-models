# Ollama model repository

A few weeks ago I wanted to run [ollama](https://github.com/ollama/ollama/) on a machine, that was not connected to the internet. After a bit of searching, around, I found [this issue](https://github.com/ollama/ollama/issues/696), which basically said that the models are not just available as a download as a standalone file. So I decided to download the models myself, using a machine that had internet access, and make them available for everyone, in form of a compressed folder. This way, setting up your desired model will be as simple as moving a few files around.

## Table of contents 📚

- [Installation](#installation-)
- [Download links](#download-links-)
- [Manual export](#manual-export-)
- [FAQ](#faq-)

## Installation 🚀

1. Download the model you want to use from the [download links](#download-links-) section.
2. Extract the downloaded file `.tar.gz` file. Then extract the `.tar` file located inside the extracted folder.
3. Move the extracted folder `models` to the root of the `ollama` repository. See [where-are-models-stored](https://github.com/ollama/ollama/blob/main/docs/faq.md#where-are-models-stored), from the official `ollama` FAQ for more information.
4. You should now be able to use the model you downloaded. Executing `ollama run MODEL_NAME` should work as expected, without it trying to download the model.

## Download links 📥

<details>
<summary>Click to expand</summary>

<!-- MODEL_TABLE -->
| Model Name | Last Modified | Size | Download Link |
| --- | --- | --- | --- |
| codellama | 2024-08-18 16:48 | 3.4G | [Download](https://data.pyenb.network/Github/Ollama/models/codellama.tar.gz) |
| gemma2 | 2024-08-18 18:24 | 4.8G | [Download](https://data.pyenb.network/Github/Ollama/models/gemma2.tar.gz) |
| gemma2:2b | 2024-08-18 15:45 | 1.5G | [Download](https://data.pyenb.network/Github/Ollama/models/gemma2:2b.tar.gz) |
| llama2-uncensored | 2024-08-18 16:32 | 3.4G | [Download](https://data.pyenb.network/Github/Ollama/models/llama2-uncensored.tar.gz) |
| llama3.1:70b | 2024-08-18 19:51 | 35G | [Download](https://data.pyenb.network/Github/Ollama/models/llama3.1:70b.tar.gz) |
| llama3:8b | 2024-08-18 20:13 | 4.1G | [Download](https://data.pyenb.network/Github/Ollama/models/llama3:8b.tar.gz) |
| mistral | 2024-08-18 20:08 | 3.6G | [Download](https://data.pyenb.network/Github/Ollama/models/mistral.tar.gz) |
| moondream | 2024-08-18 16:29 | 1.4G | [Download](https://data.pyenb.network/Github/Ollama/models/moondream.tar.gz) |
| phi3 | 2024-08-18 16:20 | 1.9G | [Download](https://data.pyenb.network/Github/Ollama/models/phi3.tar.gz) |

</details>

Or you can of course just browse the [models folder](https://data.pyenb.network/Github/Ollama/models/) directly and download the model you want.

> [!NOTE]
> I am, as of now, still in the process of downloading and uploading the models, whenever I have time. So please have a bit of patience and see [I want a model that is not listed here, what can I do?](#i-want-a-model-that-is-not-listed-here-what-can-i-do) for more information.

## Manual export 📦

To export the model yourself, you can use the [ollama-exporter.sh](./ollama-exporter.sh) script, that I created. The script will create a `.tar.gz` file of the model you want to export.

> [!CAUTION]
> This script will delete everything in the `models` folder to make sure that only the model you want to export is present. Make sure to back up any models you want to keep! I did this on a separate VM.

```bash
Usage: ollama-exporter.sh [OPTIONS]

Options:
  -m, --model-name    Name of the model to pull and backup (e.g. "moondream", "gemma2:2b", "llama3.1:70b").
  -d, --dest-folder   Path to the destination folder where the tar.gz file will be moved.
  -f, --model-folder  Path to the ollama model folder (default: /usr/share/ollama/.ollama/models).
  -h, --help          Display this help message and exit.

If no options are provided, the script will display this help message.

Examples:
  ollama-exporter.sh -m moondream -d /path/to/backup -f /custom/path/to/models
  ollama-exporter.sh -m llama3.1 -d /home/pyenb/Daten/Backups/Ollama/models
```

###### This script is currently WIP and Linux only. Requires `ollama, rclone, pv and pigz` to be installed

As the model name, everything out of [Ollamas registry](https://registry.ollama.com/library) should work. Everything else should be self-explanatory.

The finished `.tar.gz` file structure will look like this:

```plaintext
MODEL_NAME.tar.gz
└── MODEL_NAME.tar
    └── models
        ├── blobs
        │   └── sha256-...
        └── manifests
            └── registry.ollama.ai
                └── library
                    └── MODEL_NAME
                        └── latest
```

<details>
<summary>Example output</summary>

```bash
pyenb@ollama:~$ sudo ./ollama-exporter.sh -m llama3.1:70b -d /home/pyenb/Daten/Backups/Ollama/models
Pulling the Ollama model: llama3.1:70b...
pulling manifest 
pulling a677b4a4b70c... 100% 39 GB                         
pulling 11ce4ee3e170... 100% 1.7 KB                         
pulling 0ba8f0e314b4... 100% 12 KB                         
pulling 56bb8bd477a5... 100% 96 B                         
pulling 654440dac7f3... 100% 486 B                         
verifying sha256 digest 
writing manifest 
removing any unused layers 
success 
Compressing the model folder...
37.2GiB 0:02:41 [ 235MiB/s] [==========================================================================] 100%            
Moving the tar.gz file to the destination folder using rclone...
2024/08/18 19:51:15 NOTICE: Config file "/root/.config/rclone/rclone.conf" not found - using defaults
Transferred:       35.464 GiB / 35.464 GiB, 100%, 1.243 MiB/s, ETA 0s
Checks:                 2 / 2, 100%
Deleted:                1 (files), 0 (dirs)
Renamed:                1
Transferred:            1 / 1, 100%
Elapsed time:      7m36.3s
Press Enter to continue with deletion or Ctrl+C to cancel...
Deleting the original model folder contents...
Model moved and cleaned up successfully.
```

</details>

## FAQ ❓

### Why not upload them using Github LFS?

With GitHub LFS, a "data pack" costs approximately €5 per month for 50GB of storage. The Storage-VPS I'm using also costs around 5€ per month, but with 800GB of SSD storage. So I decided to host the files myself. The only downside is mostly the download speed, so consider [supporting me](https://github.com/sponsors/Pyenb), so that I can upgrade the server.

### I want a model that is not listed here, what can I do?

You can either create the model yourself by following the [manual export](#manual-export) instructions, or you can open an issue, and I will try to get it done as soon as possible.

## Resources 🔗

- [where-are-models-stored](https://github.com/ollama/ollama/blob/main/docs/faq.md#where-are-models-stored)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Disclaimer

This repository is for research purposes only, the use of this code is your responsibility.

I take NO responsibility and/or liability for how you choose to use any of the source code available here. By using any of the files available in this repository, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again, ALL files available here are for EDUCATION and/or RESEARCH purposes ONLY.

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

URL = "https://data.pyenb.network/Github/Ollama/models/"
TORRENT_URL = URL + "torrents/"

try:
    response = requests.get(URL)
except:
    print("Failed to fetch the page. Exiting...")
    exit(1)

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')[2:]

markdown_table = "| Model | Parameters | Last Modified | Size | Download Link |\n| --- | --- | --- | --- | --- |\n"

# Add tqdm for the progress bar, setting total number of rows to process
for row in tqdm(rows, desc="Processing rows"):
    columns = row.find_all('td')
    if len(columns) < 4:
        continue

    file_name = columns[1].find('a').get_text().strip()

    # Skip 'Parent Directory' and non-torrent files
    if file_name == "Parent Directory" or not file_name.endswith(".tar.gz.torrent"):
        continue

    last_modified = columns[2].get_text().strip()
    size = columns[3].get_text().strip()

    # Remove '.tar.gz.torrent' to extract model and parameters
    file_name_base = file_name.replace('.tar.gz.torrent', '')

    # Check for ':' to split model and parameters
    if ':' in file_name_base:
        model, parameters = file_name_base.split(':', 1)
    else:
        model = file_name_base
        parameters = '---'

    torrent_url = TORRENT_URL + file_name
    
    # Add the row to the markdown table
    markdown_table += f"| {model} | {parameters.upper()} | {last_modified} | {size} | [Torrent]({torrent_url}) |\n"

# Read and update the README file
with open("README.md", "r", encoding="utf8") as file:
    readme = file.read()

readme_parts = readme.split("<!-- MODEL_TABLE_START -->")
before_table = readme_parts[0]
after_table = readme_parts[1].split("<!-- MODEL_TABLE_END -->")[1]

# Update the README content
new_readme = f"{before_table}<!-- MODEL_TABLE_START -->\n{markdown_table}<!-- MODEL_TABLE_END -->{after_table}"

# Write the updated README file
with open("README.md", "w+", encoding="utf8") as file:
    file.write(new_readme)

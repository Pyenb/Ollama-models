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

markdown_table = "| Model | Parameters | Last Modified | Size | Download Links |\n| --- | --- | --- | --- | --- |\n"

# Add tqdm for the progress bar, setting total number of rows to process
for row in tqdm(rows, desc="Processing rows"):
    columns = row.find_all('td')
    if len(columns) < 4:
        continue
    
    file_name = columns[1].find('a').get_text().strip()
    
    # Correcting the logic to skip 'Parent Directory' and 'torrents' directory
    if file_name == "Parent Directory" or 'torrents' in file_name:
        continue
    
    last_modified = columns[2].get_text().strip()
    if '1970' in last_modified:
        continue
    
    size = columns[3].get_text().strip()
    
    file_url = URL + file_name
    file_name = file_name.replace('.tar.gz', '')
    
    # Check for ':' to split model and parameters
    if ':' in file_name:
        model, parameters = file_name.split(':', 1)
    else:
        model = file_name
        parameters = '---'
    
    # Check if the corresponding torrent file exists
    torrent_file = f"{file_name}.tar.gz.torrent"
    torrent_url = TORRENT_URL + torrent_file
    
    # Send a request to check if the torrent file exists
    torrent_exists = requests.head(torrent_url).status_code == 200
    
    torrent_link = f"[Torrent]({torrent_url})" if torrent_exists else '---'
    
    # Add the row to the markdown table
    markdown_table += f"| {model} | {parameters.upper()} | {last_modified} | {size} | [Storage VPS]({file_url}) / {torrent_link} |\n"

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

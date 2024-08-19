import requests
from bs4 import BeautifulSoup

URL = "https://data.pyenb.network/Github/Ollama/models/"

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
for row in rows:
    columns = row.find_all('td')
    if len(columns) < 4:
        continue
    
    file_name = columns[1].find('a').get_text().strip()
    if file_name == "Parent Directory":
        continue
    
    last_modified = columns[2].get_text().strip()
    if '1970' in last_modified:
        continue
    
    size = columns[3].get_text().strip()
    
    file_url = URL + file_name
    file_name = file_name.replace('.tar.gz', '')
    
    if ':' in file_name:
        model, parameters = file_name.split(':', 1)
    else:
        model = file_name
        parameters = '---'
    
    markdown_table += f"| {model} | {parameters.upper()} | {last_modified} | {size} | [Download]({file_url}) |\n"

with open("README.md", "r", encoding="utf8") as file:
    readme = file.read()

readme = readme.split("<!-- MODEL_TABLE_START -->")
readme[1] = readme[1].split("<!-- MODEL_TABLE_END -->")[1]
readme = readme[0] + "<!-- MODEL_TABLE_START -->\n" + markdown_table + "<!-- MODEL_TABLE_END -->" + readme[1]

with open("README.md", "w+", encoding="utf8") as file:
    file.write(readme)

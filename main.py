from texte_scraper.db.database import CreoleTextDatabase
from texte_scraper.models.texte import Texte
from texte_scraper.services.ayibopost_scraper import TexteScraper
import re

creole_text_db = CreoleTextDatabase(
    "localhost", "root", "", "")

# add data
urls = []
for url in urls:
    scraper = TexteScraper(url)
    text = scraper.scrape()

    if text:
        try:
            # creole_text_db.insert_into_textes(text)
            print(f"{str(text.id_text)}:Data added successfully \n")
        except Exception as e:
            print(e)
    else:
        print(f"Failed to retrieve the page.")


creole_text_db.close_connection


# Read the file
with open('test.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Add a new line after each '.', '?', or '!'
modified_content = re.sub(r'([.?!])', r'\g<0>\n', content)

# Split the modified content into lines and capitalize each line
capitalized_lines = [line.capitalize()
                     for line in modified_content.split('\n')]

# Join the capitalized lines with newline characters
final_content = '\n'.join(capitalized_lines)

# Write the modified content back to the file
with open('data.txt', 'w', encoding='utf-8') as file:
    for line in capitalized_lines:
        file.write(line.replace(' ,', ',').replace(' .', '.').replace(
            ' :', ':').replace(' !', '!').capitalize() + '\n')

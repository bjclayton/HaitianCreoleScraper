from texte_scraper.db.database import CreoleTextDatabase
from texte_scraper.models.texte import Texte
from texte_scraper.services.ayibopost_scraper import TexteScraper


creole_text_db = CreoleTextDatabase(
    "localhost", "root","", "")

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


creole_text_db.close_connection()

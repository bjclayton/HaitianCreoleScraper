import requests
from bs4 import BeautifulSoup
from texte_scraper.models.texte import Texte


class TexteScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            titre = ""
            auteur = ""
            source = self.url
            date_publication = ""
            contenu = ""
            categorie = ""
            etiquettes = ""

            # titre = soup.find("h1", class_="entry-title").text.strip()
            date_publication = soup.find("time", class_="entry-date").text.strip()

            categorie = [el.text.strip()
                        for el in soup.find_all("li", class_="entry-category")]
            categorie = ", ".join(categorie)

            div_content = soup.find("div", class_="td-post-content")
            all_p_tag = div_content.findAll("p")

            if all_p_tag[-1].find("strong"):
                auteur = all_p_tag[-1].find("strong").text.strip()
                all_p_tag = all_p_tag[:-1]
            elif all_p_tag[-2].find("strong"):
                auteur = all_p_tag[-2].find("strong").text.strip()
                all_p_tag = all_p_tag[:-2]


            for tag in all_p_tag:
                contenu += tag.text.strip()

            text = Texte(titre, auteur, source, date_publication,
                        contenu, categorie, etiquettes)
            return text
        else:
            return None



urls = [
    "https://rezonodwes.com/?p=269731",
    "https://rezonodwes.com/?p=251522",
    "https://rezonodwes.com/?p=312914",
    "https://rezonodwes.com/?p=193608",
    "https://rezonodwes.com/?p=134770",
    "https://rezonodwes.com/?p=129689",
    "https://rezonodwes.com/?p=239342",
    "https://rezonodwes.com/?p=317167",
    "https://rezonodwes.com/?p=112088",
    "https://rezonodwes.com/?p=113709",
    "https://rezonodwes.com/?p=232593",
    "https://rezonodwes.com/?p=306940",
    "https://rezonodwes.com/?p=303747",
    "https://rezonodwes.com/?p=311904",
    "https://rezonodwes.com/?p=312458",
    "https://rezonodwes.com/?p=321514",
    "https://rezonodwes.com/?p=243937",
    "https://rezonodwes.com/?p=315280",
    "https://rezonodwes.com/?p=300749",
    "https://rezonodwes.com/?p=317973",
]

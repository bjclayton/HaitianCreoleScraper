import requests
from bs4 import BeautifulSoup
# from texte_scraper.models.texte import Texte


class TexteScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        print(response)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            titre = ""
            auteur = ""
            source = self.url
            date_publication = ""
            contenu = ""
            categorie = ""
            etiquettes = ""

            titre = soup.find("h1", itemprop="headline").text.strip()
            div_cat = soup.find("div", class_="post-category")
            categorie = [el.text.strip() for el in div_cat.find_all("a")]
            categorie = ",".join(categorie)
            

            date_publication = soup.find("div", class_="post-date").text.strip()
            auteur = soup.find("div", class_="post-author").find("a").text.strip()

            # post_content = soup.find("div", class_="entry-content")
            # for h4_tag in post_content.findAll("h4"):
            #     contenu += h4_tag.text.strip()

            # etiquettes = [el.text.strip()
            #             for el in soup.find_all("a", rel="tag")]
            # etiquettes = ", ".join(etiquettes)

            text = (titre, auteur, source, date_publication,
                        contenu, categorie, etiquettes)
            return text
        else:
            return None


scraper = TexteScraper("https://espaskreyol.org/yon-apesi-sou-istwa-lang-kreyol-nou-an/")
print(scraper.scrape())

urls = [
    "https://espaskreyol.org/yon-apesi-sou-istwa-lang-kreyol-nou-an/",
    "https://espaskreyol.org/istwa-lang-ak-kilti-kreyol/",
    "https://espaskreyol.org/pou-ki-sa-pou-nou-rive-ki-bo/",
    "https://espaskreyol.org/pwoveb-nan-dyaspora-ki-wol-yo/",
    "https://espaskreyol.org/respe-nan-lang-nou-respe-pou-demokrasi-dezyem/",
    "https://espaskreyol.org/pwoveb-nan-dyaspora-ki-wol-yo/",
    "https://espaskreyol.org/jewografi-kreyol/",
    "https://espaskreyol.org/istwa-lang-ak-kilti-kreyol/",
]


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

            # find all categories and etiquettes
            titre = soup.find(
                "h1", class_="entry-title entry-title--lg").text.strip()
            date_publication = soup.find(
                "time", class_="time published").text.strip()
            auteur = soup.find("a", rel="author").text.strip()

            # get the content
            article_div = soup.find("div", class_="single-body")
            contenu += article_div.find("h3").text.strip()

            for p_tag in article_div.find_all("p"):
                if p_tag.find('strong') is None or p_tag.find('a') is None:
                    contenu += p_tag.text.strip()

            text = Texte(titre, auteur, source, date_publication,
                        contenu, categorie, etiquettes)
            return text
        else:
            return None


urls = [
    "https://ayibopost.com/timoun-ki-pale-kreyol-kontinye-ap-pase-move-moman-nan-lekol-an-ayiti/",
    "https://ayibopost.com/foutbol-fe-lang-kreyol-la-vin-pi-rich/",
    "https://ayibopost.com/lagrandyab-ak-lang-pep-souvren/",
    "https://ayibopost.com/lang-kreyol-la-sibi-anpil-diskriminasyon-nan-medya-an-ayiti/",
    "https://ayibopost.com/rezososyo-ap-demantibile-lang-kreyol-la-an-menm-tan-se-yon-bel-opotinite/",
    "https://ayibopost.com/8-lang/",
    "https://ayibopost.com/ayibopost-lanse-operasyon-ozetazini/"
]

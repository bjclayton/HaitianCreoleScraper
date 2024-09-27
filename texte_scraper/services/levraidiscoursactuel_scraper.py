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

            titre = soup.find("h1", class_="entry-title").text.strip()
            date_publication = soup.find("time", class_="entry-date").text.strip()
            auteur = soup.find("a", class_="url fn n").text.strip()

            post_content = soup.find("div", class_="entry-content")
            for h4_tag in post_content.findAll("h4"):
                contenu += h4_tag.text.strip()

            # etiquettes = [el.text.strip()
            #             for el in soup.find_all("a", rel="tag")]
            # etiquettes = ", ".join(etiquettes)

            text = Texte(titre, auteur, source, date_publication,
                        contenu, categorie, etiquettes)
            return text
        else:
            return None


urls = [
    "https://levraidiscoursactuel.com/2013/01/07/pwodiksyon-sekirite-gouvenen-ak-demokrasitwa-gwo-wol-sitwayen-yo-ansanm-ak-twa-gwo-moso-pouvwa-yo/",
    "https://levraidiscoursactuel.com/2013/01/07/pwodiksyon-sekirite-gouvenen-ak-demokrasitwa-gwo-wol-sitwayen-yo-ansanm-ak-twa-gwo-moso-pouvwa-yo-2/",
    "https://levraidiscoursactuel.com/2019/02/17/jean-henry-ceantdiskou-mesaj-premye-minis-ayiti-10-jou-apre-pep-la-revolte-kont-prezidan-jovnel-moyiz/#",
    "https://levraidiscoursactuel.com/2014/12/15/discours-de-demission-du-premier-ministre-laurent-s-lamothe/#",
    "https://levraidiscoursactuel.com/2018/10/28/jhonny-victor-chante-kreyol-danse-petro-par-jhonny-victor/",
    "https://levraidiscoursactuel.com/2013/01/15/tan-ki-pa-tan/#",
    "https://levraidiscoursactuel.com/2013/01/21/pwodiksyon-sekirite-gouvenen-ak-demokrasi-dezyem-pati/#",
]


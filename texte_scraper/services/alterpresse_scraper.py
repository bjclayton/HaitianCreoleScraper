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
            categorie = "Atik"
            etiquettes = ""

            categorie = soup.find(
                "a", class_="entry__meta-category").text.strip()
            date_publication = soup.find(
                "li", class_="entry__meta-date").text.strip()
            titre = soup.find("h1", class_="thumb-entry-title").text.strip()

            div_content = soup.find("div", class_="entry__article")
            if div_content:
                for p_tag in div_content:
                    contenu += p_tag.text.strip()

            text = Texte(titre, auteur, source, date_publication,
                    contenu, categorie, etiquettes)
            return text
        else:
            return None


urls = [
    "https://www.alterpresse.org/spip.php?article29024",
    "https://www.alterpresse.org/spip.php?article29042",
    "https://www.alterpresse.org/spip.php?article29039",
    "https://www.alterpresse.org/spip.php?article29184",
    "https://www.alterpresse.org/spip.php?article29183",
    "https://www.alterpresse.org/spip.php?article29177",
    "https://www.alterpresse.org/spip.php?article29170",
    "https://www.alterpresse.org/spip.php?article29163",
    "https://www.alterpresse.org/spip.php?article29159",
    "https://www.alterpresse.org/spip.php?article29139",
    "https://www.alterpresse.org/spip.php?article29140",
    "https://www.alterpresse.org/spip.php?article29141",
    "https://www.alterpresse.org/spip.php?article29051",
    "https://www.alterpresse.org/spip.php?article29098",
    "https://www.alterpresse.org/spip.php?article29046",
    "https://www.alterpresse.org/spip.php?article29043",
    "https://www.alterpresse.org/spip.php?article29771",
    "https://www.alterpresse.org/spip.php?article29753",
    "https://www.alterpresse.org/spip.php?article29703",
    "https://www.alterpresse.org/spip.php?article29694",
    "https://www.alterpresse.org/spip.php?article29666",
    "https://www.alterpresse.org/spip.php?article29644",
    "https://www.alterpresse.org/spip.php?article29587",
    "https://www.alterpresse.org/spip.php?article29491",
    "https://www.alterpresse.org/spip.php?article29486",
    "https://www.alterpresse.org/spip.php?article29483",
    "https://www.alterpresse.org/spip.php?article29420",
    "https://www.alterpresse.org/spip.php?article29357",
    "https://www.alterpresse.org/spip.php?article29327",
    "https://www.alterpresse.org/spip.php?article10683",
    "https://www.alterpresse.org/spip.php?article28995",
    "https://www.alterpresse.org/spip.php?article28953",
    "https://www.alterpresse.org/spip.php?article28933",
    "https://www.alterpresse.org/spip.php?article28852",
    "https://www.alterpresse.org/spip.php?article28849",
    "https://www.alterpresse.org/spip.php?article28832",
    "https://www.alterpresse.org/spip.php?article28833",
    "https://www.alterpresse.org/spip.php?article28808",
    "https://www.alterpresse.org/spip.php?article28805",
    "https://www.alterpresse.org/spip.php?article28803",
    "https://www.alterpresse.org/spip.php?article28799",
    "https://www.alterpresse.org/spip.php?article28788",
    "https://www.alterpresse.org/spip.php?article28782",
    "https://www.alterpresse.org/spip.php?article28785",
    "https://www.alterpresse.org/spip.php?article28784",
    "https://www.alterpresse.org/spip.php?article28767",
    "https://www.alterpresse.org/spip.php?article28760",
    "https://www.alterpresse.org/spip.php?article28758",
    "https://www.alterpresse.org/spip.php?article28739",
    "https://www.alterpresse.org/spip.php?article28733",
    "https://www.alterpresse.org/spip.php?article28729",
    "https://www.alterpresse.org/spip.php?article28722",
    "https://www.alterpresse.org/spip.php?article28711",
    "https://www.alterpresse.org/spip.php?article28701",
    "https://www.alterpresse.org/spip.php?article28697",
    "https://www.alterpresse.org/spip.php?article28679",
    "https://www.alterpresse.org/spip.php?article28691",
]

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
            source = ""
            date_publication = ""
            contenu = ""
            categorie = "Atik"
            etiquettes = ""

            post_date_div = soup.find("div", class_="post-date ml-0")

            if post_date_div:
                day = post_date_div.find("span", class_="day").text.strip()
                month = post_date_div.find("span", class_="month").text.strip()
                date_publication = f"{day} {month}"

            post_content_div = soup.find("div", class_="post-content ml-0")

            if post_content_div:
                titre = post_content_div.find("a", rel="bookmark").text.strip()
                source = post_content_div.find("a", href=True)["href"]

                etiquettes_div = post_content_div.find(
                    "div", class_="post-meta")
                etiquettes = [a.text.strip()
                            for a in etiquettes_div.find_all("a", rel="tag")]
                etiquettes = ",".join(etiquettes)

                contenu = ""
                for p_tag in post_content_div.find_all("p"):
                    if "&nbsp;" in p_tag.get_text():
                        break
                    contenu += p_tag.get_text().strip()

            text = Texte(titre, auteur, source, date_publication,
                        contenu, categorie, etiquettes)
            return text
        else:
            return None


urls = [
    "https://ankreyol.net/jounen-entenasyonal-lang-manman-pou-yon-sistem-edikasyon-ki-bay-bonjan-rezilta/",
    "https://ankreyol.net/sans-manje-nan-kek-ekspresyon-kreyol/",
    "https://ankreyol.net/eske-ou-pale-jagon-kreyol/",
    "https://ankreyol.net/literati-kreyol-mo-chwazi/",
    "https://ankreyol.net/konbyen-tan-yon-sitiyasyon-aprantisaj-dwe-dire/",
    "https://ankreyol.net/kisa-yon-sitiyasyon-aprantisaj-ye/",
    "https://ankreyol.net/atelye-ekriti-ti-liv-dijital-nan-monreyal/",
    "https://ankreyol.net/pwogram-selebrasyon-jounen-lang-matenel-nan-fakilte-lengwistik-aplike/",
    "https://ankreyol.net/chantez-stephanie-sejour-antoine-ki-gen-non-atis-li-tifan-pot-pawol-15em-edisyon-mwa-kreyol-monreyal-la/",
    "https://ankreyol.net/adye-wida/",
    "https://ankreyol.net/yon-michan-liv-grame-kreyol-ayisyen/",
    "https://ankreyol.net/konferans-grame-deskriptif-kreyol-ayisyen-an-yon-zouti-analiz-san-parey/",
    "https://ankreyol.net/plis-pase-25-nouvo-liv-an-kreyol-nan-livres-en-folie-2016-la/"
]

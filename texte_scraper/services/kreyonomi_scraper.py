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
            category_tag = soup.find_all("a", rel="category tag")
            if category_tag:
                categorie = category_tag[0].text.strip()
                etiquettes = [el.text.strip() for el in category_tag[1:]]
                etiquettes = ",".join(etiquettes)

            # find the title
            titre = soup.find('h1', class_="entry-title").text.strip()

            # get the content
            post_content_div = soup.find('div', class_="entry-content")
            if post_content_div:
                for p_tag in post_content_div.find_all('p'):
                    other_content = ""
                    if post_content_div.find('ol'):
                        other_content = post_content_div.find('ol')
                        for el in other_content.findAll('li'):
                            contenu += el.text.strip()
                    elif post_content_div.find('ul'):
                        other_content = post_content_div.find('ul')
                        for el in other_content.findAll('li'):
                            contenu += el.text.strip()

                    contenu += p_tag.text.strip()

                auteur = soup.find('h3', class_="author-name").text.strip()
                date_publication = soup.find('time').text.strip()

            text = Texte(titre, auteur, source, date_publication,
                         contenu, categorie, etiquettes)
            return text
        else:
            return None



urls = [
    "https://kreyonomi.wordpress.com/2023/10/11/bilten-kreyonomi-1-oktob-2023-rel-lespwa/",
    "https://kreyonomi.wordpress.com/2023/07/25/sel-yod/",
    "https://kreyonomi.wordpress.com/2023/10/26/yon-prensip-ki-chita-deye-tout-riches/",
    "https://kreyonomi.wordpress.com/2023/03/12/panik-labank-yon-ti-kout-je-sou-kriz-finansye-silicon-valley-bank-lan-etazini/",
    "https://kreyonomi.wordpress.com/2021/09/07/gwo-grangou-nan-nip-ak-nan-sid-apre-katastwof-yo/",
    "https://kreyonomi.wordpress.com/2021/09/06/mayi-peyi-a-ka-toke-kon-ak-mayi-enpote-a/",
    "https://kreyonomi.wordpress.com/2021/09/06/kesyon-raz-kiryozite-lasyans-filozofi/",
    "https://kreyonomi.wordpress.com/2021/09/05/manje-peyi-ayiti/",
    "https://kreyonomi.wordpress.com/2021/08/20/solidarite-peyizan-14out2021/",
    "https://kreyonomi.wordpress.com/2021/08/17/tranblemannte-goudougoudou-14out2021/",
    "https://kreyonomi.wordpress.com/2021/07/03/matematik-envansyon-oswa-dekouvet/",
    "https://kreyonomi.wordpress.com/2021/03/01/risk-ak-ensetitid-nan-travay-late/",
    "https://kreyonomi.wordpress.com/2020/05/27/lwademann/",
    "https://kreyonomi.wordpress.com/2020/05/29/komeslib/",
    "https://kreyonomi.wordpress.com/2020/06/04/kreyonomipodcast/",
    "https://kreyonomi.wordpress.com/2020/06/24/langaj/",
    "https://kreyonomi.wordpress.com/2020/07/12/dyasporapodcast/",
    "https://kreyonomi.wordpress.com/2020/08/07/ekonomipratik/",
    "https://kreyonomi.wordpress.com/2020/09/08/reskiye/",
    "https://kreyonomi.wordpress.com/2020/09/13/lapatri/",
    "https://kreyonomi.wordpress.com/2020/09/18/jodipademen/",
    "https://kreyonomi.wordpress.com/2020/10/02/mwakreyol/",
    "https://kreyonomi.wordpress.com/2020/10/27/jounenkreyol/",
    "https://kreyonomi.wordpress.com/2020/12/02/sezon2/",
    "https://kreyonomi.wordpress.com/2020/12/11/nouvo-sezon/",
    "https://kreyonomi.wordpress.com/2021/01/04/mlm/",
    "https://kreyonomi.wordpress.com/2020/05/27/lwademann/",
    "https://kreyonomi.wordpress.com/2020/05/24/orijincovid/",
    "https://kreyonomi.wordpress.com/2020/05/19/tiyemalere/",
    "https://kreyonomi.wordpress.com/2020/05/16/covidayiti/",
    "https://kreyonomi.wordpress.com/2020/05/08/lekolkreyol/",
    "https://kreyonomi.wordpress.com/2020/05/05/banmprev/",
    "https://kreyonomi.wordpress.com/2020/04/21/siygri/",
    "https://kreyonomi.wordpress.com/2016/11/14/yo-pa-konn-achte-chat-nan-sak/"
]

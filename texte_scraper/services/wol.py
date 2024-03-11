import re
import requests
from bs4 import BeautifulSoup

def process_line(line):
    line = re.sub(r'\([^)]*\)', '', line)
    line = re.sub(r'—.*$', '', line)
    line = re.sub(r'\[.*?\]', '', line)
    return line


urls = [
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023200",
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023201",
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023202",
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023203",
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023204",
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023205",
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023206",
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023207",
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023208",
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023209",
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023210",
    "https://wol.jw.org/ht/wol/d/r60/lp-cr/1102023211",
]

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        theme_scrp_paragraphs = soup.find_all('p', class_='themeScrp')
        sb_paragraphs = soup.find_all('p', class_='sb')
                
        with open('out.txt', 'a', encoding='utf-8') as out:
            for themeScrp, sb in zip(theme_scrp_paragraphs, sb_paragraphs):
                sb_text = process_line(sb.text)
                themeScrp_text = process_line(themeScrp.text)
                out.write(themeScrp_text + " " + sb_text + '\n')

        print("Paragraphs written to files successfully.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

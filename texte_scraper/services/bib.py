import re
import requests
from bs4 import BeautifulSoup
import time  

def clean_text(input_text):
    return re.sub(r'[0-9\*\+]', '', input_text)

def scrape_and_write(url, output_file):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        sb_paragraphs = soup.find_all('p', class_='sb')

        with open(output_file, 'a', encoding='utf-8') as out:
            for sb in sb_paragraphs:
                sb_text = sb.text
                cleaned_text = clean_text(sb_text)
                out.write(f"{cleaned_text}\n")
    else:
        print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")

def main():
    number_of_chapters = {
    1: 50, 2: 40, 3: 27, 4: 36, 5: 34, 6: 24, 7: 21, 8: 4, 9: 31, 10: 24,
    11: 22, 12: 25, 13: 29, 14: 36, 15: 10, 16: 13, 17: 10, 18: 42, 19: 150,
    20: 31, 21: 12, 22: 8, 23: 66, 24: 52, 25: 5, 26: 48, 27: 12, 28: 14, 29: 3,
    30: 9, 31: 1, 32: 4, 33: 7, 34: 3, 35: 3, 36: 3, 37: 2, 38: 14, 39: 4, 40: 28,
    41: 16, 42: 16, 43: 13, 44: 6, 45: 6, 46: 4, 47: 4, 48: 4, 49: 4, 50: 3, 51: 3,
    52: 5, 53: 5, 54: 3, 55: 6, 56: 4, 57: 3, 58: 1, 59: 13, 60: 5, 61: 5, 62: 5,
    63: 1, 64: 1, 65: 1, 66: 22
    }

    for index, chapter in number_of_chapters.items():
        for i in range(1, chapter + 1):
            url = f"https://wol.jw.org/ht/wol/b/r60/lp-cr/nwt/{index}/{i}#study=discover"
            output_file = 'out.txt'

            scrape_and_write(url, output_file)
            print(f"Paragraphs written to files successfully. ({index}, {i})")

            time.sleep(1)

if __name__ == "__main__":
    main()

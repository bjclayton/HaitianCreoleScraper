import requests
from bs4 import BeautifulSoup

with open('data/creole_words.txt', 'r', encoding='utf-8') as file:
    words = file.read().split(',')

print(len(words))
count = 1
notfound = []

with open('out.txt', 'a', encoding='utf-8') as outfile:
    for word in words:
        url = f"https://langkreyolla.com/diksyone.php?mo={word}"

        if count > 2872:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            first_dd = soup.find('dd')
            if first_dd:
                p_tag = first_dd.find('p')
                
                if p_tag:
                    outfile.write(p_tag.get_text().replace('Egz :', '') + "\n")
                    print(f"Data added. {count}")
                else:
                    notfound.append(word)
                    print(f"No <p> tag found within the first <dd> tag. {word}")
            else:
                notfound.append(word)
                print(f"No <dd> tag found on the webpage. {word}")
        count += 1

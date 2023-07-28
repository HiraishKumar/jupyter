# from bs4 import BeautifulSoup
# import requests
# import csv

# url='https://www.hackerrank.com/domains/java'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# source = requests.get(url, headers=headers)
# if source.status_code == 200:
#     soup = BeautifulSoup(source.text, 'lxml')
# else:
#     print(f"Failed to fetch data from {url}")
    
# challenge_cards = soup.find_all('h4',class_='challengecard-title')

# with open('jupyter\Web_sca\hackrank.csv', 'w', encoding='utf-8') as write_file:
#     csvwriter = csv.writer(write_file)
#     csvwriter.writerow(['Name'])

#     for card in challenge_cards:
#         name = card.text.strip()
#         csvwriter.writerow([name])

from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.hackerrank.com/domains/java'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

source = requests.get(url, headers=headers)

if source.status_code == 200:
    soup = BeautifulSoup(source.text, 'lxml')
else:
    print(f"Failed to fetch data from {url}")

# Assuming the challenge names are in elements with class "challengecard-title"
challenge_cards = soup.find_all('h4', class_='challengecard-title')

with open('jupyter\Web_sca\hackrank.csv', 'w', encoding='utf-8') as write_file:
    csvwriter = csv.writer(write_file)
    csvwriter.writerow(['Name'])

    for card in challenge_cards:
        name = card.text.strip()
        csvwriter.writerow([name])
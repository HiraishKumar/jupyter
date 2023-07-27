import csv
import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.flipkart.com/search?q=laptop%203060&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

# items = BeautifulSoup(requests.get(url).text, 'lxml').find_all('div', class_="_13oc-S")

def getdata(url):
    source = requests.get(url)
    if source.status_code == 200:
        soup = BeautifulSoup(source.text, 'lxml')
        return soup
    else:
        print(f"Failed to fetch data from {url}")
        return None

def getnextpage(soup):
    # this will return the next page URL
    pages = soup.find('div', class_='_2MImiq')
    if pages:
        next_page_link = pages.find('nav', class_='yFHi8N').find('a', class_='_1LKTO3')
        if next_page_link:
            return 'https://www.flipkart.com' + str(next_page_link['href'])
    else:
        return None
    
def csv_writer(items_):
    with open('jupyter\Web_sca\output.csv', 'a', encoding='utf-8-sig') as write_file:
            csvwriter = csv.writer(write_file)
            csvwriter.writerow(['Name', 'Price']) 

            for item in items_:
                name = item.find('div', class_="_4rR01T").text
                price = item.find('div', class_="_30jeq3 _1_WHN1").text
                csvwriter.writerow([name, price])

i = 0
while i < 2:
    data = getdata(url)
    if data is None:
        break
    url = getnextpage(data)
    if url is None:
        print("No more pages to scrape.")
        break
    csv_writer(data.find_all('div', class_="_13oc-S"))    
    i += 1
    time.sleep(2)  # Adding a delay to avoid aggressive scraping and rate limiting


import requests
from bs4 import BeautifulSoup
import csv

source = requests.get('https://www.flipkart.com/search?q=laptop%203060&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
items = BeautifulSoup(source.text, 'lxml').find_all('div', class_="_13oc-S")

with open('jupyter\Web_sca\output.csv', 'w', encoding='utf-8-sig') as write_file:
    csv_writer = csv.writer(write_file)
    csv_writer.writerow(['Name', 'Price']) 

    for item in items:
        name = item.find('div', class_="_4rR01T").text
        price = item.find('div', class_="_30jeq3 _1_WHN1").text
        csv_writer.writerow([name, price])



    
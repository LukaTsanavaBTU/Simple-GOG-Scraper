import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

url = "https://www.gog.com/en/games"
pages_start = 1
pages_end = 5
csv_file = open("gog_scraping_results.csv", "w", newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title", "Price"])

for i in range(pages_start, pages_end + 1):
    parameters = {'page': i}
    content = requests.get(url, params=parameters).text
    soup = BeautifulSoup(content, 'html.parser')
    all_tiles = soup.find('div', {'selenium-id': 'paginatedProductsGrid'}).findAll('product-tile')
    for tile in all_tiles:
        title = tile.find('product-title').text.replace('DLC', '[DLC] ').replace("\n", "")
        price = tile.find('span', class_="final-value").text
        csv_writer.writerow([title, price])
    sleep(randint(10, 20))

csv_file.close()

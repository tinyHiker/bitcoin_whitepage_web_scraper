import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/List_of_UFC_champions'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

table = soup.find('table', attrs={'class': 'wikitable'})

rows = table.find_all('tr')[2:]  # Skip the header row

weight_classes = []
title_defenses = []

for row in rows:
    cells = row.find_all('td')
    if len(cells) > 8:  # Only process rows that have enough cells
        weight_class = cells[1].text.strip()
        defenses = cells[7].text.strip()
        if weight_class and defenses.isdigit():
            weight_classes.append(weight_class)
            title_defenses.append(int(defenses))

# Convert weight classes to integers
unique_classes = list(set(weight_classes))
weight_classes = [unique_classes.index(x) for x in weight_classes]


plt.figure(figsize=(10, 6))
plt.plot(weight_classes, title_defenses)
plt.xlabel('Weight Class')
plt.ylabel('Title Defenses')
plt.title('UFC Title Defenses by Weight Class')
plt.show()


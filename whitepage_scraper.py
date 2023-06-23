import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import csv

ht = requests.get('https://www.bitcoin.com/satoshi-archive/whitepaper/').text #Getting HTML of the Bitcoin Whitepaper on bitcoin.com
soup = BeautifulSoup(ht, 'lxml') 

#The main contents of the whitepaper is directly wrapped by this div tag
main_content = soup.find('div', id = 'main-content', class_= 'main-content', role = 'main') 

headings = main_content.find_all('h3') 
heading_list = []

def clean_heading(heading) -> str:
    modified_heading = heading.text.strip()
    
    try:
        cleaned_heading = modified_heading.split('. ', 1)[1]
    except IndexError:
        cleaned_heading = modified_heading
    
    return cleaned_heading
    



for heading in headings:
    cleaned_heading = clean_heading(heading)
    heading_list.append(cleaned_heading)
    
    
    
with open('categories.csv', 'w') as category_file:
    category_writer = csv.writer(category_file, delimiter='\t')
    category_writer.writerow(['Category Title', 'Character Count of Title'])
    
    for heading in heading_list:
        category_writer.writerow([heading, str(len(heading))])
        
    
        












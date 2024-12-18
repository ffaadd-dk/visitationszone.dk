import sys
import requests

from bs4 import BeautifulSoup


URL = "https://politi.dk/lov-og-information/visitationszoner"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"

try:
    r = requests.get(URL, headers={"User-Agent": UA})
except:
    print("Failed to connect, skipping update")
    sys.exit(0)

s = BeautifulSoup(r.text, features="html.parser")
el = s.find("div", class_="QAndAAccordion")

cards = el.find_all("div", class_="card")

f = open("current.txt", "w")

for card in cards:
    area = card.find("div", class_="card-header") \
            .get_text() \
            .strip()
    
    description = card.find("div", class_="card-body") \
            .get_text() \
            .strip()
            
    if "ingen aktuelle visitationszoner" in description.lower():
        continue

    f.write("###\n")
    f.write(area + "\n")
    f.write(description + "\n")
    f.write("###\n")
    

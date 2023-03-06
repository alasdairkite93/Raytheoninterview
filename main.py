import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

from collections import Counter

keywords = ['Viruses', 'Bugs', 'DDOS', 'Patches', 'Vulnerabilities', 'Threats']
filenames = ['cyber-security.xml', 'DDOS-file.txt', 'online-data.json', 'Secure-file.txt']

dict = {"Viruses":0, "Bugs":0, "DDOS":0, "Patches":0, "Vulnerabilities":0, "Threats":0}

#Case Sensistive search

for file in filenames:
    with open(file, 'r') as r:
        data = r.read()

        if "xml" in file:
            soup = BeautifulSoup(data, "xml")
            items = soup.findAll('item')
            for item in items:
                if item.text in dict:
                    dict[item.text] += 1

            descriptions = soup.findAll('description')
            for description in descriptions:
                text = description.text.split(" ")
                for word in text:
                    if word.casefold() in dict:
                        dict[word] += 1

        if "txt" in file:
            text = data.split(" ")
            for word in text:
                word = word.replace('.', '')
                if word in dict:
                    dict[word] += 1
        print(dict)

        if "json" in file:
            print("json")
            json = json.loads(data)
            print(json.keys())
            for word in keywords:
                try:
                    print(json[word])
                except KeyError:
                    pass


print(dict)





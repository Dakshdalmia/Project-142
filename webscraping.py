import requests
import time
import pandas as pd
from bs4 import BeautifulSoup

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
response = requests.get(start_url)

star_data_list=[]
star_name = []
radius = []
mass = []
distance = []

def scrape():
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find_all("table")[7]
    tr_tags = table.find_all("tr")
    
    for tr_tag in tr_tags:
        td_tags = tr_tag.find_all("td")
        row = []
        for td_tag in td_tags:
            row.append(td_tag.text.strip())
        star_data_list.append(row)

    for i in range(1,len(star_data_list)):
        star_name.append(star_data_list[i][0])
        radius.append(star_data_list[i][8])
        mass.append(star_data_list[i][7])
        distance.append(star_data_list[i][5])

scrape()

data = {"Star Name":star_name, "Distance":distance, "Mass":mass, "Radius":radius}

dataframe = pd.DataFrame(data)
dataframe.to_csv("star_data.csv")


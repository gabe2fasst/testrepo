import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://github.com/search?q=python"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

results = soup.find_all('div', class_= "f4 text-normal")

base_url = "https://github.com"
Repo = []
Url = []

for i in results:
    links = i.find_all("a")
    for link in links:
        link_url = base_url + link["href"]
    Repo.append(link.text.strip())
    Url.append(link_url)
        #print(link.text.strip(), link_url)

data = list(zip(Repo,Url))
col = ['Repo','Url']
df = pd.DataFrame(data= data, columns= col)
print(df)

        

        
    
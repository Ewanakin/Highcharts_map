import requests
from bs4 import BeautifulSoup

def get_link(page):
    req = requests.get(page, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0','connection': 'keep-alive'}).content
    soup = BeautifulSoup(req, "html.parser")
    with open('link.txt', 'a') as file:
        for element in soup.find_all("a", attrs={"class": "TopoJSON"}):
            file.write(page+element.get("href")+",")
        for element in soup.find_all("a", attrs={"class": "JS"}):
            file.write(page + element.get("href") + ",")




if __name__ == '__main__':
    get_link("https://code.highcharts.com/mapdata/")
    with open("link.txt", 'r') as file:
        for i in file:
            test = i.split(",")
        print(len(test))
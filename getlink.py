from bs4 import BeautifulSoup
import requests
import re


def link():
    links = []
    page = requests.get("https://m.facebook.com/detikcom/")
    soup = BeautifulSoup(page.content, "html.parser")
    story1 = re.compile(r'\/story\.php\?story\_fbid=[^;]+\;id=[^;]+\;')
    story2 = story1.findall(str(soup))
    for a in story2:
        y = "https://m.facebook.com{}".format(a).replace('amp;', '')
        links.append(y)
        links = list(dict.fromkeys(links))
    print(links)
    return links


if __name__ == '__main__':
    link()

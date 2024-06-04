import requests

from bs4 import BeautifulSoup

with open("data/spotify.html","r") as f:
    html_doc=f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title.string, type(soup.title.string))
print(soup.div)
print(soup.find_all("div"))
print(soup.find_all("div")[1])

for link in soup.find_all("a"):
    print(link.get("href"))

# s=soup.find(id="link3")
# print(s)
# print(s.get("href"))

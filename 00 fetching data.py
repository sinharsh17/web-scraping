import requests

def fetchAndSaveToFile(url,path):
    r=requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)    

url="https://open.spotify.com/artist/6LEG9Ld1aLImEFEVHdWNSB"

fetchAndSaveToFile(url,"data/spotify.html")
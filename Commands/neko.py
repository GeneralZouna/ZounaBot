import requests
import asyncio

def get_neko(lewd=False):
    img = requests.get("https://nekos.life/api/v2/img/"+("neko" if not lewd else "lewd")).json()["url"]
    return img

def get_pat():
    img = requests.get("https://nekos.life/api/v2/img/pat").json()["url"]
    return img


  
def neko_life(keyword):
    # for list of endpoints/keywords check the link
    # https://nekos.life/api/v2/endpoints
    response = requests.get("https://nekos.life/api/v2/img/" + keyword)
    
    if response.status_code <= 400:
        img = response.json()["url"]
    else:
        img = "Error 404"
    return img

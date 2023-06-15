import requests
import json

header = { "X-Riot-Token": "RGAPI-24b76ecc-9bed-41ba-bf3f-f98a185c0112" }

def translate_region(region):
    if region == "EUW":
        region = "euw1"
    elif region == "EUNE":
        region = "eun1"
    elif region == "BR":
        region = "br1"
    elif region == "JP":
        region = "jp1"
    elif region == "KR":
        region = "kr"
    elif region == "LA1":
        region = "la11"
    elif region == "LA2":
        region = "la2"
    elif region == "NA":
        region = "na1"
    elif region == "OC":
        region = "oc1"
    elif region == "RU":
        region = "ru"
    elif region == "TR":
        region = "tr1"
    return region

def translate_selection_region(region):
    if region[0] == "2":
        region = "euw1"
    elif region[0] == "1":
        region = "eun1"
    elif region[0] == "5":
        region = "br1"
    elif region[0] == "6":
        region = "jp1"
    elif region[0] == "4":
        region = "kr"
    elif region[0] == "8":
        region = "la11"
    elif region[0] == "9":
        region = "la2"
    elif region[0] == "3":
        region = "na1"
    elif region[0] == "7":
        region = "oc1"
    elif region[0] == "10":
        region = "ru"
    elif region[0] == "11":
        region = "tr1"
    return region

def league_by_name(name, region):
    res = requests.get(headers=header, url=f"https://{translate_region(region)}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}")
    return json.loads(res.text)

def league_by_puuid(puuid, region):
    res = requests.get(headers=header, url=f"https://{translate_region(region)}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}")
    return json.loads(res.text)

def league_by_summoner(summoner_id, region):
    res = requests.get(headers=header, url=f"https://{translate_region(region)}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}")
    return json.loads(res.text)
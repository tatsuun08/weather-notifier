import requests
import xml.etree.ElementTree as ET
import json



id_list_url = "https://weather.tsukumijima.net/primary_area.xml"
weather_list_url = "https://weather.tsukumijima.net/api/forecast?city="


def get_city_id(root, name) -> dict:
    prefectures = root.findall("channel/{http://weather.livedoor.com/%5C/ns/rss/2.0}source/pref")

    for pref in prefectures:
        if (pref.attrib["title"]==name):
            cities = pref.findall("city")
            break
    city_ids = [{"name":city.attrib["title"], "id":city.attrib["id"]} for city in cities]
    
    return city_ids 


def get_city_weather(area) -> dict:
    #xmlの最上位要素を取得
    response = requests.get(id_list_url)
    root = ET.fromstring(response.text)

    city = get_city_id(root, area)
    url = weather_list_url + city[0]["id"]
    text = requests.get(url).text
    json_file = json.loads(text)


    f = json_file
    city_weather = {
        "name": f["location"]["city"],
        "prefecture": f["location"]["prefecture"],
        "weather": f["forecasts"][0]["telop"],
        "max_tempreture": f["forecasts"][0]["temperature"]["max"]["celsius"],
        "min_tempreture": f["forecasts"][0]["temperature"]["min"]["celsius"],
    }
    return city_weather






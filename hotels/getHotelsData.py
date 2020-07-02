#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests, json

def get_goibibo_data(city_id="8717279093827200968", chk_in="20200704", chk_out="20200705", tvlr="1-2-0", params=(('s', 'popularity'), ('cur', 'INR'), ('tmz', '-330'),)):
    url = 'https://hermes.goibibo.com/hotels/v12/search/data/v3/{}/{}/{}/{}'.format(city_id, chk_in, chk_out, tvlr)
    headers = {
        'authority': 'hermes.goibibo.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'accept': '*/*',
        'origin': 'https://www.goibibo.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.goibibo.com/hotels/find-hotels-in-Goa/8717279093827200968/8717279093827200968/^%^7B^%^22ci^%^22:^%^2220200703^%^22,^%^22co^%^22:^%^2220200704^%^22,^%^22r^%^22:^%^221-2-0^%^22^%^7D/?^{^%^22filter^%^22:^{^}^}^&sec=dom^&cc=IN',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '_abck=026DE62A22F30449BE92840C64AE9D5A~-1~YAAQVW0/F7IDBxBzAQAAy/RJEATPGHM0E6zGTaf2JsjdBAVO88IfUrLFjZNaavQmhY+/rC9z1VrK1F0MFhPox0w58gysF095zIONLosGRrAwUS8fmGNOsobilJE9XOhD9ZtlTIroaLz8o7VPDD6l6R4tXpUjmdacLiQnK8Ki82xDtpzbJfVZf49qjsG76m583YUmq1GvP2YC51w3DFr19CHopt5YqF4e2njYcOTCzeFtb9th3KPAEokMuPAT7pG8b9gfE5jrHR4s/IVe/Z9XrRM0Erp7a/63iSExN81URuzPrVWeRTIdCiHkjGGSkyuiLNIjtf3Q1z4=~0~-1~-1; Domain=.goibibo.com; Path=/; Expires=Fri, 02 Jul 2021 16:09:09 GMT; Max-Age=31536000; Secure',
    }
    try:
        print("requested!")
        response = requests.get(url, headers=headers, params=params)
        print("Response receieved!")
        data = getFilteredData(response.json())
        return data
    except:
        return {'error': 404}


def getFilteredData(data):
    hotels_list = []
    for hotel in data['data']:
        obj = {}
        obj['hotel_name'] = hotel['hn']
        obj['location'] = hotel['l']
        obj['image'] = hotel['t']
        obj['score'] = hotel['gr']
        obj['reviewCount'] = hotel['rec']
        obj['ratingCount'] = hotel['grc']
        obj['reviewCount'] = hotel['rec']
        obj['offeringPrice'] = hotel['opr']
        obj['specialPrice'] = hotel['spr']
        obj['tnc'] = hotel['tnc']
        hotels_list.append(obj)
    return hotels_list


def getCitiesMapping():
    f = open('hotels/map.json', 'r')
    data = json.load(f)
    return data

def getSampleHotels():
    f = open('hotels/data.json' ,'r')
    data = json.load(f)
    return data

if __name__ == "__main__":
    res = get_goibibo_data()
    json.dump(res, open("data.json", 'w'))
    print(res)

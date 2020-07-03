#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests, json

def get_goibibo_data(city_id="8717279093827200968", chk_in="20200704", chk_out="20200705", tvlr="1-2-0", params=(('s', 'popularity'), ('cur', 'INR'), ('tmz', '-330'),)):
    print(city_id, chk_in, chk_out, tvlr)
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
        'cookie': 'go_ct=09186a3a90b1645564d040d80c3963f6; go_tf_lc=%22go_tf_direct%22; go_tf_direct=%22%22; go_fix2=; tvc_sm_lpc=not_set%20/%20not_set%20/%20(not%20set); _gcl_au=1.1.1677971384.1593635158; bm_sz=D687FD1915519D1AD32A768B12BB11A9~YAAQPnUsMW3+Eu9yAQAADanSEQiBXiHyJVtXHNG+YJ1QDFT8ozw1wJ+Pp+BQxzkYowGwHjjW2bcXNzDbBcVNVI7A7i/QZZHK5r0wTSWFNF3HjG4bWTdcluqWew/c+Y0QzhO/Eo670Out3+YXw3bBHASe2yPjXbZRoH6h5D/rkXuKG6GHFnsS5g0k4ixmq651Lw==; go_attrib_sess_temp=%22go_tf_direct%22; ak_bmsc=4344B7C0777DE5406A2FA6029F8E5AA7312C753E192200002D6BFE5E042EB545~plyU50Tu/F2ujtIaXR9zEwppOQ9fB8KZf6rTWoDBB9cVi+j9kdbxFnj57GgmQqwbVc5V/Aoh4oAPzGlXIzuT5hKeIUw3XD3/+6guiupCFcqE7OLiv4kg/1yCjyZq9wR7i0VoXjYLbEJV1JMuQrmenR8Ck2Gb4s/t/X7SjFtSDbTOSlIESzLxygdxsr6rDvvNSdtPX3/Pck001OO4URuystnAmIkH1MyRKvqx+MsKwWayK46UeNWKPbJ9zPYFzbM7om; _fbp=fb.1.1593731890625.837564011; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.1622839858.1593731891; tvc_sess_alive=1; tvc_setShoppers=0|0|0|0; ls_sm_lpc24=not_set%20/%20not_set%20/%20(not%20set); _ga_6M7BM6XZ7L=GS1.1.1593731890.1.0.1593731892.0; _ga=GA1.2.1663740450.1593635160; _hjid=06fda338-4264-4414-ad30-b4516c1d37fb; _hjAbsoluteSessionInProgress=1; go_dsu=dweb%7Cdirect%7C%7C%7Chotels%7C; _abck=1A67E2E542181C219FCE92AAE6BC416B~0~YAAQPnUsMXf+Eu9yAQAAdmXTEQRCqCq22wHaTZzzNw3ix8hdtFvFP25Ax4iSA0iTvddgvYdFhzpXgLaz9nM5xX6PRVzz/BRydiiaqXQbOwbna6u3drTWLM0k5lATHCcxaqHZ7hE6sOPakeOYqh/IRncHnyO52nQmsgXa+rX9B40I1GT1hpI9QwGrwHNwXStIcvGqcA9Xd5BvtMj9O4QcPTmgjwBpGXtb/aab66krWKSLayiWZlRQOlIyKePpqQHHpI5f+Yj9P+BxwP7HWn3hgMRHqQHByqRc5zNclDjDnnGDhYeAHWF64o8jJLAZY4VbDQXsLFeiaxU=~-1~-1~-1; tvc_sess=%7B%22sm%22:%22(direct)%20/%20(none)%20/%20(not%20set)%22,%22t%22:1593731975840%7D; bm_sv=D2FAEAC6F1B0F5AA7CE134739F16A99A~lV720lPhcDer3A37Ou+NP047BYWaP+paGSaCrQTa7TZZrV7l1mz5znmSfr4re4rXnEq4Bbg2nLfyMOXZ8VVAaeQU7wILOB6gZWy3TDzP4cvnSnMMm+j90pO7KeNIAbgj35GjW2IWEUZLWhIF+xSnnTizFmNmsjc/TkiV+6wDvYM='
    }
    try:
        print("requested!")
        response = requests.get(url, headers=headers, params=params)
        print("Response receieved!")
        # print("res:", response.json())
        data = getFilteredData(response.json())
        return data, 200
    except:
        return {'error': 404}, 404


def getFilteredData(data):
    mainObj = {}
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
    mainObj['hotels'] = hotels_list
    if 'next' in data:
        mainObj['next'] = data['next']
    return mainObj


def getCitiesMapping():
    f = open('hotels/map.json', 'r')
    data = json.load(f)
    return data

def getSampleHotels():
    f = open('hotels/data.json' ,'r')
    data = json.load(f)
    return data

if __name__ == "__main__":
    res, code = get_goibibo_data(city_id="8717279093827200968", chk_in="20200704", chk_out="20200705", tvlr="1-1-0")
    json.dump(res, open("data.json", 'w'))
    print(code, res)

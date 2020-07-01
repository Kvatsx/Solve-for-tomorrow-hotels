#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests, json

def get_goibibo_data(city_id="8717279093827200968", chk_in="20200703", chk_out="20200704", tvlr="1-2-0", params=(('s', 'popularity'), ('cur', 'INR'), ('tmz', '-330'),)):
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
        'cookie': 'go_ct=132a518ca4474c9239ed2ecb83d4c742; go_tf_lc=^%^22go_tf_direct^%^22; go_tf_direct=^%^22^%^22; go_fix2=; tvc_sm_lpc=not_set^%^20/^%^20not_set^%^20/^%^20(not^%^20set); ls_sm_lpc24=not_set^%^20/^%^20not_set^%^20/^%^20(not^%^20set); _gcl_au=1.1.541977418.1593581880; _gid=GA1.2.195236673.1593581881; bm_sz=C17CE81CC683526D5D59857FD91A5F82~YAAQLHUsMbkdIOhyAQAAdSTwCwjCKMqJK0IGrxAHReW2Tb649kiOOfSoSsDcHQ0x/mt2Kc/zLucudV3pdFoC7gbGLUAU0IEAvoWd7OlvNhASOUtziNFHMBR15rGoy6IfKs078NA95X1OQeiT2tuDUTOwz+k0QM0LHFBa5qHW7+JKCnI3EQk9kAI9h+QWAg0XLQ==; go_attrib_sess_temp=^%^22go_tf_direct^%^22; ak_bmsc=712BFFD4A44E21C6F346BF4C50E82DE0312C752C537A000082E9FC5E3C90BF7D~plxIv+1Aus+9t3FPnSDzkK8NXdv8QRRgfTz6opZmvXVzktt8isDYqYaISydH9JrODxGCruXANmhWHOsdicxL1aSXRuODR7JOxUCI49kgtCiyNJu60IY4GztprNjcHjVyFExxSZrvHOSoIRs6rJsAXzleLuhoI/L0mL49sDiL23icFztVmmulftu3JFnwoiT5ED2ZmXfdiZ6NHY04hEWM7P2tWv6v2QsA+8TUwnSXHXlVzUtIMEhi13Pb8AWC+wCAHr; _ga_6M7BM6XZ7L=GS1.1.1593633162.1.0.1593633162.0; go_dsu=dweb^%^7Cdirect^%^7C^%^7C^%^7Chotels^%^7C; tvc_sess_alive=1; tvc_setShoppers=0^|0^|0^|0; _hjid=06fda338-4264-4414-ad30-b4516c1d37fb; _hjAbsoluteSessionInProgress=1; AMP_TOKEN=^%^24NOT_FOUND; _ga=GA1.2.1063745517.1593581881; tvc_sess=^%^7B^%^22sm^%^22:^%^22(direct)^%^20/^%^20(none)^%^20/^%^20(not^%^20set)^%^22,^%^22t^%^22:1593634187869^%^7D; _abck=D2CE9BA8019E78B9DE041B35A2261BF2~-1~YAAQLHUsMakgIOhyAQAA0+3/CwQI4bTBaLTUcKGODquXijDdtk2eTQku1+4esbnUlAr4/YY7HROyBi0S0vbvx5UZRqtFR1Pr5jqm5XbeParqe8cCtTcfbyj+UQNJ78k8Y+ERydyN14Oplfq2mo+ejT+K3BaRBnRND8NKaQOASTWrI+5XQrvywAlcYUja0V+5NSJ3gS5rwMB6DSMJJRJ3ZIaOUsGR3booYW5DBdowF0S2zz2wuFWXNbh28cdL6qi+jN21n+lmQi/gCWq7zxLTiI00k+oaRT+nJWdGWi+Yd4sGBvPoijDzDOXrslyo/KViCeSzjTWjwTxQ~-1~-1~-1; bm_sv=285A6CE0F02FA08C56E51A9F3D55848F~qlE+TAYIU/R/uSmGprETzRUZ2APOsOnncyBuxFMgx3pNAHg4BOp/RnJKnX/47++hI246LGQQ6iWh9XK4XuXmknHSY3zGbD/uX+A1I/InJNrRm3tOo9YoFrhY6nhMK3CEBkrwtszXUTxFuxszAReQgIW4If9OBfG87wxS4hlHaVg=',
    }
    try:
        response = requests.get(url, headers=headers, params=params)
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

if __name__ == "__main__":
    res, d = get_goibibo_data()
    json.dump(res, open("data.json", 'w'))
    print(res)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests, json

def get_goibibo_data(city_id="8717279093827200968", chk_in="20200703", chk_out="20200704", tvlr="1-2-0", params=(('s', 'popularity^'), ('cur', 'INR^'), ('tmz', '-330'),)):
    url = 'https://hermes.goibibo.com/hotels/v12/search/data/v3/{}/{}/{}/{}'.format(city_id, chk_in, chk_out, tvlr)
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Accept': '*/*',
        'Origin': 'https://www.goibibo.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()


if __name__ == "__main__":
    res = get_goibibo_data()
    json.dump(res, open("data.json", 'w'))
    print(res)

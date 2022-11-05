import requests
from pprint import pprint

from get_time import get_base

def get_info():
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

    serviceKey = "/RiLDbQOrX1DYkcfCT5/LyQYEKJ3G4If9ktXL8/B8o3aCQfi/S6D0g+OFjWQD+dZa2ru1Iwbasb9TV+IlJU0wA=="

    base_date, base_time = get_base()

    params = {
        'serviceKey': serviceKey,
        'pageNo': '1',
        'numOfRows': '1000',
        'dataType': 'JSON', # XML 에서 JSON 으로 변경
        'base_date': base_date, # 실습하는 날짜로 변경
        'base_time': base_time, # 가장 가까운 시간으로 변경
        'nx': '89', # 수성구 nx
        'ny': '90' # 수성구 ny
    }

    res = requests.get(url=url, params=params)
    res=res.json()
    data=res['response']['body']['items']['item']
    _data = []
    for d in data:
        _data.append((d['category'],d['obsrValue']))

    _data =_data[:4]


    code={'PTY':'강수형태','REH':'습도','RN1':'1시간 강수량','T1H':'온도'}
    rain_info=['없음', '비', '비/눈', '눈', '',  '빗방울', '빗방울눈날림', '눈날림']

    weather_info = {}

    for c, v in _data:
        if c == 'PTY':
            v = rain_info[int(v)]
        else:
            v=float(v)

        weather_info[code[c]] = v

    return weather_info


if __name__ == "__main__":
    info = get_info()
    pprint(info)


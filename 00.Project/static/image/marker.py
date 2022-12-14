!pip install folium
!pip install selenium
!pip install haversine

from operator import index
import folium
import pandas as pd
from folium.features import CustomIcon
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from haversine import haversine

"""03_카카오로컬.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t0IYBN275npUTegH6ZO8Ut8kKJf2-KnY
"""

import requests
from urllib.parse import quote
import pandas as pd
import json

"""API키 가져오기"""

with open('./kakaoapi.txt') as kf:
  kakao_key = kf.read()

"""URL 만들기"""

local_url  = "https://dapi.kakao.com/v2/local/search/address.json"
addr = '광주광역시 동구 산수길35번길 36-2(계림동)'
url = f'{local_url}?query={quote(addr)}'
url

#API Key를 입력하기 위한 헤더를 만들어 줌
header = {'Authorization':f'KakaoAK {kakao_key}'}

"""요청해서 결과 얻기"""

result = requests.get(url, headers=header).json()
result

result.keys()

result['documents'][0].keys()

경도 = float(result['documents'][0]['x'])
위도 = float(result['documents'][0]['y'])
도로명주소 = result['documents'][0]['address_name']


data={
    '장소':[''],
    '자동차정비업체종류':[''],
    '도로명주소':[도로명주소],
    '위도':[위도],
    '경도':[경도],
    '전화번호':['']
}
df = pd.DataFrame(data)


df2 = pd.read_csv('./광주_자동차정비업체.csv')
map = folium.Map(location=[df2.위도.mean(), df2.경도.mean()], zoom_start=17,
max_bounds=True,
min_zoom=17,
max_zoom=17,
min_lat=df.위도[0],
max_lat=df.위도[0],
min_lon=df.경도[0],
max_lon=df.경도[0],
zoom_control=False,
no_touch=True)
folium.Marker(
    location=[df.위도[0], df.경도[0]],
    popup=folium.Popup(df.도로명주소[0], max_width=200),
    tooltip='사고위치',
    icon=folium.Icon('darkred', icon='ok')
).add_to(map)
folium.CircleMarker(
    radius=200,
    location=[df.위도[0], df.경도[0]],
    color="#ffffff",        # RGB, 16진수
    fill=True,
    fill_color="ffffff"
).add_to(map)
map.save('광주시_자동차정비업체-4.html')
map

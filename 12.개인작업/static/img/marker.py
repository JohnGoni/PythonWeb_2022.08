!pip install folium
!pip install selenium

import folium
import pandas as pd
from folium.features import CustomIcon
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver


df = pd.read_csv('./광주_자동차정비업체.csv')
map = folium.Map(location=[df.위도.mean(), df.경도.mean()], zoom_start=17,
max_bounds=True,
min_zoom=17,
max_zoom=17,
min_lat=35.1615,
max_lat=35.1615,
min_lon=126.9042,
max_lon=126.9042,
zoom_control=False,
no_touch=True)
for i in df.index:
    folium.Marker(
        location=[df.위도[i], df.경도[i]],
        popup=folium.Popup(f"<a href='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={df.장소[i]}', target=_'blink'>{df.도로명주소[i]}</a>",
        max_width=100),
        tooltip=df.장소[i]
    ).add_to(map)
folium.Marker(
    location=[35.161894610275986, 126.90426748208054],
    popup=folium.Popup('광주광역시 북구 신안동 162-1', max_width=200),
    tooltip='사고위치',
    icon=folium.Icon('darkred', icon='ok')
).add_to(map)
folium.CircleMarker(
    radius=200,
    location=[35.161894610275986, 126.90426748208054],
    color="#ffffff",        # RGB, 16진수
    fill=True,
    fill_color="ffffff"
).add_to(map)
title_html = '<h3 align="center" style="font-size:20px">자동차 정비업체</h3>'    
map.get_root().html.add_child(folium.Element(title_html))
map.save('광주시_자동차정비업체.html')
map


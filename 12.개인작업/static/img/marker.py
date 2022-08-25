!pip install folium
!pip install selenium

import folium
import pandas as pd
from folium.features import CustomIcon
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver


df2 = pd.read_csv('./광주_자동차정비업체.csv')
df1 = pd.read_csv('./사고지점.csv')
map = folium.Map(location=[df2.위도.mean(), df2.경도.mean()], zoom_start=17,
max_bounds=True,
min_zoom=17,
max_zoom=17,
min_lat=df1.위도[0],
max_lat=df1.위도[0],
min_lon=df1.경도[0],
max_lon=df1.경도[0],
zoom_control=False,
no_touch=True)
for i in df2.index:
    folium.Marker(
        location=[df2.위도[i], df2.경도[i]],
        popup=folium.Popup(f"<a href='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={df2.장소[i]}', target=_'blink'>{df2.도로명주소[i]}</a>",
        max_width=100),
        tooltip=df2.장소[i]
    ).add_to(map)
folium.Marker(
    location=[df1.위도[0], df1.경도[0]],
    popup=folium.Popup(df1.도로명주소[0], max_width=200),
    tooltip='사고위치',
    icon=folium.Icon('darkred', icon='ok')
).add_to(map)
folium.CircleMarker(
    radius=200,
    location=[df1.위도[0], df1.경도[0]],
    color="#ffffff",        # RGB, 16진수
    fill=True,
    fill_color="ffffff"
).add_to(map)
title_html = '<h3 align="center" style="font-size:20px">자동차 정비업체</h3>'    
map.get_root().html.add_child(folium.Element(title_html))
map.save('광주시_자동차정비업체.html')
map


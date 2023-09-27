import pandas as pd
import folium

map = folium.Map([38, -99], zoom_start=5, tiles="OpenStreetMap")
fg = folium.FeatureGroup(name="My Map")


data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html= """ 
Volcano name: <br>
<a href="https://www.google.com/search?q=%%22%s Volcano%%22" target="_blank">%s Volcano</a><br>
Height: %s m
"""

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.CustomIcon("icon.png")))

map.add_child(fg)
map.save("VolMap1.html")

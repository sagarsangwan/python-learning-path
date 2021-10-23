import folium
import pandas
volcanos = pandas.read_csv("s.txt")
#print(volcanos)


map = folium.Map(location= [38.50, -90.09], zoom_start=6, tiles="Stamen Terrain")


lon = list(volcanos["LON"])
lat =  list(volcanos["LAT"])
v_name = list(volcanos["NAME"])
elevtion = list(volcanos["ELEV"])
print(elevtion)
def color_choose(x):
    if x<1000:
        return "green"
    elif 1000<=x<=2000:
        return "orange"
    else:
        return "red"

data_jsn = open("world.json", "r", encoding= "utf-8-sig").read()
fgv = folium.FeatureGroup(name="volcanoes") 



for lt, lg, name, en in zip(lat, lon, v_name, elevtion):
    fgv.add_child(folium.CircleMarker(location=[lt, lg], radius=7, popup = name + "(" +str(en)+ ")", 
    fill_color = color_choose(en), color = "grey", fill_capacity = 3 ))

    
fgp = folium.FeatureGroup(name="population") 

fgp.add_child(folium.GeoJson(data=data_jsn, 
style_function= lambda x : {"fillcolor" : "green" if x["properties"]["POP2005"]<10000000
else "orange" if x["properties"]["POP2005"]<=10000000<= 20000000 else "red"}))

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl(position="topright"))

map.save("map1.html")

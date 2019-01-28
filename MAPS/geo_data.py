import folium
import pandas as pd
from folium.plugins import MarkerCluster



# Moscow
# map = folium.Map(location=[55.753215, 37.622504], zoom_start = 8)
data = pd.read_csv("Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']



#
# #create map
# map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 8,tiles = "Mapbox bright")
#
#
# # #Add Marker
# # folium.Marker(location=[37.4074687,-122.086669], popup = "Google HQ", icon=folium.Icon(color = 'gray')).add_to(map)
#
#
#
# #Multiple Markers
# for coordinates in [[37.4074687,-122.086669],[37.8199286,-122.4804438]]:
#     folium.Marker(location=coordinates, icon=folium.Icon(color = 'green')).add_to(map)
#
# map.save("map1.html")





#add pandas

# # Create base map
# map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles = "Mapbox bright")
#
# #Plot Markers
# for lat, lon, elevation in zip(lat, lon, elevation):
#     folium.Marker(location=[lat, lon], popup=str(elevation)+" m", icon=folium.Icon(color = 'gray')).add_to(map)
#
# #Save the map
# map.save("map1.html")



#Function to change colors
def color_change(elev):
    if(elev < 1000):
        return('green')
    elif(1000 <= elev <3000):
        return('orange')
    else:
        return('red')
		
		
		
#Create base map with blackback
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles = "CartoDB dark_matter")



#Create Cluster
marker_cluster = MarkerCluster().add_to(map)

# #Plot Markers
# for lat, lon, elevation in zip(lat, lon, elevation):
#     folium.Marker(location=[lat, lon], popup=str(elevation), icon=folium.Icon(color = color_change(elevation))).add_to(map)
		
#Plot Markers - new icons
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(elevation)+" m", fill_color=color_change(elevation), color="gray", fill_opacity = 0.9).add_to(marker_cluster)

#Save the map
map.save("map1.html")























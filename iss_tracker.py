import requests
import folium
import time
import math
from folium.features import CustomIcon

# Function to calculate distance between two coordinates
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0 # Radius of the Earth in kilometers
    
    # Convert degrees to radians
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    # Haversine formula
    a = math.sin(delta_phi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c

def track_iss_path():
    path_coordinates = []
    total_distance = 0.0
    print("Starting ISS tracking... (Fetching 5 locations, 10 seconds apart)")
    
    iss_map = folium.Map(zoom_start=3)
    iss_icon_url = "https://upload.wikimedia.org/wikipedia/commons/d/d0/International_Space_Station.svg"
    
    for i in range(5):
        url = "http://api.open-notify.org/iss-now.json"
        try:
            response = requests.get(url)
            data = response.json()
            
            lat = float(data['iss_position']['latitude'])
            lon = float(data['iss_position']['longitude'])
            
            print(f"Point {i+1}: Lat {lat}, Lon {lon}")
            
            # Calculate distance from the previous point if it exists
            if path_coordinates:
                prev_lat, prev_lon = path_coordinates[-1]
                distance = calculate_distance(prev_lat, prev_lon, lat, lon)
                total_distance += distance
            
            path_coordinates.append([lat, lon])
            folium.CircleMarker(location=[lat, lon], radius=3, color="red").add_to(iss_map)
            
            if i < 4:
                time.sleep(10)
                
        except Exception as e:
            print(f"Error fetching data: {e}")
            
    if path_coordinates:
        iss_map.location = path_coordinates[-1]
        
        spaceship_icon = CustomIcon(iss_icon_url, icon_size=(50, 50), icon_anchor=(25, 25))
        
        # Update popup to show the total distance traveled
        popup_text = f"Current ISS Location<br>Traveled: {total_distance:.2f} km"
        
        folium.Marker(path_coordinates[-1], popup=popup_text, icon=spaceship_icon).add_to(iss_map)
        folium.PolyLine(path_coordinates, color="blue", weight=2.5, opacity=1).add_to(iss_map)
        
        iss_map.save("iss_flight_path.html")
        print(f"\nTotal distance tracked: {total_distance:.2f} kilometers.")
        print("Map generated! Open 'iss_flight_path.html' to view it.")

if __name__ == "__main__":
    track_iss_path()
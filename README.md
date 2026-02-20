# 🛰️ ISS Location Tracker

A Python-based tracking script that fetches the real-time location of the International Space Station (ISS) and plots its flight path on an interactive web map.

## 🚀 Features
* **Live API Integration:** Fetches real-time latitude and longitude data from the Open Notify ISS API.
* **Interactive Mapping:** Uses the `folium` library to generate an interactive HTML map showing the exact location.
* **Flight Path Visualization:** Records multiple coordinates over time to draw a flight path trail.
* **Distance Calculation:** Uses the Haversine formula to calculate the total distance (in kilometers) the ISS traveled during the tracking period.
* **Custom UI:** Replaces standard map markers with a custom ISS spaceship icon.

## 🛠️ Technologies Used
* **Python**
* **Requests** (API handling)
* **Folium** (Map rendering)
* **Math** (Spherical trigonometry calculations)

## 💻 How to Run
1. Clone this repository.
2. Install the required libraries: `pip install requests folium`
3. Run the script: `python iss_tracker.py`
4. Open the generated `iss_flight_path.html` file in any web browser to view the live map!
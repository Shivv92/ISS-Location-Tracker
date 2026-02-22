from flask import Flask, jsonify
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)  # Allows your HTML map to talk to this Python server

@app.route('/api/radar/iss', methods=['GET'])
def get_space_intelligence():
    try:
        # 1. Fetch raw satellite data
        response = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
        data = response.json()
        
        # 2. Process and upgrade the data (The Pro Feature)
        intelligence_data = {
            "latitude": data['latitude'],
            "longitude": data['longitude'],
            "velocity_kmh": round(data['velocity'], 2),
            "altitude_km": round(data['altitude'], 2),
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data['timestamp'])),
            "orbit_status": "LOCKED",
            "system_health": "OPTIMAL"
        }
        
        # 3. Send to Dashboard
        return jsonify(intelligence_data)

    except Exception as e:
        return jsonify({
            "error": "SATELLITE_UPLINK_FAILED", 
            "details": str(e)
        }), 500

if __name__ == '__main__':
    print("🛰️ Global Space Intelligence Radar Backend INITIALIZED on Port 5000")
    app.run(debug=True, port=5000)
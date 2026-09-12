from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Base route
@app.route('/')
def home():
    return "Welcome to the Public API Demo!"

# API endpoint route
@app.route('/fact')
def get_cat_fact():
    cat_api_url = "https://catfact.ninja/fact"
    
    try:
        # Fetch a random cat fact from the external API
        response = requests.get(cat_api_url, timeout=5)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Return the JSON response from the Cat Facts API directly
        data = response.json()
        return jsonify(data)
        
    except requests.exceptions.RequestException as e:
        # Return an error message if the external API call fails
        return jsonify({
            "error": "Failed to fetch cat fact",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    # Listens on all interfaces on port 5000 (ideal for Dockerization)
    app.run(host='0.0.0.0', port=5000)

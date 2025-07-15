# andrew_api.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow CORS from any origin

# Global variable to store "Andrew's" current activity and timestamp
andrew_status = {
    "activity": "Probably coding or making coffee ☕️",
    "timestamp": datetime.utcnow().isoformat() + 'Z'
}

@app.route('/activity', methods=['GET'])
def get_activity():
    """
    Returns the current activity and timestamp as a JSON object.
    Example response: {"activity": "Opened Instagram", "timestamp": "2024-06-01T12:34:56Z"}
    """
    return jsonify(andrew_status)

@app.route('/update', methods=['POST'])
def update_activity():
    """
    Updates Andrew's current activity. Expects JSON: {"activity": "..."}
    Updates the timestamp to now. Returns the new status.
    """
    data = request.get_json()
    if not data or 'activity' not in data:
        return jsonify({"error": "Missing 'activity' in request body!"}), 400
    # Update the global status
    andrew_status["activity"] = data["activity"]
    andrew_status["timestamp"] = datetime.utcnow().isoformat() + 'Z'
    return jsonify(andrew_status)

if __name__ == '__main__':
    # Run the API in debug mode for easy development
    print("🟢 AndrewAPI is running! Now everyone can know what Andrew is up to. This is definitely not a privacy violation. 😅")
    app.run(debug=True) 
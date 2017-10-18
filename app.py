import json

from flask import Flask, render_template, request
import requests

APP_ID = ""
API_ACCESS_TOKEN = ""
API_BASE = 'https://api.intercom.io/'
YOUR_ADMIN_ID = ""
HEADERS = {
      'Authorization': 'Bearer {}'.format(API_ACCESS_TOKEN),
      'Accept': 'application/json',
      'Content-Type' : 'application/json'
      }

app = Flask(__name__)

@app.route('/')
def index():
    user = {}
    user['user_id'] = 8476589349837
    user['name'] = "Guy McMan"
    return render_template('index.html', user=user, app_id=APP_ID)     


@app.route('/send_inapp', methods = ['POST'])
def send_inapp():
    user_id = request.form['user_id']
    message_contents = request.form['message_contents']
    payload = {
      "message_type": "inapp",
      "body": message_contents,
      "from": {
        "type": "admin",
        "id": YOUR_ADMIN_ID 
      },
      "to": {
        "type": "user",
        "user_id": user_id
      }
    }
    r = requests.post(API_BASE + "messages", headers=HEADERS, json=payload)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3333)  
    
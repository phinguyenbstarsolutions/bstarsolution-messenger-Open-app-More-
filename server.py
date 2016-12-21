import os
import json
from flask import Flask, request

CONTACT_LIST = [{'userName': 'Phong'}, {'userName': 'Dinh'}, {'userName': 'Antony'}, {'userName': 'Khanh'}, {'userName': 'Tan'}, {'userName': 'Hiep'}]

app = Flask(__name__)

@app.route('/contactList', methods=['GET', 'POST'])
def contactList():
  return json.dumps({'contact': CONTACT_LIST})

@app.route('/', methods=['GET', 'POST'])
def welcome():
  resp = twilio.twiml.Response()
  resp.say("Welcome to Twilio")
  return str(resp)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)

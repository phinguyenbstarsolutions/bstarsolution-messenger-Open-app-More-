import os
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/Contact/List', methods=['GET', 'POST'])
def contactList():
  userName = request.values.get('username')
  return json.dumps(load_data('contacts.json'))


def load_data(data_path, username = None):
    data = None
    
    if data_path is not None:
        # try to open the file as json
        with open(data_path, 'r') as file:
            data = json.load(file)
    for item in data:
        if username == item['userName']:
            data.remove(item)
            break
    return data



@app.route('/', methods=['GET', 'POST'])
def welcome():
  resp = twilio.twiml.Response()
  resp.say("Welcome to Twilio")
  return str(resp)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)

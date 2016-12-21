import os
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/Contact/List', methods=['GET', 'POST'])
def contactList():
  userName = request.values.get('username')
  data = load_data('contacts.json')
  for item in data:
      if userName == item['userName']:
          data.remove(item)
          break
  return json.dumps(data)

@app.route('/api/Transaction/List', methods=['GET', 'POST'])
def transactionList():
    memberId = request.values.get('memberId')
    tmp = load_data('transations.json')
    data = []
    for item in tmp:
        if memberId == item['memberId']:
            data.append(item)
    return json.dumps(data)

def load_data(data_path):
    data = None
    
    if data_path is not None:
        # try to open the file as json
        with open(data_path, 'r') as file:
            data = json.load(file)
    return data



@app.route('/', methods=['GET', 'POST'])
def welcome():
  resp = twilio.twiml.Response()
  resp.say("Welcome to Twilio")
  return str(resp)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)

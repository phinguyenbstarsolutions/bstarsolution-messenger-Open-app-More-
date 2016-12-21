import os
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/OAuth', methods=['POST'])
def signIn():
    userName = request.form['username']
    data = load_data('contacts.json')
    for item in data:
        if userName == item['userName']:
            user = {}
            user['access_token']    = 'BStar Solutions'
            user['token_type']      = 'BStar Solutions'
            user['expires_in']      = 0
            user['UserName']        = item['userName']
            user['PhoneNumber']     = item['phone']
            user['AppEnabled']      = 'true'
            user['.issued']         = 'BStar Solutions'
            user['.expires']        = 'BStar Solutions'
            return json.dumps(user)
    return json.dumps({'message': 'User not exist'})

@app.route('/api/Account/UserInfo', methods=['POST'])
def userInfo():
    userName = request.form['username']
    data = load_data('contacts.json')
    for item in data:
        if userName == item['userName']:
            user = {}
            user['userid']      = item['id']
            user['fullName']    = item['name']
            user['phoneNumber'] = item['phone']
            user['address']     = item['address']
            user['name']        = item['userName']
            return json.dumps(user)
    return json.dumps({'message': 'User not exist'})


@app.route('/api/Contact/List', methods=['POST'])
def contactList():
  userName = request.form['username']
  data = load_data('contacts.json')
  for item in data:
      if userName == item['userName']:
          data.remove(item)
          break
  return json.dumps(data)

@app.route('/api/Transaction/List', methods=['POST'])
def transactionList():
    memberId = request.form['memberId']
    tmp = load_data('transations.json')
    data = []
    for item in tmp:
        if memberId == str(item['memberId']):
            data.append(item)
    return json.dumps(data)

def load_data(data_path):
    data = None
    
    if data_path is not None:
        # try to open the file as json
        with open(data_path, 'r') as file:
            data = json.load(file)
    return data



@app.route('/', methods=['GET', 'POST', 'PUT'])
def welcome():
  resp = twilio.twiml.Response()
  resp.say("Welcome to Twilio")
  return str(resp)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)

import os, sys, requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verification.token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello World", 200

if __name__ == "__main__" :
   # IP
    response = requests.get('https://httpbin.org/ip')
    print('Your IP is {0}'.format(response.json()['origin']))
    app.run(debug = True, port = 80)
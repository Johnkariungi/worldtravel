import os, sys, requests
from flask import Flask, request
from utils import wit_response
from pymessenger.bot import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAADHBIbZCiLYBAE0HqEsFft7WtKE513RyuK5NKD2ip62BgoI2bZBr19xoHCvmvFSGrFZBgmGAVNDNZBUbgelEg8d0l82furg9V3xDmL9LRZAJtfyviBJLU756T4uSKfb4B9WhtTxGg4WdFOHZA1sQ1ZAFgJwGVo8jzO0ssjVSb24AZDZD"

bot = Bot(PAGE_ACCESS_TOKEN)

# @app.route('/', methods=['GET'])
# @app.route('/<path:path>')
# def verify():
#     # Webhook verification
#     if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
#         if not request.args.get("hub.verify_token") == "hello":
#             return "Verification token mismatch", 403
#         return request.args["hub.challenge"], 200
#     return "Hello World", 200


@app.route('/', methods=['POST'])
def Webhook():
    print("Got to post!")
    data = request.get_json()
    log(data)
    print(data)
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

				# IDs
                    sender_id = messaging_event['sender']['id']
                    recipient_id = messaging_event['recipient']['id']

                    if messaging_event.get('message'):
                        # Extracting text message
                        if 'text' in messaging_event['message']:
                            messaging_text = messaging_event['message']['text']
                        else:
                            messaging_text = 'no text'

                        # Echo
                        #response = messaging_text
                        response = None

                        entity, value = wit_response(messaging_text)

                        if entity == "places":
                            response = "Ok, I will send you {} cool places.".format(str(value))
                        elif entity == "recreation":
                            response = "Ok, so you would like to recreation to {0}, I will send you cool places from {0}".format(str(value))
                        elif entity == "eat":
                            response = "Ok, so you would like to eat to {0}, I will send you cool places from {0}".format(str(value))
                        elif entity == "walk":
                            response = "Ok, so you would like to walk to {0}, I will send you cool places from {0}".format(str(value))
                        elif entity == "shop":
                            response = "Ok, so you would like to shop to {0}, I will send you cool places from {0}".format(str(value))
                        elif entity == "hike":
                            response = "Ok, so you would like to hike to {0}, I will send you cool places from {0}".format(str(value))
                        elif entity == "entertainment":
                            response = "Ok, so you would like to entertainment to {0}, I will send you cool places from {0}".format(str(value))
                        elif entity == "location":
                            response = "Ok, so you would like to travel to {0}, I will send you cool places from {0}".format(str(value))
                        if response == None:
                            response = "Please try again, thank you!"

                        bot.send_text_message(sender_id, response)

            return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()
    

if __name__ == "__main__" :
   # IP
    #response = requests.get('https://httpbin.org/ip')
    #print('Your IP is {0}'.format(response.json()['origin']))
    #app.run(debug = True, port = 80)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

from wit import Wit

access_token = "7VQGABSTV4CNR77DPDLH2FVSIK7ZMTOY"

client = Wit(access_token = access_token)
#message_text = "I like cool places"

def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    value = None

    try:
        entity = list(resp['entities'])[0]
        value = resp['entities']['entity'][0]['value']
    except Exception as e:
        print(e)
    return (entity, value)
#print(resp)
print(wit_response('I like cool places'))
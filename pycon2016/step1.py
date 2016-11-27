from wit import Wit

def send(request, response):
    print('Bot responde: {}'.format(response['text']))

actions = {
    'send': send,
}

ACCESS_TOKEN = 'BYP2LLV64PDAUH2KPNRHN2T7ICZUGDHV' 
client = Wit(access_token=ACCESS_TOKEN, actions=actions)
client.interactive()

from wit import Wit
from utils import first_entity_value 

def send(request, response):
    print(response['text'])

def get_beer_type(request):
    context = request['context']
    entities = request['entities']

    beer_type = first_entity_value(entities, 'tipo_birra')
    if beer_type:
        context['tipo_birra'] = beer_type 

    return context

actions = {
    'send': send,
    'get_beer_type': get_beer_type,
}

ACCESS_TOKEN = 'BYP2LLV64PDAUH2KPNRHN2T7ICZUGDHV' 
client = Wit(access_token=ACCESS_TOKEN, actions=actions)
client.interactive()

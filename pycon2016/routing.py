from channels.routing import route


channel_routing = [
    route('websocket.receive', 'pyconar.consumers.ws_bot'),
]


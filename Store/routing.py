from channels.routing import ProtocolTypeRouter

#from home.consumers import ws_connect, ws_disconnect

application = ProtocolTypeRouter({

})

# channel_routing = [
#     route('websocket.connect', ws_connect),
#     route('websocket.disconnect', ws_disconnect),
# ]
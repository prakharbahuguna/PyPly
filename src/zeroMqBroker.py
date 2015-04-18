__author__ = 'matt'

import zmq
import json


class ZeroMQBroker:
    def __init__(self, jukebox, server, port):
        # Socket to talk to server
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect('tcp://{}:{}'.format(server, port))
        self.jukebox = jukebox

    def messageListener(self, partyID):
        self.socket.setsockopt(zmq.SUBSCRIBE, partyID)

        while True:
            message = self.socket.recv_string()
            message_parts = message.split()
            topic = message_parts[0]
            verb = message_parts[1]
            argument = None

            if len(message_parts) > 2:
                argument = message_parts[2]

            if verb == 'loadPlaylist':
                self.jukebox.setPlaylist(json.loads(message_parts[2]))
            elif verb == 'quit':
                self.jukebox.running = False
                return

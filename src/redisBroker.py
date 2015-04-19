__author__ = 'matt'

import json
from redis import Redis

class ZeroMQBroker:
    def __init__(self):
        # Socket to talk to server
        self.redisClient = Redis(host="redis92559-pyply.j.layershift.co.uk", password="O3KcaI9RRj")
        #self.jukebox = jukebox

    def messageListener(self, partyID):
        while True:
            message = self.redisClient.blpop("party")
            message_parts = message[1].split()
            topic = message[0]
            verb = message_parts[0]
            argument = message_parts[1]

            if len(message_parts) > 2:
                argument = message_parts[2]

            if verb == 'loadPlaylist':
                self.jukebox.setPlaylist(json.loads(message_parts[2]))
            if verb == 'skipVote':
                self.jukebox.addSkipVote()
            if verb == 'pause':
                self.jukebox.pausePlayer()
            elif verb == 'quit':
                self.jukebox.running = False
                return

if __name__ == '__main__':
    underTest = ZeroMQBroker()
    underTest.messageListener(1234)
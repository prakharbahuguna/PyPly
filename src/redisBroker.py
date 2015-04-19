import json
from redis import Redis

class RedisBroker:
    def __init__(self, jukebox):
        # Socket to talk to server
        self.redisClient = Redis(host="redis92559-pyply.j.layershift.co.uk", password="O3KcaI9RRj")
        self.jukebox = jukebox

    def messageListener(self, partyID):
        while True:
            message = self.redisClient.blpop("party")
            message_parts = message[1].split()
            topic = message[0]
            verb = message_parts[0]
            argument = ""
            if len(message_parts) > 1:
                argument = message_parts[1]
                print argument

            if verb == 'loadPlaylist' and argument:
                self.jukebox.setPlaylist(json.loads(argument))
            if verb == 'skipVote':
                self.jukebox.addSkipVote()
            if verb == 'togglePause':
                self.jukebox.togglePausePlayer()

if __name__ == '__main__':
    underTest = RedisBroker()
    underTest.messageListener("party")
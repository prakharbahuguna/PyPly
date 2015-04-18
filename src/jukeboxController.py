__author__ = 'matt'

import threading
import spotify_wrapper
import urllib2
from zeroMqBroker import ZeroMQBroker
from time import sleep
from collections import deque
from sys import stdin

SERVER = 'pyply.j.layershift.co.uk'
PORT = '5556'


class JukeboxController:
    def __init__(self):
        self.playlist = None
        self.running = False

    def setPlaylist(self, pl):
        self.playlist = deque(pl)

    def spotifyController(self):
        while self.running:
            if self.playlist:
                status = spotify_wrapper.player_state()
                if status == 'paused' or status == 'stopped':
                    nexttrack = self.playlist.popleft()
                    self.playlist.append(nexttrack)
                    spotify_wrapper.play_track(nexttrack)
                    print('Now playing ' + nexttrack)
            sleep(1)

        spotify_wrapper.play_pause()


if __name__ == "__main__":
    print('Enter Party ID:')
    partyId = stdin.readline()[:-1]
    print('Enter Spotify Playlist URI:')
    plist = stdin.readline()[:-1]

    jukebox = JukeboxController()
    jukebox.running = True
    jukeThread = threading.Thread(name='SpotifyController', target=jukebox.spotifyController)

    mqBroker = ZeroMQBroker(jukebox, SERVER, PORT)
    brokerThread = threading.Thread(name='MessageListener', target=mqBroker.messageListener, args=(partyId,))

    urllib2.urlopen('http://{}/setup/{}/{}'.format(SERVER, partyId, plist))

    jukeThread.start()
    brokerThread.start()
    jukeThread.join()

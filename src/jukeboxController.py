__author__ = 'matt'

import threading
import spotify_wrapper
from redisBroker import RedisBroker
from time import sleep
from collections import deque
import requests
from sys import stdin

SERVER = 'pyply.j.layershift.co.uk'
SKIP_THRESHOLD = 3


class JukeboxController:
    def __init__(self):
        self.playlist = None
        self.currentSkipCount = 0

    def addSkipVote(self):
        self.currentSkipCount += 1
        if self.currentSkipCount >= SKIP_THRESHOLD:
            self.goNextTrack()

    def pausePlayer(self):
        if spotify_wrapper.player_state() == 'playing':
            spotify_wrapper.play_pause()

    def goNextTrack(self):
        self.currentSkipCount = 0
        nextTrack = self.playlist.popleft()
        self.playlist.append(nextTrack)
        spotify_wrapper.play_track(nextTrack)
        print('Now playing ' + nextTrack)

    def setPlaylist(self, pl):
        self.playlist = deque(pl)

    def spotifyController(self):
        while True:
            if self.playlist:
                status = spotify_wrapper.player_state()
                if status == 'stopped':
                    self.goNextTrack()
            sleep(1)


if __name__ == "__main__":
    #print('Enter Party ID:')
    #partyId = stdin.readline()[:-1]

    print "Using Party ID 1234"
    partyId = "1234"

    jukebox = JukeboxController()
    jukeThread = threading.Thread(name='SpotifyController', target=jukebox.spotifyController)

    redisBroker = RedisBroker()
    brokerThread = threading.Thread(name='MessageListener', target=redisBroker.messageListener, args=(partyId,))

    #r = requests.get('http://{}/party/{}'.format(SERVER, partyId))
    #if r.status_code == 200 and r.json()['success'] and r.json()['playlist_prompt']:
        #print('Enter Spotify playlist URI:')
        #plist = stdin.readline()[:-1]
        #r = requests.get('http://{}/playlist/{}/{}'.format(SERVER, partyId, plist))

    jukeThread.start()
    brokerThread.start()
    jukeThread.join()

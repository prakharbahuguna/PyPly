__author__ = 'matt'

import threading
import spotify_wrapper
from zeroMqBroker import ZeroMQBroker
from time import sleep
from collections import deque


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
                    print "Now playing " + nexttrack
            sleep(1)

        spotify_wrapper.play_pause()


if __name__ == "__main__":
    jukebox = JukeboxController()
    jukebox.running = True
    jukeThread = threading.Thread(name='SpotifyController', target=jukebox.spotifyController)

    mqBroker = ZeroMQBroker(jukebox)
    brokerThread = threading.Thread(name='MessageListener', target=mqBroker.messageListener, args=('house1',))

    jukeThread.start()
    brokerThread.start()
    jukeThread.join()

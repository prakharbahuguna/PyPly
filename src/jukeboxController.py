__author__ = 'matt'

import thread
import spotify_wrapper
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
            status = spotify_wrapper.player_state()
            print status
            
            if not self.playlist:
                print "Empty playlist - get some tunes sent in!"
            elif status == 'paused' or status == 'stopped':
                nextTrack = self.playlist.popleft()
                self.playlist.append(nextTrack)
                spotify_wrapper.play_track(nextTrack)
                print "Now playing " + nextTrack
            sleep(1)

        spotify_wrapper.play_pause()


if __name__ == "__main__":
    jukebox = JukeboxController
    jukebox.running = True
    thread.start_new_thread(jukebox.spotifyController, ())

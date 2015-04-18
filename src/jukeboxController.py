__author__ = 'matt'

import thread
import spotify_wrapper
from time import sleep

class JukeboxController:

    def __init__(self):
        self.playlist = []

    def setPlaylist(self, pl):
        self.playlist = pl

    def spotifyController(self):
        while True:
            status = spotify_wrapper.player_state()
            print status
            
            if not self.playlist:
                print "Empty playlist - get some tunes sent in!"
            elif status == "stopped":
                nextTrack = self.playlist.pop(0)
                spotify_wrapper.play_track(nextTrack)
                print "Now playing " + nextTrack

                self.addToBackOfQueue(nextTrack)
            sleep(1)

    def addToBackOfQueue(self, nextTrack):
        # Need to remove it from playlist and re-add at the end
        return

if __name__ == "__main__":
    jukebox = JukeboxController
    thread.start_new_thread(jukebox.spotifyController)
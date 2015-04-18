import unittest
import sys
import threading
from time import sleep

sys.path.append('../src/')
import spotify_wrapper
from jukeboxController import JukeboxController

__author__ = 'prakhar'
test_plist = ['spotify:track:5eZaT21ZVGyGHJ8kcwaNxA', 'spotify:track:3agtg0x11wPvLIWkYR39nZ',
              'spotify:track:6Sy9BUbgFse0n0LPA5lwy5']


class JukeboxControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.jukebox = JukeboxController()
        self.t = threading.Thread(target=self.jukebox.spotifyController)

    def test_set_playlist(self):
        self.jukebox.running = False
        self.jukebox.setPlaylist(test_plist)
        self.assertEqual(self.jukebox.playlist[0], test_plist[0])

    def test_playback(self):
        self.jukebox.running = False
        self.assertEqual('paused', spotify_wrapper.player_state())

        self.jukebox.setPlaylist(test_plist)
        self.jukebox.running = True
        self.t.start()
        sleep(5)

        self.assertEqual('playing', spotify_wrapper.player_state())
        self.assertEqual(test_plist[0], spotify_wrapper.track_id())
        self.assertEqual(test_plist[1], self.jukebox.playlist[0])

        self.jukebox.setPlaylist(test_plist[2:])
        self.assertEqual(test_plist[0], spotify_wrapper.track_id())
        spotify_wrapper.skip_track()
        sleep(5)
        self.assertEqual(test_plist[2], spotify_wrapper.track_id())

    def tearDown(self):
        self.jukebox.running = False

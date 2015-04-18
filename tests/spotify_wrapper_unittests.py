import unittest
import sys

sys.path.append('../src/')
import spotify_wrapper

__author__ = 'prakhar'
test_id = 'spotify:track:546QTayX6j4GcZsfTRrVnL'
test_name = 'Remember The Name (feat. Styles Of Beyond)'
test_artist = 'Fort Minor'


class SpotifyWrapperTestCase(unittest.TestCase):
    def setUp(self):
        spotify_wrapper.play_track(test_id)

    def test_track_id(self):
        self.assertEqual(test_id, spotify_wrapper.track_id())

    def test_track_name(self):
        self.assertEqual(test_name, spotify_wrapper.track_name())

    def test_track_artist(self):
        self.assertEqual(test_artist, spotify_wrapper.track_artist())

    def test_player_state(self):
        self.assertEqual('playing', spotify_wrapper.player_state())
        spotify_wrapper.play_pause()
        self.assertEqual('paused', spotify_wrapper.player_state())


if __name__ == '__main__':
    unittest.main()
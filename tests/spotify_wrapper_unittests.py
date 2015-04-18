import unittest, sys
sys.path.append('../src/')
import spotify_wrapper

__author__ = 'prakhar'
test_id = 'spotify:track:546QTayX6j4GcZsfTRrVnL'
test_name = 'Remember The Name (feat. Styles Of Beyond)'
test_artist = 'Fort Minor'


class SpotifyWrapperTestCase(unittest.TestCase):
    def setUp(self):
        spotify_wrapper.play_track(test_id)

    def tearDown(self):
        spotify_wrapper.play_pause()


    def test_track_id(self):
        self.assertEqual(spotify_wrapper.track_id(), test_id)


    def test_track_name(self):
        self.assertEqual(spotify_wrapper.track_name(), test_name)


    def test_track_artist(self):
        self.assertEqual(spotify_wrapper.track_artist(), test_artist)


if __name__ == '__main__':
    unittest.main()
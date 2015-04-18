__author__ = 'matt'

import unittest
from client import unmarshalSpotifyURIsFromJSON
import json

class ClientUnittests(unittest.TestCase):

    def test_unmarshal_spotify_uris_from_json(self):
        jsonarray = json.dumps(["uri1", "uri2", "uri3", "uri4"])
        spotifyURIs = unmarshalSpotifyURIsFromJSON(jsonarray)
        self.assertEqual(spotifyURIs, json.loads(jsonarray))

if __name__ == '__main__':
    unittest.main()
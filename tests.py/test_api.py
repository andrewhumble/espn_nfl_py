import unittest
from espn_nfl_api import ESPNAPI, APIError

class TestESPNAPI(unittest.TestCase):

    def setUp(self):
        self.api = ESPNAPI()

    def test_get_probabilities(self):
        # Replace 'event_id' with a valid event ID for testing
        event_id = '401220403'
        response = self.api.get_probabilities(event_id)
        self.assertIsNotNone(response)

    # Add more tests for other endpoints

if __name__ == '__main__':
    unittest.main()
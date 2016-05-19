import unittest
import matterweb


class MatterWebTestCase(unittest.TestCase):

    def setUp(self):
        self.url = "http://team.oz4cs.com/hooks/itpz3ynsjbbttgycj75g1nerec"

    def test_simple_notify(self):
        self.assertTrue(matterweb.notify(self.url, text="message!"))

if __name__ == '__main__':
    unittest.main()

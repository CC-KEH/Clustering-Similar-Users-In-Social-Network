import unittest
from webapp.app import app

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'User Activity Clustering', result.data)

if __name__ == "__main__":
    unittest.main()

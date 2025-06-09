import unittest
from sports_predictor.app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sports Prediction', response.data)

    def test_prediction(self):
        data = {'sport': 'Soccer', 'team1': 'A', 'team2': 'B'}
        response = self.client.post('/predict', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Predicted winner', response.data)

if __name__ == '__main__':
    unittest.main()

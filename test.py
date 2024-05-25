import unittest

from convert import  app
from unittest.mock import patch



class CurrencyConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    @patch('requests.get')
    def test_currency_conversion(self, mock_get):

        mock_response_data = {
            'rates': {
                'USD': 1.0,
                'EUR': 0.85
            }
        }
        mock_get.return_value.json.return_value = mock_response_data

        result = self.app.post('/convert', data={
            'amount': '100',
            'from_currency': 'USD',
            'to_currency': 'EUR'
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn('100.0 USD равно 85.0 EUR', result.get_data(as_text=True))
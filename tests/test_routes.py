import unittest
from flask import url_for
from api_routes import app

class FlaskTestCase(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_data(self):
        response = self.client.get('/')
        response_data = eval(response.data)
        self.assertEquals(response_data['message'], "Hello, world!")

# if __name__ == "__main__":
#     unittest.main()
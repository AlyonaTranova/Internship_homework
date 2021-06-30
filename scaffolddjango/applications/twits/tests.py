import unittest
from rest_framework.test import APIClient
import django
django.setup()


class MyTestCase(unittest.TestCase):
    def test_1(self):
        client = APIClient()
        response = client.get('/api/twits/film/', format='json')
        self.assertEqual(200, response.status_code)

    def test_2(self):
        client = APIClient()
        client.login(username='ad', password='ad')


if __name__ == '__main__':
    unittest.main()

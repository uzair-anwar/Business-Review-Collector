import unittest
from django.test import Client


class BusinessEndpointTests(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_valid_request(self):
        response = self.client.get(
            '/business/https%3A%2F%2Fwww.lendingtree.com%2Freviews%2Fbusiness%2Fondeck%2F51886298%2F')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response content and structure

    def test_invalid_url(self):
        response = self.client.get('/business/invalid_url')
        self.assertEqual(response.status_code, 301)
        # Add assertions to check the error message

    def test_method_not_allowed(self):
        response = self.client.post(
            '/business/https%3A%2F%2Fwww.lendingtree.com%2Freviews%2Fbusiness%2Fondeck%2F51886298%2F')
        self.assertEqual(response.status_code, 405)
        # Add assertions to check the response content

    def test_error_handling(self):
        response = self.client.get(
            '/business/https%3A%2F%2Fwww.nonexistenturl.com')
        self.assertEqual(response.status_code, 301)
        # Add assertions to check the error message


if __name__ == '__main__':
    unittest.main()

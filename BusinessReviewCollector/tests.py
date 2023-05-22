from django.test import TestCase, Client
from django.urls import reverse
import urllib.parse


class BusinessEndpointTests(TestCase):
    def setUp(self):
        self.client = Client()

    import urllib.parse

    def test_valid_request(self):
        business_name = "ondeck/51886298"
        encoded_business_name = urllib.parse.quote(business_name)
        url = reverse('business', args=[encoded_business_name])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], business_name)
        self.assertIn('reviews', response.json())

    def test_invalid_url(self):
        invalid_business_name = "invalid_example"
        url = reverse('business', args=[invalid_business_name])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 500)

    def test_error_handling(self):
        business_name = "error_example"
        url = reverse('business', args=[business_name])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 500)
        self.assertIn('An error occurred', response.content.decode())

    def test_post_request(self):
        url = reverse('business', args=['example'])
        response = self.client.post(url, {'data': 'sample data'})

        self.assertEqual(response.status_code, 405)

from django.test import TestCase, Client
from django.urls import reverse
from map.models import Excavations

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.excavation = Excavations.objects.create(
            INSPIRE_ID="12345",
            FUNKCJA="test function",
            CHRONOLOGIA="test chronology",
            MIEJSCOWOSC="test location",
            LINK="https://example.com"
        )

    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_view(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_excavation_data_valid_id(self):
        url = reverse('get_excavation_data', args=[self.excavation.INSPIRE_ID])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                'Funkcja': 'Test function',
                'Chronologia': 'Test chronology',
                'Miejscowość': 'Test Location',
                'Link': 'https://example.com'
            }
        )

    def test_get_excavation_data_invalid_id(self):
        url = reverse('get_excavation_data', args=["invalid_id"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'error': 'Excavation not found'}
        )

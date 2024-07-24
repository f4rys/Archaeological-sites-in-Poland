from django.test import SimpleTestCase
from django.urls import reverse, resolve
from map import views

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, views.about)

    def test_get_excavation_data_url_resolves(self):
        url = reverse('get_excavation_data', args=['12345'])
        self.assertEqual(resolve(url).func, views.get_excavation_data)
        self.assertEqual(resolve(url).kwargs['inspire_id'], '12345')

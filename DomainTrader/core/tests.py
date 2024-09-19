from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class IndexTest(TestCase):
  def teste_status(self):
    self.resp = self.client.get('/')
    self.assertEqual(self.resp.status_code, 200)
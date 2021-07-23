from django.test import TestCase
from .models import *
from django.test import TestCase

# Create your tests here.
class GymTestCase(TestCase):
    def test_Enquiry(self):
        poll_1 = Enquiry.objects.create(name="bhuban",contact="99999999",emailid="test@gmail.com",age="23",gender='male')
    

        resp = self.client.get('/add_enquiry/')
        print(resp)

        self.assertEqual(resp.status_code, 200)
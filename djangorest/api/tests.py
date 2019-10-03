from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from .models import Bucketlist
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model"""

    def setUp(self):
        """Define the test client and other variables"""
        self.bucketlist_name = "Act in a play"
        self.bucketlist = Bucketlist(name = self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        """Test that the model can create a bucketlist"""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views"""

    def setUp(self):
        """Define the test client and other variables"""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Iceland'}
        self.response = self.client.post(reverse('create'), self.bucketlist_data, format="json")

    def test_api_can_create_a_bucketlist(self):
        """Test the api can create a bucketlist"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a bucketlist"""
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(reverse('details', kwargs={'pk':bucketlist.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_a_bucketlist(self):
        """Test the api can update a bucketlist"""
        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name': 'Something New'}
        res = self.client.put(reverse('details', kwargs={'pk':bucketlist.id}), change_bucketlist, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_bucketlist(self):
        """Test the api can delete a bucketlist"""
        bucketlist = Bucketlist.objects.get()
        res = self.client.delete(reverse('details', kwargs={'pk':bucketlist.id}), follow=True)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

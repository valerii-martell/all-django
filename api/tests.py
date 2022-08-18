import unittest

from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from mock import patch
from rest_framework import status
from rest_framework.test import APIClient

from graphql_api.models import Model, Make
from .serializers import ModelSerializer, MakeSerializer

MODEL_URL = reverse('rest_api:model-list')
MAKE_URL = reverse('rest_api:make-list')


class PublicApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(MODEL_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED) # HTTP_403_FORBIDDEN


class PrivateApiTestsAbstract:
    model = None
    client = None
    URL = None
    serializer = None

    @patch('api.views.send_email')
    @unittest.skip
    def test_retrieve(self, mock_email):
        self.model.objects.create(name='Test name')
        self.model.objects.create(name='Test name 2')

        res = self.client.get(self.URL)

        instances = self.model.objects.all().order_by('-name')
        serializer = self.serializer(instances, many=True)

        if self.model is Model:
            mock_email.assert_called_once()
            mock_email.assert_called_with('my value 1')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_successful(self):
        payload = {'name': 'test name'}
        self.client.post(self.URL, payload)

        exists = self.model.objects.filter(
            name=payload['name']).exists()
        self.assertTrue(exists)

    def test_create_invalid(self):
        payload = {'name': ''}
        res = self.client.post(self.URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_list(self):
        payload = {'name': []}
        res = self.client.post(self.URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


class PrivateModelApiTests(TestCase, PrivateApiTestsAbstract):
    def setUp(self):
        self.user = get_user_model().objects.create_user('test@gmail.com',
                                                         'password123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.model = Model
        self.serializer = ModelSerializer
        self.URL = MODEL_URL


class PrivateMakeApiTests(TestCase, PrivateApiTestsAbstract):

    def setUp(self):
        self.user = get_user_model().objects.create_user('test@gmail.com',
                                                         'password123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.model = Make
        self.serializer = MakeSerializer
        self.URL = MAKE_URL
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
import json

from django.core.urlresolvers import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class ApplicationListViewSetTestCase(APITestCase):
    def setUp(self):
        mommy.make('ApplicationModel', _quantity=2)

    def test_list(self):
        client = APIClient()
        url = reverse('test_api_list')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(len(data), 2)

    def test_create(self):
        client = APIClient()
        url = reverse('test_api_list')
        data = {
            'name': 'test_name',
            'key': 'test_key',
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = json.loads(response.content)
        self.assertEqual(data['name'], 'test_name')
        self.assertEqual(data['key'], '')


class ApplicationItemViewSetTestCase(APITestCase):
    def setUp(self):
        mommy.make('ApplicationModel', _quantity=2)

    def test_get(self):
        client = APIClient()
        test_app = mommy.make('ApplicationModel', name='test1', key='test_key')
        url = reverse('test_api_item', kwargs={'pk': test_app.pk})
        url = url + '?key=' + test_app.key
        response = client.get(url, )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(data['name'], 'test1')

    def test_get_not_permitted(self):
        client = APIClient()
        test_app = mommy.make('ApplicationModel', name='test1')
        url = reverse('test_api_item', kwargs={'pk': test_app.pk})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update(self):
        client = APIClient()
        test_app = mommy.make('ApplicationModel', name='test1')
        url = reverse('test_api_item', kwargs={'pk': test_app.pk})
        data = {'name': 'test2'}
        response = client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(data['name'], 'test2')

    def test_add_api_key(self):
        client = APIClient()
        test_app = mommy.make('ApplicationModel', name='test1', key='test_key')
        url = reverse('test_api_update_key', kwargs={'pk': test_app.pk})
        response = client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(data['key'], hashlib.md5('test1').hexdigest())

    def test_delete(self):
        client = APIClient()
        test_app = mommy.make('ApplicationModel', name='test1')
        url = reverse('test_api_item', kwargs={'pk': test_app.pk})
        response = client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        url = reverse('test_api_list')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(len(data), 2)

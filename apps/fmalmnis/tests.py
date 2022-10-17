from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.core import models
from apps.fmalmnis import utils


class ParserTests(APITestCase):
    # def test_timetable_creation(self):
    #     url = reverse('download')

    #     response = self.client.post(url)

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertIsNotNone(models.Timetable.objects.all())
    #     self.assertIsNotNone(response.json()['id'])

    def test_sending(self):
        data = utils.load_main_db()
        print(data)

from rest_framework.views import APIView
from .constants import SCHOOL_NAME
from .constants import CITY_NAME
from apps.core import models
from . import utils


class DownloadView(APIView):
    city: models.City = models.City.objects.get_or_create(name=CITY_NAME)[0]
    school: models.School = models.School.objects.get_or_create(
        name=SCHOOL_NAME, city=city)[0]

    def post(self, request, format=None):
        timetable = models.Timetable.objects.create(school=self.school)


class Timetable(APIView):
    def post(self, request, format=None):
        pass

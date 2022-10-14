from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core import models, serializers

from . import utils
from .constants import CITY_NAME, SCHOOL_NAME


class DownloadView(APIView):
    city: models.City = models.City.objects.get_or_create(name=CITY_NAME)[0]
    school: models.School = models.School.objects.get_or_create(
        name=SCHOOL_NAME, city=city)[0]

    def post(self, request, format=None):
        timetable = models.Timetable.objects.create(school=self.school)
        utils.load_main_db(timetable)
        serializer = serializers.TimetableSerializer(instance=timetable)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class Timetable(APIView):
    def post(self, request, format=None):
        pass

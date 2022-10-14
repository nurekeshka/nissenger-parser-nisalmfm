from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core import models, serializers

from . import utils
from .constants import CITY_NAME, SCHOOL_NAME


class DownloadView(APIView):
    city: models.City = models.City.objects.get(name=CITY_NAME)
    school: models.School = models.School.objects.get(
        name=SCHOOL_NAME, city=city)

    def post(self, request, format=None):
        timetable = models.Timetable.objects.create(school=self.school)
        utils.load_main_db(timetable)
        serializer = serializers.TimetableSerializer(instance=timetable)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class Timetable(APIView):
    def post(self, request, format=None):
        pass

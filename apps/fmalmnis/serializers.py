from rest_framework import serializers
from . import models


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ('name',)


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = ('name', 'city')


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Timetable
        fields = ('creation_datetime', 'school')


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Day
        fields = ('name',)


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Class
        fields = ('grade', 'letter', 'timetable')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ('name', 'classes', 'timetable')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('name', 'timetable')


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Period
        fields = ('number', 'starttime', 'endtime', 'timetable')


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classroom
        fields = ('name', 'timetable')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('name', 'timetable')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ('subject', 'classroom', 'teacher',
                  'period', 'group', 'day', 'timetable')

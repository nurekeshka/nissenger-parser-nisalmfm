from django.contrib import admin
from . import models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    fields = ('name', 'city')


@admin.register(models.Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('creation_datetime',)


@admin.register(models.Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('grade', 'letter', 'timetable')
    fields = ('grade', 'letter', 'timetable')


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'timetable')
    fields = ('name', 'classes', 'timetable')


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'timetable')
    fields = ('name', 'timetable')


@admin.register(models.Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('number', 'starttime', 'endtime', 'timetable')
    fields = ('number', ('starttime', 'endtime', 'timetable'))


@admin.register(models.Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'timetable')
    fields = ('name', 'timetable')


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'timetable')
    fields = ('name', 'timetable')


@admin.register(models.Lesson)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'classroom', 'teacher',
                    'period', 'group', 'day', 'timetable')
    fields = ('subject', 'classroom', 'teacher',
              'period', 'group', 'day', 'timetable')

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


@admin.register(models.Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('grade', 'letter', 'school')
    fields = ('grade', 'letter', 'school')


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    fields = ('name', 'classes', 'school')


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    fields = ('name', 'school')


@admin.register(models.Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('number', 'starttime', 'endtime', 'school')
    fields = ('number', ('starttime', 'endtime', 'school'))


@admin.register(models.Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    fields = ('name', 'school')


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    fields = ('name', 'school')


@admin.register(models.Lesson)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'classroom', 'teacher',
                    'period', 'group', 'day', 'school')
    fields = ('subject', 'classroom', 'teacher',
              'period', 'group', 'day', 'school')

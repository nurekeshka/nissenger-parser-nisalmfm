from datetime import datetime, time
from typing import Set

from django.db import models


class City(models.Model):
    name: str = models.CharField(max_length=255, verbose_name='name')

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class School(models.Model):
    name: str = models.CharField(max_length=255, verbose_name='name')
    city: City = models.ForeignKey(
        City, on_delete=models.CASCADE, verbose_name='city')

    class Meta:
        verbose_name = 'school'
        verbose_name_plural = 'schools'

    def __str__(self):
        return self.name


class Timetable(models.Model):
    creation_datetime: datetime = models.DateTimeField(auto_now_add=True)

    school: School = models.ForeignKey(
        School, on_delete=models.CASCADE, verbose_name='school')

    class Meta:
        verbose_name = 'timetable'
        verbose_name_plural = 'schools'

    def __str__(self):
        return self.creation_datetime.strftime('%Y-%m-%d %H:%M:%S')


class Day(models.Model):
    name: str = models.CharField(max_length=25, verbose_name='name')

    class Meta:
        verbose_name = 'day'
        verbose_name_plural = 'days'

    def __str__(self):
        return self.name


class Class(models.Model):
    class Grades(models.IntegerChoices):
        seven = (7, 'seven')
        eight = (8, 'eight')
        nine = (9, 'nine')
        ten = (10, 'ten')
        eleven = (11, 'eleven')
        twelve = (12, 'twelve')

    grade: int = models.IntegerField(choices=Grades.choices)
    letter: str = models.CharField(max_length=1)

    timetable = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, verbose_name='timetable')

    class Meta:
        verbose_name = 'class'
        verbose_name_plural = 'classes'

    def __str__(self):
        return f'{self.grade}{self.letter}'


class Group(models.Model):
    name: str = models.CharField(max_length=25, verbose_name='name')
    classes: Set[Class] = models.ManyToManyField(Class, verbose_name='classes')

    timetable = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, verbose_name='timetable')

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return f'{self.name}: {list(map(str, self.classes.all()))}'


class Teacher(models.Model):
    name: str = models.CharField(max_length=50, verbose_name='name')

    timetable = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, verbose_name='timetable')

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'

    def __str__(self):
        return self.name


class Period(models.Model):
    starttime: time = models.TimeField(verbose_name='starttime')
    endtime: time = models.TimeField(verbose_name='endtime')
    number: int = models.IntegerField(verbose_name='number')

    timetable = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, verbose_name='timetable')

    class Meta:
        verbose_name = 'period'
        verbose_name_plural = 'periods'

    def __str__(self):
        return ' - '.join((self.starttime.strftime('%H:%M'), self.endtime.strftime('%H:%M')))

    def __int__(self):
        return self.number


class Classroom(models.Model):
    name: str = models.CharField(max_length=50, verbose_name='name')
    timetable = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, verbose_name='timetable')

    class Meta:
        verbose_name = 'classroom'
        verbose_name_plural = 'classrooms'

    def __str__(self):
        return self.name


class Subject(models.Model):
    name: str = models.CharField(max_length=50, verbose_name='name')
    timetable = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, verbose_name='timetable')

    class Meta:
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject: Subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name='subject')
    classroom: Classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, verbose_name='classroom')
    teacher: Teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name='teacher')
    period: Period = models.ForeignKey(
        Period, on_delete=models.CASCADE, verbose_name='period')
    group: Group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='group')
    day: Day = models.ForeignKey(
        Day, on_delete=models.CASCADE, verbose_name='day')

    timetable = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, verbose_name='timetable')

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'

    def __str__(self):
        return self.subject.name

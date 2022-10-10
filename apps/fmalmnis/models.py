from datetime import time
from django.db import models
from typing import List
from typing import Set


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


class Day(models.Model):
    name: str = models.CharField(max_length=25, verbose_name='name')

    class Meta:
        verbose_name = 'day'
        verbose_name_plural = 'days'

    def __str__(self):
        return self.name


class Class(models.Model):
    grade_choice = (7, 8, 9, 10, 11, 12)

    grade: int = models.IntegerChoices(grade_choice)
    letter: str = models.CharField(max_length=1)

    school: School = models.ForeignKey(
        School, on_delete=models.CASCADE, verbose_name='school')

    class Meta:
        verbose_name = 'class'
        verbose_name_plural = 'classes'

    def __str__(self):
        return f'{self.grade}{self.letter}'


class Group(models.Model):
    name: str = models.CharField(max_length=25, verbose_name='name')
    classes: Set[Class] = models.ManyToManyField(Class, verbose_name='classes')

    school: School = models.ForeignKey(
        School, on_delete=models.CASCADE, verbose_name='school')

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return f'{self.name}: {list(map(str, self.classes.all()))}'


class Teacher(models.Model):
    name: str = models.CharField(max_length=50, verbose_name='name')
    school: School = models.ForeignKey(
        School, on_delete=models.CASCADE, verbose_name='school')

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'

    def __str__(self):
        return self.name


class Period(models.Model):
    starttime: time = models.TimeField(verbose_name='starttime')
    endtime: time = models.TimeField(verbose_name='endtime')
    number: int = models.IntegerField(verbose_name='number')

    school: School = models.ForeignKey(
        School, on_delete=models.CASCADE, verbose_name='school')

    class Meta:
        verbose_name = 'period'
        verbose_name_plural = 'periods'

    def __str__(self):
        return ' - '.join((self.starttime.strftime('%H:%M'), self.endtime.strftime('%H:%M')))

    def __int__(self):
        return self.number


class Classroom(models.Model):
    name: str = models.CharField(max_length=50, verbose_name='name')
    school: School = models.ForeignKey(
        School, on_delete=models.CASCADE, verbose_name='school')

    class Meta:
        verbose_name = 'classroom'
        verbose_name_plural = 'classrooms'

    def __str__(self):
        return self.name


class Subject(models.Model):
    name: str = models.CharField(max_length=50, verbose_name='name')
    school: School = models.ForeignKey(
        School, on_delete=models.CASCADE, verbose_name='school')

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
        period, on_delete=models.CASCADE, verbose_name='period')
    group: Group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='group')
    day: Day = models.ForeignKey(
        Day, on_delete=models.CASCADE, verbose_name='day')

    school: School = models.ForeignKey(
        School, on_delete=models.CASCADE, verbose_name='school')

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'

    def __str__(self):
        return self.subject.name

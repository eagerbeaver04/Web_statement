from django.db import models


class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(max_length=100)
    occupation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class Subject(models.Model):
    name = models.CharField(max_length=100)


class Group(models.Model):
    number = models.CharField(max_length=100)


class CorrSubGroup(models.Model):
    number = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)


class Student(models.Model):
    group = models.CharField(max_length=100)


class Professor(models.Model):
    subject = models.CharField(max_length=100)


class CorrProffGrop(models.Model):
    id_professor = models.IntegerField(max_length=100)
    id_group = models.IntegerField(max_length=100)


class Progress(models.Model):
    id_student = models.IntegerField(max_length=100)
    attendance = models.BooleanField(max_length=100)
    mark = models.IntegerField(max_length=100)
    date = models.CharField(max_length=100)

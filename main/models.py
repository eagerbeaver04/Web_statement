from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class Subject(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)


class Group(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    number = models.CharField(max_length=100)


class CorrSubjGroup(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    group = models.ForeignKey('Group', on_delete=models.PROTECT)
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT)


class Student(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    group = models.ForeignKey('Group', on_delete=models.PROTECT)


class Professor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT)


class CorrProffGroup(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    professor = models.ForeignKey('Professor', on_delete=models.PROTECT)
    group = models.ForeignKey('Group', on_delete=models.PROTECT)


class StudentProgress(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    attendance = models.BooleanField()
    mark = models.IntegerField()
    date = models.CharField(max_length=100)
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT)
    student = models.ForeignKey('Student', on_delete=models.PROTECT)


class Account(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user = models.OneToOneField('Person', on_delete=models.CASCADE, primary_key=True)

    def check_password(self, password1):
        if self.password == password1:
            return True
        return False



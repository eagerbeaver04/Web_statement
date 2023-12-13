from django.db import models
from django.dispatch import receiver


class User(models.Model):
    class Roles(models.TextChoices):
        STUDENT = "ST"
        PROFESSOR = "PR"

    id = models.AutoField(primary_key=True, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    middle_name = models.CharField(max_length=100, default=None)
    gender = models.CharField(max_length=10, default=None)
    age = models.IntegerField(default=None)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, default=None)
    subjects = models.ManyToManyField('Subject', related_name='professors')
    role = models.CharField(
        max_length=100,
        choices=Roles.choices,
        default=Roles.STUDENT,
    )

    def check_password(self, password):
        if self.password == password:
            return True
        return False

    def serialize(self):
        fields = User._meta.get_fields()
        return {field.name: getattr(self, field.name) for field in fields if not field.is_relation}


class Subject(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def serialize(self):
        fields = Subject._meta.get_fields()
        return {field.name: getattr(self, field.name) for field in fields if not field.is_relation}


class Group(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, related_name='groups')

    def serialize(self):
        fields = Group._meta.get_fields()
        return {field.name: getattr(self, field.name) for field in fields if not field.is_relation}


class Progress(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def serialize(self):
        fields = Progress._meta.get_fields()
        return {field.name: getattr(self, field.name) for field in fields if not field.is_relation}

#
# class Person(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     middlename = models.CharField(max_length=100)
#     gender = models.CharField(max_length=10)
#     age = models.IntegerField()
#     occupation = models.CharField(max_length=100)
#     status = models.CharField(max_length=100)
#
#     def create_dict(self):
#         fields = Person._meta.get_fields()
#         return {field.name: getattr(self, field.name) for field in fields if not field.is_relation}
#
# class Subject(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     name = models.CharField(max_length=100)
#
#
# class Group(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     number = models.CharField(max_length=100)
#
#
# class CorrSubjGroup(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     group = models.ForeignKey('Group', on_delete=models.PROTECT)
#     subject = models.ForeignKey('Subject', on_delete=models.PROTECT)
#
#
# class Student(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     group = models.ForeignKey('Group', on_delete=models.PROTECT)
#
#
# class Professor(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     subject = models.ForeignKey('Subject', on_delete=models.PROTECT)
#
#
# class CorrProffGroup(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     professor = models.ForeignKey('Professor', on_delete=models.PROTECT)
#     group = models.ForeignKey('Group', on_delete=models.PROTECT)
#
#
# class StudentProgress(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     attendance = models.BooleanField()
#     mark = models.IntegerField()
#     date = models.CharField(max_length=100)
#     subject = models.ForeignKey('Subject', on_delete=models.PROTECT)
#     student = models.ForeignKey('Student', on_delete=models.PROTECT)
#
# переделать под user
# class Account(models.Model):
#     login = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     user = models.OneToOneField('Person', on_delete=models.CASCADE, primary_key=True)
#
#     def check_password(self, password1):
#         if self.password == password1:
#             return True
#         return False
#
#

from django.db import models


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
        info = {field.name: getattr(self, field.name) for field in fields if not field.is_relation}
        info['group'] = self.group.name
        info['subjects'] = self.subjects.all()
        return info


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


class MarkCell(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateField(default=None, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def serialize(self):
        fields = MarkCell._meta.get_fields()
        return {field.name: getattr(self, field.name) for field in fields if not field.is_relation}


class Progress(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    comment = models.CharField(max_length=100, default=None)
    mark = models.CharField(max_length=100, default=None)
    attendance = models.BooleanField(default=False)
    markcell = models.ForeignKey(MarkCell, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def serialize(self):
        fields = Progress._meta.get_fields()
        return {field.name: getattr(self, field.name) for field in fields if not field.is_relation}

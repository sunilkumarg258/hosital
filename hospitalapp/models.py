from django.db import models


# Create your models here.
class Departments(models.Model):
    image = models.ImageField(upload_to='pics')
    dname = models.CharField(max_length=100)
    desc = models.TextField()


class Doctors(models.Model):
    name = models.CharField(max_length=100)
    specification = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')


class Index(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    specification = models.CharField(max_length=100)


class IndexDoctor(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    specification = models.CharField(max_length=100)


class News(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    date = models.DateField()


class Patient(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    specification = models.CharField(max_length=100)


class Popular(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')


class Appointment(models.Model):
    username = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.DateField()
    message = models.TextField()




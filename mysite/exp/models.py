from django.db import models


class student(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    major = models.CharField(max_length=30)


class researchresults(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)


class relatedresources(models.Model):
    name = models.CharField(max_length=30)
    link = models.CharField(max_length=150, primary_key=True)

from django.db import models


class lang(models.Model):
    name = models.CharField(primary_key=True, max_length=10)
    pub_date = models.DateField()
    inventor = models.CharField(max_length=100)
    application = models.CharField(max_length=200)
    intro = models.TextField()

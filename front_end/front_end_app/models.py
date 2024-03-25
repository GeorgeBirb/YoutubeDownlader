# front_end_app/models.py
from django.db import models

class UrlData(models.Model):
    url = models.TextField()


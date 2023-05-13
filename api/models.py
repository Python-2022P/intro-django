from django.db import models


class Phone(models.Model):
    name        = models.TextField()
    description = models.TextField()


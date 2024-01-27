from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    view_count = models.IntegerField()
    point_count = models.IntegerField()
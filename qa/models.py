from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    view_count = models.IntegerField()
    point_count = models.IntegerField()

    def __str__(self):
        return self.title
from django.db import models


class ToDo(models.Model):
    task = models.CharField(max_length=255)
    data = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return self.task

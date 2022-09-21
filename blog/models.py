from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    description = models.TextField()

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title


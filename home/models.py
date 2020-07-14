from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

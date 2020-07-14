from django.db import models


class Newsletter(models.Model):
    email = models.CharField(max_length=250)
    subscribed = models.DateTimeField(auto_now_add=True)
    unsubscribed = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-subscribed',)
        db_table = 'newsletter'

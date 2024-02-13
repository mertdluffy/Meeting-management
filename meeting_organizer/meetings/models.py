from django.db import models

class Meeting(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    participants = models.TextField()

    def __str__(self):
        return self.subject

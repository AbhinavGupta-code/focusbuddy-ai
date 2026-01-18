from django.db import models

class StudySession(models.Model):
    subject = models.CharField(max_length=100)
    time_available = models.IntegerField()
    energy_level = models.CharField(max_length=20)
    ai_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

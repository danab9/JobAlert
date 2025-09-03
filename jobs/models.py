from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} at {self.company} ({self.location})"
    

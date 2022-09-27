from django.db import models

class Olimp(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Date_Start = models.DateTimeField(blank=True,null=True)
    Date_End = models.DateTimeField(blank=True,null=True)
    Site = models.URLField(blank=True)
    #tags = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.Title
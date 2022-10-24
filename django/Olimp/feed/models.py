from django.db import models

class Olimp(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Date_Start = models.DateTimeField(blank=True,null=True)
    Date_End = models.DateTimeField(blank=True,null=True)
    Site = models.URLField(blank=True)
    tags = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.Title
    
    
    
class Trier(models.Model):
    Name = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    SecondName = models.CharField(max_length=100)
    Form = models.IntegerField()
    OlimpTry = models.ForeignKey(Olimp, on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.Name, self.LastName
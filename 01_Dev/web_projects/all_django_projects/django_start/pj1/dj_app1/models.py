from django.db import models

# Create your models here.
class Series(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    synopsis = models.TextField()
    image = models.ImageField(upload_to='static/images/')

class Session(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    synopsis = models.TextField()
    duration_secs = models.DurationField()
    url = models.URLField()
    image = models.ImageField(upload_to='static/images/')
    pud_date = models.DateTimeField('Date Published')


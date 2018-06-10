from django.db import models
# Create your models here.

class Fish(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(blank=False, null=False) 
    created = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    image_id = models.IntegerField()
    #image_id = models.ForeignKey(
    #    'Fish',
    #    on_delete=models.CASCADE,
    #)
    report_type = models.CharField(max_length=20, default='report_type')
    title = models.CharField(max_length=255, default='title')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

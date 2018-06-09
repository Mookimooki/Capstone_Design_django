from django.db import models

# Create your models here.

class Fish(models.Model):
    #_id = models.ObjectIdField()
    image = models.FileField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
    image_id = models.ForeignKey(
        Fish,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    one_to_one = True


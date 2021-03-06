from django.db import models

# Create your models here.

class Blog_Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
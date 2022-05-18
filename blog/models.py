from django.db import models

# Create your models here.
# COMO SE CREO EL POST 1
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    
    def __str__(self):
        return self.title
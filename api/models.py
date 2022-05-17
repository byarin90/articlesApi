from django.db import models
# Create your models here.

# Table Class
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
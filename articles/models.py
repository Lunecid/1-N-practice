from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()    
    at_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Commnet(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE) 



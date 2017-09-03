from django.db import models

# Create your models here.
class Blogs(models.Model):
    email=  models.CharField(max_length=255)
    text=  models.TextField()
    title=  models.TextField()
    createdAt = models.DateTimeField(auto_now_add = True)
    class Meta:
        db_table='blogs'

class Comments(models.Model):
    blog = models.ForeignKey(Blogs)
    comment =  models.TextField()
    createdAt = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table='comments'
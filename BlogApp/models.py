from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image')
    desc = models.TextField()
    time = models.DateTimeField(auto_now_add = True)

class Comment_section(models.Model):
    comnt_id=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200,null=True)
    comment = models.CharField(max_length=200,null=True)


class Share_blg(models.Model):
    share_id = models.AutoField(primary_key=True)
    sender_mail= models.CharField(max_length=200,null=True)
    sender_name = models.CharField(max_length=200,null=True)
    content = models.CharField(max_length=200,null=True)

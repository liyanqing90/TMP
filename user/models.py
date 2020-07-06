from django.db import models

# Create your models here.
class Project(models.Model):
    '''项目表'''
    name = models.CharField(null=False,unique=True,max_length=20)

class Status(models.Model):
    '''状态表'''
    name = models.CharField(null=False,unique=True,max_length=20)

class Requirement(models.Model):
    '''需求表'''
    name=models.CharField(null=False,unique=True,max_length=20)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    category = models.CharField(max_length=10,null=False)
    owner  = models.CharField(max_length=10,null=False)
    status =models.ForeignKey(Status,on_delete=models.CASCADE)
    finish = models.IntegerField(default=3,choices=((0,'执行中'),(1,'已归档'),(3,'未开始')))
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(null=False, max_length=10)
    password = models.CharField(null=False, max_length=10)


class Project(models.Model):
    '''项目表'''
    name = models.CharField(null=False, unique=True, max_length=20)


class Status(models.Model):
    '''状态表'''
    name = models.CharField(null=False, unique=True, max_length=20)


class Category(models.Model):
    name = models.CharField(null=False, unique=True, max_length=20)


class Requirement(models.Model):
    '''需求表'''
    name = models.CharField(null=False, unique=True, max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    finish = models.IntegerField(default=3, choices=((0, '执行中'), (1, '已归档'), (3, '未开始')))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

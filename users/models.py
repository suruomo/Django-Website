# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from datetime import  datetime

# Create your models here.
from django.db import models
# 继承默认用户表并进行修改
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birthday=models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender=models.CharField(max_length=7,choices=(("male",u"男"),("female",u"女")),default="female")
    address=models.CharField(max_length=100,verbose_name=u"地址",default=u"")
    mobile=models.CharField(max_length=11,verbose_name=u"手机号",null=True,blank=True)
    image=models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.username
class EmailVerrifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name="验证码")
    email=models.CharField(max_length=50,verbose_name="邮箱")
    send_type=models.CharField(choices=(("register","注册"),("forget","找回密码")),max_length=10)
    send_time=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name="邮箱验证码"
        verbose_name_plural=verbose_name

class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name="标题",)
    image=models.ImageField(upload_to="banner/%Y/%m",verbose_name="轮播图",max_length=100)
    url=models.URLField(max_length=200,verbose_name="访问地址")
    index=models.IntegerField(max_length=100,verbose_name="顺序")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name="轮播图"
        verbose_name_plural=verbose_name
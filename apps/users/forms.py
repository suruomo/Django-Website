# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/4/28 13:42'
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    # 字段定义同页面name定义一致
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    email=forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # 验证码字段
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})

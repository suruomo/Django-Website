# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/4/28 13:42'
from django import forms
from captcha.fields import CaptchaField

# 登陆表单
class LoginForm(forms.Form):
    # 字段定义同页面name定义一致
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)

# 注册表单
class RegisterForm(forms.Form):
    email=forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # 验证码字段
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})

#忘记密码表单
class ForgetPwdForm(forms.Form):
    email=forms.EmailField(required=True)
    # 验证码字段
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})

#重置密码表单
class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)
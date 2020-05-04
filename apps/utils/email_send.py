# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/4/30 15:38'

from random import Random
# 内置发送邮箱
from django.core.mail import send_mail
from users.models import EmailVerrifyRecord
from django_web.settings import EMAIL_FROM


# 发送邮箱验证码
def send_register_email(email, send_type="register"):
    email_record = EmailVerrifyRecord()
    # 生成验证码
    code = generate_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    # 将验证码保存到数据库中
    email_record.save()
    email_title = ""
    email_body = ""
    if send_type == "register":
        email_title = "慕学在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "慕学在线网忘记密码重置链接"
        email_body = "请点击下面的链接重置密码：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


# 生成随机验证码
def generate_random_str(randomlength=8):
    str = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

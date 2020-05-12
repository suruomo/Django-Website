"""django_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url

import xadmin
from django.urls import path, include, re_path
from organization.views import OrgView
from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ModifyPwdView,ResetView
# Template文件相关
from django.views.generic import TemplateView
# 处理静态文件
from django.views.static import serve

from django_web.settings import MEDIA_ROOT
urlpatterns = [
    path(r'xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"),name="index"),
    path('login', LoginView.as_view(),name="login"),
    path('register', RegisterView.as_view(),name="register"),
    # 验证码路径
    path('captcha', include('captcha.urls')),
    # 激活用户
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name="user_active" ),
    # 忘记密码
    re_path('forget',ForgetPwdView.as_view(),name="forget_pwd" ),
    # 重置密码页面
    re_path('reset/(?P<active_code>.*)/',ResetView.as_view(),name="reset_pwd" ),
    # 修改密码
    re_path('modify_pwd',ModifyPwdView.as_view(),name="modify_pwd" ),
    # 课程机构首页
    re_path('org_list',OrgView.as_view(),name="org_list" ),

    # media信息，配置上传文件的访问处理
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]

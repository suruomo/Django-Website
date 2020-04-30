from django.shortcuts import render
from django.contrib.auth import  authenticate,login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm,RegisterForm
from utils.email_send import send_register_email
from .models import EmailVerrifyRecord
# 密码加密
from django.contrib.auth.hashers import make_password
# Create your views here.
# 自定义登录
class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 自定义通过用户名或者邮箱登陆
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 基于类实现登录
class LoginView(View):

    def get(self,request):
        return render(request, "login.html", {})

    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            # 如果用户不为空
            if user is not None:
                # 如果用户激活登录
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {'msg': "用户未激活！"})
            else:
                return render(request, "login.html", {'msg': "用户名或密码错误！"})
        else:
            return render(request, "login.html", {"login_form":login_form})



# 基于函数实现登录
# def user_login(request):
#     if request.method == "POST":
#         user_name=request.POST.get("username","")
#         pass_word=request.POST.get("password","")
#         user=authenticate(username=user_name,password=pass_word)
#         if user is not None:
#             login(request,user)
#             return render(request,"index.html")
#         else:
#             return render(request,"login.html",{'msg':"用户名或密码错误！"})
#     elif request.  method == "GET":
#         return render(request,"login.html",{})

# 基于类实现注册
class RegisterView(View):

    def get(self,request):
        # 需要返回验证码
        register_form=RegisterForm()
        return render(request,"register.html",{'register_form':register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")
            user_profile=UserProfile()
            user_profile.username=user_name
            user_profile.email=user_name
            # 密码加密
            user_profile.password=make_password(pass_word)
            user_profile.is_active=False
            user_profile.save()
            send_register_email(user_name,"register")
            return render(request, "login.html")
        else:
            return render(request, 'register.html',{"register_form":register_form})


class ActiveUserView(View):
    def get(self,request,active_code):
        all_record=EmailVerrifyRecord.objects.filter(code=active_code)
        if all_record:
            for record in all_record:
                email=record.email
                user=UserProfile.objects.get(email=email)
                user.is_active=True
                user.save()
        return render(request, "login.html")

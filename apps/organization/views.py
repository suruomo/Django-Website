# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .models import CourseOrg,CityDict

class OrgView(View):
    """
    获取课程机构列表功能
    """
    def get(self,request):
        # 所有课程机构
        all_orgs=CourseOrg.objects.all()
        # 所有城市
        all_citys=CityDict.objects.all()
        # 机构数量
        org_nums=all_orgs.count()
        return render(request,"org-list.html",{
            "all_orgs":all_orgs,
            "all_citys":all_citys,
            "org_nums":org_nums
        })
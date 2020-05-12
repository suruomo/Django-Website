# -*- coding: utf-8 -*-
from django.core.paginator import PageNotAnInteger
from django.shortcuts import render, render_to_response
from django.views.generic import View
# Create your views here.
from pure_pagination import Paginator

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
        org_nums = all_orgs.count()

        # 对课程机构分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
# 第二个参数为每页显示条数，必须写，官方文档没有
        p = Paginator(all_orgs,3,request=request)
        orgs = p.page(page)

        return render(request,"org-list.html",{
            "all_orgs":orgs,
            "all_citys":all_citys,
            "org_nums":org_nums
        })
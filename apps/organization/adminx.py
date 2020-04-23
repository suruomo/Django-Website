# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/4/23 16:09'

import xadmin
from .models import CityDict,Teacher,CourseOrg

class CityDictAdmin(object):
    # 列表显示字段
    list_display=['name','desc',"add_time" ]
    # 搜索字段
    search_fields=['name','desc']
    # 筛选字段
    list_filter=['name','desc',"add_time" ]


class CourseOrgAdmin(object):

    # 列表显示字段
    list_display = ['name', 'desc', 'click_nums', "fav_nums",'image', 'address', "city","add_time"]
    # 搜索字段
    search_fields = ['name', 'desc', 'click_nums', "fav_nums",'image', 'address', "city"]
    # 筛选字段
    list_filter = ['name', 'desc', 'click_nums', "fav_nums",'image', 'address', "city","add_time"]

class TeacherAdmin(object):
    # 列表显示字段
    list_display = ['org', 'name', 'work_years', "work_company",'work_position', 'points', "click_nums","fav_nums","add_time"]
    # 搜索字段
    search_fields = ['org', 'name', 'work_years', "work_company",'work_position', 'points', "click_nums","fav_nums"]
    # 筛选字段
    list_filter =  ['org', 'name', 'work_years', "work_company",'work_position', 'points', "click_nums","fav_nums","add_time"]

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)

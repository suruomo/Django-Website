# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/4/23 15:52'

import xadmin
from .models import Course,Video,Lesson,CourseResource

class CourseAdmin(object):
    # 列表显示字段
    list_display = ['name', 'desc', 'detail', "degree",'learn_time', 'students', 'fav_nums', "image", 'click_nums', "add_time"]
    # 搜索字段
    search_fields = ['name', 'desc', 'detail', "degree",'learn_time', 'students', 'fav_nums', "image", 'click_nums']
    # 筛选字段
    list_filter =['name', 'desc', 'detail', "degree",'learn_time', 'students', 'fav_nums', "image", 'click_nums', "add_time"]


class LessonAdmin(object):
    # 列表显示字段
    list_display = ['course', 'name',"add_time"]
    # 搜索字段
    search_fields = ['course', 'name']
    # 筛选字段
    list_filter = ['course', 'name',"add_time"]


class VideoAdmin(object):
    # 列表显示字段
    list_display = ['lesson', 'name', "add_time"]
    # 搜索字段
    search_fields = ['lesson', 'name']
    # 筛选字段
    list_filter = ['lesson', 'name', "add_time"]



class CourseResourceAdmin(object):
    # 列表显示字段
    list_display = ['course', 'name',"download", "add_time"]
    # 搜索字段
    search_fields = ['course','name',"download"]
    # 筛选字段
    list_filter = ['course', 'name', "download","add_time"]

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
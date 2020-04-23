# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/4/23 16:00'

import xadmin
from .models import UserAsk,UserMessage,UserCourse,CourseComments,UserFavorite

class UserAskAdmin(object):
    # 列表显示字段
    list_display = ['name', 'mobile', 'course_name', "add_time"]
    # 搜索字段
    search_fields = ['name', 'mobile', 'course_name']
    # 筛选字段
    list_filter =['name', 'mobile', 'course_name', "add_time"]


class CourseCommentsAdmin(object):
    # 列表显示字段
    list_display = ['user', 'course', 'comments', "add_time"]
    # 搜索字段
    search_fields = ['user', 'course', 'comments']
    # 筛选字段
    list_filter =['user', 'course', 'comments', "add_time"]


class UserFavoriteAdmin(object):
    # 列表显示字段
    list_display = ['user', 'fav_id', 'fav_type', "add_time"]
    # 搜索字段
    search_fields = ['user', 'fav_id', 'fav_type']
    # 筛选字段
    list_filter =['user', 'fav_id', 'fav_type', "add_time"]


class UserMessageAdmin(object):
    # 列表显示字段
    list_display = ['user', 'message', 'has_read', "add_time"]
    # 搜索字段
    search_fields = ['user', 'message', 'has_read']
    # 筛选字段
    list_filter =['user', 'message', 'has_read', "add_time"]



class UserCourseAdmin(object):
    # 列表显示字段
    list_display = ['user', 'course', "add_time"]
    # 搜索字段
    search_fields = ['user', 'course']
    # 筛选字段
    list_filter =['user', 'course', "add_time"]


xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
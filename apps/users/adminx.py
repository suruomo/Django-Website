# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/4/23 15:02'

import xadmin
from xadmin import views
from .models import EmailVerrifyRecord,Banner

# 基础配置
class BaseSetting(object):
    # 允许主题
    enable_themes=True
    use_bootswatch=True

# 全局配置
class GlobalSetting(object):
    # 左上角页头
    site_title="慕学后台管理系统"
    # 页脚
    site_footer="慕学在线网"
    # 设置菜单栏收缩
    menu_style="accordion"

class EmailVerifyRecordAdmin(object):
    # 列表显示字段
    list_display=['code','email','send_type',"send_time" ]
    # 搜索字段
    search_fields=['code','email','send_type']
    # 筛选字段
    list_filter=['code','email','send_type',"send_time" ]


class BannerAdmin(object):
    # 列表显示字段
    list_display = ['title', 'image', 'url', "index","add_time"]
    # 搜索字段
    search_fields = ['title', 'image', 'url', "index"]
    # 筛选字段
    list_filter = ['title', 'image', 'url', "index","add_time"]

# 注册model
xadmin.site.register(EmailVerrifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
# 注册基础配置
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 注册全局配置
xadmin.site.register(views.CommAdminView,GlobalSetting)

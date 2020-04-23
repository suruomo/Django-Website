# -*- coding: utf-8 -*-
__author__ = 'suruomo'
__date__ = '2020/4/23 15:02'

import xadmin
from .models import EmailVerrifyRecord,Banner

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

xadmin.site.register(EmailVerrifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
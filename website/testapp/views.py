# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import tushare as ts
 
def index(request):
    return HttpResponse(u"欢迎光临DataMole！")
	
def dahua(request):
    # 大华
    # dahua = ts.get_realtime_quotes('002236')
    # changeDH = (float(dahua.iloc[0,3])-float(dahua.iloc[0,2]))/float(dahua.iloc[0,2])*100
    # dh = '%s %.2f%%' %(dahua.iloc[0,3], changeDH)
    
    # 北部湾港
    beibuwan = ts.get_realtime_quotes('000582')
    changeBBW = (float(beibuwan.iloc[0,3])-float(beibuwan.iloc[0,2]))/float(beibuwan.iloc[0,2])*100
    BBW = '%s %.2f%%' %(beibuwan.iloc[0,3], changeBBW)
    
    # 上证、深证
    shrt = ts.get_realtime_quotes('sh')
    changeSH = (float(shrt.iloc[0,3])-float(shrt.iloc[0,2]))/float(shrt.iloc[0,2])*100
    SH = '%s %.2f%%' %(shrt.iloc[0,3], changeSH)
    
    # 创业板
    cyb = ts.get_realtime_quotes('cyb')
    changeCYB = (float(cyb.iloc[0,3])-float(cyb.iloc[0,2]))/float(cyb.iloc[0,2])*100
    CYB = '%s %.2f%%' %(cyb.iloc[0,3], changeCYB)
    
    strPrint = 'BBW ' + BBW \
    + '<br>SH ' + SH \
    + '<br>CYB ' + CYB
    return HttpResponse(strPrint)
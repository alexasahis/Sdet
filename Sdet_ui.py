#!/usr/bin/env python
# -*- coding: utf-8 -*-

#------------------------
#Author:qiuzhiqian
#Email:xia_mengliang@163.com
#------------------------

import Sdet_core
import tkinter as tk

top = tk.Tk()
top.title("Sdet")                                       #����UI����

TopFrame=tk.Frame(top,width=60)                         #��������ʹ��
WordEntry=tk.Entry(TopFrame,width=45)                   #����һ�������ı���
SearchBtn=tk.Button(TopFrame,text="Search",width=15)    #����һ����ť

ResultLabel=tk.Label(top,text='Nothing',height=15,width=65,bg='#FFFFDD',justify=tk.LEFT)    #����һ����ʾ��ǩ

def BtnCallback():                                      #��ť�����ص�����
    words=WordEntry.get()                               #��ȡ�ı����е��ı�
    sdh=Sdet_core.Sdet_handle()
    if(sdh.priority==0):
        res=sdh.GetWordLocalInfo(words)
        if(res<0):          #���ز�ѯ�޽��
            sdh.GetWordWebInfo(sdh.GetWebString(words))
            sdh.SaveLocalInfo()     #�������ݿ�
    else:
        sdh.GetWordWebInfo(sdh.GetWebString(words))
    
    out_string=sdh.Result_Formate()
    ResultLabel.configure(text=out_string,anchor=tk.NW)

SearchBtn.configure(command=BtnCallback)        #���ûص�����

WordEntry.grid(row=0,column=0)              #����
SearchBtn.grid(row=0,column=1)

TopFrame.grid(row=0,column=0)
ResultLabel.grid(row=1,column=0)


# ������Ϣѭ��
top.mainloop()

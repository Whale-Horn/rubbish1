#!/usr/bin/python3
# -*- coding: utf-8 -*-

import viVoicecloud as vv
from sjtu.answer import aiui_answer
vv.Login()
t = vv.tts()
print("请输入问题，输入exit退出\n================")
while 1:   
    q = input("问题：")
    if q=="exit":
        break
    else:     
        aiui_answer(q,vv,t)
vv.Logout()


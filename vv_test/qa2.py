#!/usr/bin/python3
#-*- coding:utf-8-*-

import viVoicecloud as vv
from sjtu.answer import aiui_answer, my_answer

# 登录vivoicecloud账号
vv.Login()

# 创建语音合成对象
t = vv.tts()

print("请输入问题，输入exit退出")

while True:
    q = input("问题：")
    if q == "exit":
        break
    else:
        if not my_answer(q,t):
            aiui_answer(q,vv,t)
vv.Logout()

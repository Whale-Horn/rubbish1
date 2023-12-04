#!/usr/bin/python3
#-*- coding:utf-8 -*-

def aiui_answer(q,vv,tts):
    a = vv.aiui(q)
    if a[0]!=4:
        if a[1] in ["openQA","datetime","weather","calc","baike","poetry","news"]:
            for i in a[3]:
                tts.say(i)
                
        elif a[1] == "musicX":
            tts.say("暂时不会唱歌")

        else:
            tts.say("对不起，我无法回答这个问题")

    else:
        tts.say("对不起，我无法回答这个问题")



myqa = {
    "你好":["你好！跟我聊聊吧"],
    "lol":["恕瑞玛！你们的皇帝回来啦！","圣火将你洗涤！","懦弱之举我决不姑息！"],
     "你(真|好|非常)?聪明":["没人生来杰出","你的眼光不错","你这样说我会骄傲的"],
     "再见|再会|我走了":["勇敢地前进吧，朋友","愿圣光指引你的方向","为了联盟"],
    }
import random
import re

def my_answer(q,tts):
    for key in myqa:
        if re.search(key,q):
            alist = myqa[key]
            n = random.randint(0,len(alist)-1)
            tts.say(alist[n])
            return True
    else:
        return False
    

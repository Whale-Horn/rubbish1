#!/usr/bin/python3
# -*- coding: utf-8 -*-

#第一步：检索歌曲
import urllib
import urllib.request
import json

url = "http://tingapi.ting.baidu.com/v1/restserver/ting?"
url += "from=webapp_music"
url += "&method=baidu.ting.search.catalogSug"
url += "&format=json"

keywords = "少年"
keywords_encoded = urllib.parse.quote(keywords) #转成urlcode编码

url += "&query="+keywords_encoded

# 尝试10次检索

songid = None
for i in range(10):   
    ref = urllib.request.urlopen(url)
    result = ref.read()
    dict1 = json.loads(str(result,encoding='utf-8'))
    try:
        songid = dict1["song"][0]["songid"]
        print("songID: "+ songid)
        break
    except:
        pass
else:
    print("检索失败")

if songid:
    
    #第二步：获取链接

    # url2 = "http://music.taihe.com/data/music/fmlink?"  #弃用
    url2 = "http://play.taihe.com/data/music/songlink?type=m4a,mp3"
    url2 += "&songIds="+songid

    ref2 = urllib.request.urlopen(url2)
    result2 = ref2.read()

    dict2 = json.loads(str(result2,encoding='utf-8'))
    songLink = dict2["data"]["songList"][0]["songLink"]
    print("songLink: "+songLink)


    #第三步：下载或播放

    #urllib.request.urlretrieve(songLink,"myMusic.mp3")  #可以下载

    import vlc
    p = vlc.MediaPlayer(songLink)
    p.play()                                            #直接播放

    import time
    time.sleep(5)

    while p.is_playing():                        #每隔0.5秒循环一次，直到音乐播放结束
        time.sleep(0.5)             









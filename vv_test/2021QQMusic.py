import urllib.parse as parse
from urllib.request import urlretrieve
import requests
import json
import os
import time
import sys


def Time_1():  # 进度条函数
    for i in range(1, 51):
        sys.stdout.write('\r')
        sys.stdout.write('{0}% |{1}'.format(int(i % 51) * 2, int(i % 51) * '■'))
        sys.stdout.flush()
        time.sleep(0.125)
    sys.stdout.write('\n')


def get_download_url(song_name:str,song_index:int):
    w = parse.urlencode({'w': song_name})
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=63229658163010696&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&%s&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0' % (
        w)
    content = requests.get(url=url)
    str_1 = content.text
    dict_1 = json.loads(str_1)
    song_list = dict_1['data']['song']['list']
    str_3 = '''https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey5559460738919986&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"1825194589","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"1825194589","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'''
    url_list = []
    music_name = []

    for i in range(len(song_list)):
        music_name.append(song_list[i]['name'] + '-' + song_list[i]['singer'][0]['name'])

        print('{}.{}-{}'.format(i + 1, song_list[i]['name'], song_list[i]['singer'][0]['name']))
        url_list.append(str_3 % (song_list[i]['mid']))

    id = int(song_index)
    content_json = requests.get(url=url_list[id - 1])
    dict_2 = json.loads(content_json.text)
    url_ip = dict_2['req']['data']['freeflowsip'][1]
    purl = dict_2['req_0']['data']['midurlinfo'][0]['purl']
    return  url_ip + purl

# try:
#     os.mkdir('./QQ音乐')
# except:
#     pass
# finally:
#     try:
#         print('开始下载...')
#         urlretrieve(url=downlad, filename='./QQ音乐/{}.mp3'.format(music_name[id - 1]))
#         Time_1()
#         print('{}.mp3下载完成！'.format(music_name[id - 1]))
#     except Exception as e:
#         print(e, '对不起，你没有该歌曲的版权！')
import vlc
p = vlc.MediaPlayer(get_download_url("小苹果",1))
p.play()                                            #直接播放

import time
time.sleep(5)

while p.is_playing():                        #每隔0.5秒循环一次，直到音乐播放结束
    time.sleep(0.5)
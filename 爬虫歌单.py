# -*- coding: utf-8 -*-
import json
import os
import requests

headers = {
    'Origin': 'https://y.qq.com',
    'Referer': 'https://y.qq.com/portal/search.html',
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}


def get_music_info():
    music_info_list = []
    name = input('请输入歌手或歌曲：')  # input函数 输入 做用户交互 使用的
    page = input('请输入页码：')
    num = input('请输入当前页码需要返回的数据条数：')
    url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p={page}&n={num}&w={name}'
    response = requests.get(url).text  # 获取到的是字符串
    # 将response切分成json格式 类似字典 但是现在还是字符串
    music_json = response[9:-1]
    # json转字典
    music_data = json.loads(music_json)  # 转换成 字典
    # print(music_data)
    music_list = music_data['data']['song']['list']
    for music in music_list:
        music_name = music['songname']  # 歌曲的名字
        singer_name = music['singer'][0]['name']  # 歌手的名字
        songmid = music['songmid']
        media_mid = music['media_mid']
        music_info_list.append((music_name, singer_name, songmid, media_mid))
    return music_info_list


# 获取vkey
def get_purl(music_info_list):
    music_data = []
    for music in music_info_list:
        music_name = music[0]
        singer_name = music[1]
        songmid = music[2]
        url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"8846039534","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8846039534","songmid":["%s"],"songtype":[0],"uin":"1152921504784213523","loginflag":1,"platform":"20"}},"comm":{"uin":"1152921504784213523","format":"json","ct":24,"cv":0}}' % songmid
        response = requests.get(url).json()  # 如果你获取的数据 是 {}  .json() 他会直接帮我们转换成字典
        purl = response['req_0']['data']['midurlinfo'][0]['purl']
        full_media_url = 'http://dl.stream.qqmusic.qq.com/' + purl
        music_data.append(
            {
                'music_name': music_name,
                'singer_name': singer_name,
                'full_media_url': full_media_url
            }
        )
    return music_data


def save_music_mp3(music_data):
    if not os.path.exists('歌曲下载'):  # 判断是否有歌曲下载文件夹
        os.mkdir('歌曲下载')  # 如果没有创建 歌曲下载文件夹
    for music in music_data:
        music_name = music['music_name']
        singer_name = music['singer_name']
        full_url = music['full_media_url']
        music_response = requests.get(full_url, headers=headers).content
        with open('歌曲下载/%s-%s.mp3' % (music_name, singer_name), 'wb')as fp:
            fp.write(music_response)
            print('[%s]保存成功！' % music_name)


if __name__ == '__main__':
    music_info_list = get_music_info()
    music_data = get_purl(music_info_list)
    save_music_mp3(music_data)

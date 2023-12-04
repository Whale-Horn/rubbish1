# -*- coding: utf-8 -*-
import pyaudio
import viVoicecloud as vv
from sjtu.audio import findDevice

device_in = findDevice("pulse","input")
Sample_channels = 1  
Sample_rate = 16000  
Sample_width = 2         
time_seconds = 0.5  #录音片段的时长，建议设为0.2-0.5秒

p = pyaudio.PyAudio()
stream = p.open(
            rate=Sample_rate,
            format=p.get_format_from_width(Sample_width),
            channels=Sample_channels,
            input=True,
            input_device_index=device_in,
            start = False)

vv.Login()#登录
ASR=vv.asr()#实例化
ASR.SessionBegin(language='Chinese')#开始语音识别

stream.start_stream()
print ('***Listening...')

#录音并上传到讯飞，当判定一句话已经结束时，status返回3
status=0
while status!=3:
    frames=stream.read(int(Sample_rate*time_seconds))
    ret,status,recStatus=ASR.AudioWrite(frames)
    
stream.stop_stream()
print ('---GetResult...')
    
words=ASR.GetResult()#获取结果
ASR.SessionEnd()#结束语音识别
print (words)
vv.Logout()#注销
stream.close()
p.terminate()








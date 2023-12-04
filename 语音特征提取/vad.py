#!/usr/bin/python3
# -*- coding:utf-8 -*-

import webrtcvad
import wave

def get_speech_part(file, new_file, minTime):
    fl = wave.open(file, "rb")
    rate = fl.getframerate()
    vad = webrtcvad.Vad(1)
    speech_part = b''
    
    # 检测起点
    while True:
        part = fl.readframes(int(rate * 0.03))
        if part != b'':
            if vad.is_speech(part, rate):
                speech_part += part
                break
            
    # 检测终点
    while True:
        part = fl.readframes(int(rate * 0.03))
        if part != b'':
            speech_part += part
        else:
            if vad.is_speech(part, rate):
                break
            else:
                if len(speech_part) < (rate + minTime * 2):
                    continue
                else:
                    fl.close()
                    f2 = wave.open(new_file, "wb")
                    f2.setframerate(rate)
                    f2.setnchannels(1)
                    f2.setsampwidth(2)
                    f2.writeframes(speech_part)
                    f2.close()
                    break
    fl.close()

if __name__ == "__main__":
    get_speech_part("standard.wav", "new_standard.wav", 0.5)
    get_speech_part("record.wav", "new_record.wav", 0.5)

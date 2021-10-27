import os, sys
import time

from threading import Thread

import openpibo
from openpibo.speech import Speech
from openpibo.audio import Audio

import requests
import json

import argparse

class mySpeech(Speech):
    def __init__(self, txtname='questions.txt'):
        super().__init__()
        self.question=[]
        #self.read_txt(txtname)
        
    def my_mic(self, dst, timeout=5):
        if os.path.isfile(dst):
            os.remove(dst)
        #arecord -l 에서 카드가 잡혀야 함. (snd_rpi_simple_card)
        cmd = f"arecord -D default -c2 -r 16000 -f S32_LE -d {timeout} -t wav -q -vv -V streo stream.raw;sox stream.raw -c 1 -b 16 {dst};rm stream.raw"
        os.system(cmd)
        audio_obj.play(filename=dst, out='local', volume=-2000)
        time.sleep(5)
        audio_obj.stop()
    
    def kakao_stt(self,dst):
        url = 'https://kakaoi-newtone-openapi.kakao.com/v1/recognize'
        #headers = {'Content-Type':'application/octet-stliream', 'Authorization':'KakaoAK' + kakao_account}
        headers = {
          'Content-Type': 'application/octet-stliream',
          'Authorization': 'KakaoAK ' + self.kakao_account
        }
        with open(dst, 'rb') as f:
            data = f.read()
        res = requests.post(url, headers=headers, data=data)
        try:
          result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1]
        except Exception as ex:
          result_json_string = res.text[res.text.index('{"type":"errorCalled"'):res.text.rindex('}')+1]
        result = json.loads(result_json_string)
        return result['value']
    
        
    def my_stt(self,num):
        filename = f"stream{num}.wav"
        self.my_mic(filename)
        result = self.kakao_stt(filename)
        return result
    
    def read_txt(self, filename):
        f=open(filename, 'r')
        for num, line in enumerate(f.readlines()):
            line = line.rstrip('\n')
            if not len(line) == 0:
                self.question.append(line)
        
    def my_tts(self, num, line):
        filename = f"tts{num}.mp3"
        speech_obj.tts(f"<speak>\
                  <voice name='WOMAN_READ_CALM'>{line}<break time='500ms'/></voice>\
                </speak>",filename)
        audio_obj.play(filename, out='local', volume=-1500, background=False)
        
    def test(self):
        for num, line in enumerate(self.question):
            print(f"{num}, {line}")
            self.my_tts(num, line)
            self.my_stt(num)
    
if __name__ == "__main__":
    #arg = argparse.ArgumentParser()
    audio_obj = Audio()
    speech_obj = mySpeech()
    speech_obj.test()

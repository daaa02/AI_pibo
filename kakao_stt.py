import os, sys
import time

from threading import Thread

import openpibo
from openpibo.speech import Speech
from openpibo.audio import Audio

import requests
import json

import argparse

audio = Audio()

rest_api_key = 'f8f8c3f66bb3310016fdeccffba152e8'


class mySpeech:

    def record(self, filename="stream.wav", timeout=10):

        if srest_api_key in [None, '']:
            raise Exception('Kakao account invalid')

        if os.path.isfile(filename):
            os.remove(filename)

        cmd = f"arecord -D hw:2,0 -c1 -r44100 -f S16_LE -d {timeout} -t wav -q -vv -V streo stream.raw;sox stream.raw -c 1 -b 16 {filename};rm stream.raw"
        os.system(cmd)

    def kakao_stt(self, filename):
        url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
        headers = {
            "Content-Type": "application/octet-stream",
            "X-DSS-Service": "DICTATION",
            "Authorization": "KakaoAK " + rest_api_key,
        }

        with open(filename, 'rb') as fp:
            data = fp.read()
        res = requests.post(url, headers=headers, data=data)

        result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1]
        result = json.loads(result_json_string)
        print(result['value'])
        return result['value']

        # try:
        #     result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1]
        # except Exception as ex:
        #     result_json_string = res.text[res.text.index('{"type":"errorCalled"'):res.text.rindex('}') + 1]
        # result = json.loads(result_json_string)
        # return result['value']


    def my_stt(self):
        filename = f"stream.wav"
        self.record(filename)
        result = self.kakao_stt(filename)
        return result

import os
import sys
import time
import json
import requests
from threading import Thread
from konlpy.tag import Mecab

import openpibo
import openpibo_models
from openpibo.speech import Speech
from openpibo.audio import Audio
from . import config


def stt(self, filename="stream.wav", timeout=5):
    if self.kakao_account in [None, '']:
        raise Exception('Kakao account invalid')

    os.system(f'arecord -t raw -c 1 -D plughw:1,0 -f S16_LE -d {timeout} -r 16000 {filename}')

    '''curl -v "https://kakaoi-newtone-openapi.kakao.com/v1/recognize" \
    -H "Transfer-Encoding: chunked" -H "Content-Type: application/octet-stream" \
    -H "Authorization: KakaoAK API_KEY" \
    --data-binary @stream.wav '''
    url = 'https://kakaoi-newtone-openapi.kakao.com/v1/recognize'
    headers = {
        'Content-Type': 'application/octet-stliream',
        'Authorization': 'KakaoAK ' + self.kakao_account
    }

    with open(filename, 'rb') as f:
        data = f.read()
    res = requests.post(url, headers=headers, data=data)
    try:
        result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1]
    except Exception as ex:
        result_json_string = res.text[res.text.index('{"type":"errorCalled"'):res.text.rindex('}') + 1]
    result = json.loads(result_json_string)
    return result['value']

def test():
    result = stt('/home/pi/'stream.wav', 5)
    print(result)

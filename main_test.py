import openpibo
from openpibo.speech import Speech
from openpibo.audio import Audio

import scenario_1
import scenario_2
import scenario_3
import scenario_4

speech = Speech()
audio = Audio()


def main():
  scenario_1.play_balloon_soccer()
#   scenario_2.play_tissue_load()
#   scenario_3.play_animal_in_hoop()
#   scenario_4.play_im_king()


if '__name__' == "__main__"
  def stt():
    rest_api_key = 'f8f8c3f66bb3310016fdeccffba152e8'

    kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    headers = {
        "Content-Type": "application/octet-stream",
        "X-DSS-Service": "DICTATION",
        "Authorization": "KakaoAK " + rest_api_key,
    }

    with open('stream.wav', 'rb') as fp:
        stream = fp.read()

    res = requests.post(kakao_speech_url, headers=headers, data=stream)
    # print(res.text)

    result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1]
    result_final = json.loads(result_json_string)
    result = result_final['value']
    print(result)
    return result


  def tts(speech_text):
    file = openpibo.config['DATA_PATH'] + "/tts.wav"
    speech.tts(f"<speak>\
                <voice name='WOMAN_READ_CALM'><prosody rate='slow'>{speech_text}<break time='500ms'/></prosody></voice>\
                </speak>", file)
    audio.play(file, 'local', '-1000', False)
    print("\n")
    print(speech_text)
    
main()


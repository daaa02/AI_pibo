import speech_recognition as sr

def stt()
  r = sr.Recognizer()
  with sr.Microphone() as source:
      print("Say something!")
      audio = r.listen(source)

  # 구글 웹 음성 API로 인식하기 (하루에 제한 50회)
  try:
      return(r.recognize_google(audio, language='ko'))
  except sr.UnknownValueError:
      return("인식 실패")
  except sr.RequestError as e:
      return("응답 없음; {0}".format(e))

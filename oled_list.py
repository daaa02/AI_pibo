import time

import openpibo
from openpibo.oled import Oled

o = Oled()

# time.sleep(n): n초 동안 이미지 표시(어차피 multi thread 로 종료될 거니까 길게 잡음)


def run():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_question():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_suggestion():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_explain():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_photo():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_stamp():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_waiting():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_cheer():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_compliment():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_concil():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_search():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_sleep():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_wakeup():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_agree():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_deny():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_joy():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_angry():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_sad():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()


def o_tired():
    o.draw_image(openpibo.config['DATA_PATH'] + "/image/clear.png")
    o.show()
    time.sleep(20)
    o.clear()
    o.show()

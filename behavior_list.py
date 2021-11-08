import time
from threading import Thread

import openpibo
from openpibo.motion import Motion
from openpibo.device import Device
from openpibo.speech import Speech
from openpibo.audio import Audio
from openpibo.oled import Oled


import motion_list
import eye_list
import oled_list

audio = Audio()


def do_question():
    # audio.play('/home/pi/openpibo/question.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_question(), args=())
    o = Thread(target=oled_list.o_question, args=())
    m = Thread(target=motion_list.m_question(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_suggestion():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_suggestion(), args=())
    o = Thread(target=oled_list.o_suggestion, args=())
    m = Thread(target=motion_list.m_suggestion(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_explain():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_explain(), args=())
    o = Thread(target=oled_list.o_explain, args=())
    m = Thread(target=motion_list.m_explain(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_photo():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_photo(), args=())
    o = Thread(target=oled_list.o_photo, args=())
    m = Thread(target=motion_list.m_photo(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_stamp():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_stamp(), args=())
    o = Thread(target=oled_list.o_stamp, args=())
    m = Thread(target=motion_list.m_stamp(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_waiting():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_waiting(), args=())
    o = Thread(target=oled_list.o_waiting, args=())
    m = Thread(target=motion_list.m_waiting(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_cheer():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_cheer(), args=())
    o = Thread(target=oled_list.o_cheer, args=())
    m = Thread(target=motion_list.m_cheer(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_compliment():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_compliment(), args=())
    o = Thread(target=oled_list.o_compliment, args=())
    m = Thread(target=motion_list.m_compliment(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_concil():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_concil(), args=())
    o = Thread(target=oled_list.o_concil, args=())
    m = Thread(target=motion_list.m_concil(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_search():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_search(), args=())
    o = Thread(target=oled_list.o_search, args=())
    m = Thread(target=motion_list.m_search(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_sleep():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_sleep(), args=())
    o = Thread(target=oled_list.o_sleep, args=())
    m = Thread(target=motion_list.m_sleep(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_wakeup():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_wakeup(), args=())
    o = Thread(target=oled_list.o_wakeup, args=())
    m = Thread(target=motion_list.m_wakeup(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_agree():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_agree(), args=())
    o = Thread(target=oled_list.o_agree, args=())
    m = Thread(target=motion_list.m_agree(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_deny():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_deny(), args=())
    o = Thread(target=oled_list.o_deny, args=())
    m = Thread(target=motion_list.m_deny(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_joy():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_joy(), args=())
    o = Thread(target=oled_list.o_joy, args=())
    m = Thread(target=motion_list.m_joy(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_angry():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_angry(), args=())
    o = Thread(target=oled_list.o_angry, args=())
    m = Thread(target=motion_list.m_angry(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_sad():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_sad(), args=())
    o = Thread(target=oled_list.o_sad, args=())
    m = Thread(target=motion_list.m_sad(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_tired():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_tired(), args=())
    o = Thread(target=oled_list.o_tired, args=())
    m = Thread(target=motion_list.m_sad(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()

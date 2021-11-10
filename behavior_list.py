
import time
import json
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
motion = Motion()


def do_question():
    # audio.play('/home/pi/openpibo/question.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_question(), args=())
    m = Thread(target=motion.set_motion, args=("m_question", 1))
    o = Thread(target=motion_list.m_question(), args=())

    # e.daemon = True
    o.daemon = True
    m.daemon = True

    # e.start()
    o.start()
    m.start()


def do_suggestion():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_suggestion(), args=())
    m = Thread(target=motion.set_motion, args=("m_suggestion", 1))
    o = Thread(target=oled_list.o_suggestion, args=())


    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()



def do_explain():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_explain(), args=())
    m = Thread(target=motion.set_motion, args=("m_explain", 3))
    o = Thread(target=oled_list.o_explain, args=())


    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()



def do_photo():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_photo(), args=())
    m = Thread(target=motion.set_motion, args=("m_photo", 1))
    o = Thread(target=oled_list.o_photo, args=())


    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_stamp():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_stamp(), args=())
    m = Thread(target=motion.set_motion, args=("m_stamp", 1))
    o = Thread(target=oled_list.o_stamp, args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_waiting():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_waiting(), args=())
    m = Thread(target=motion.set_motion, args=("m_waiting", 3))
    o = Thread(target=oled_list.o_waiting(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_cheer():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_cheer(), args=())
    m = Thread(target=motion.set_motion, args=("m_cheer", 1))
    o = Thread(target=oled_list.o_cheer(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_compliment():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_compliment(), args=())
    m = Thread(target=motion.set_motion, args=("m_compliment", 1))
    o = Thread(target=oled_list.o_compliment, args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_concil():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_concil(), args=())
    m = Thread(target=motion.set_motion, args=("m_concil", 1))
    o = Thread(target=oled_list.o_concil, args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_search():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_search(), args=())
    m = Thread(target=motion.set_motion, args=("m_search", 3))
    o = Thread(target=oled_list.o_search(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_sleep():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_sleep(), args=())
    m = Thread(target=motion.set_motion, args=("m_sleep", 1))
    o = Thread(target=oled_list.o_sleep(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_wakeup():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_wakeup(), args=())
    m = Thread(target=motion.set_motion, args=("m_wakeup", 1))
    o = Thread(target=oled_list.o_wakeup(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_agree():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_agree(), args=())
    m = Thread(target=motion.set_motion, args=("m_agree", 1))
    o = Thread(target=oled_list.o_agree(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_deny():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_deny(), args=())
    m = Thread(target=motion.set_motion, args=("m_deny", 1))
    o = Thread(target=oled_list.o_deny(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_joy():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_joy(), args=())
    m = Thread(target=motion.set_motion, args=("m_joy", 1))
    o = Thread(target=oled_list.o_joy(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_angry():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_angry(), args=())
    m = Thread(target=motion.set_motion, args=("m_angry", 1))
    o = Thread(target=oled_list.o_angry(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_sad():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_sad(), args=())
    m = Thread(target=motion.set_motion, args=("m_sad", 1))
    o = Thread(target=oled_list.o_sad(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()


def do_tired():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # e = Thread(target=eye_list.e_tired(), args=())
    m = Thread(target=motion.set_motion, args=("m_tired", 1))
    o = Thread(target=oled_list.o_tired(), args=())

    # e.daemon = True
    m.daemon = True
    o.daemon = True

    # e.start()
    m.start()
    o.start()

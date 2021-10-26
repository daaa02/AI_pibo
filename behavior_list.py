import time
from threading import Thread

import openpibo
from openpibo.motion import Motion
from openpibo.device import Device
from openpibo.speech import Speech
from openpibo.audio import Audio

import motion_list
import eye_list

audio = Audio()


def do_question():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_question(), args=())
    m = Thread(target=motion_list.m_question(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_suggestion():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_suggestion(), args=())
    m = Thread(target=motion_list.m_suggestion(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_explain():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_explain(), args=())
    print('ccc')
    m = Thread(target=motion_list.m_explain(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_photo():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_photo(), args=())
    m = Thread(target=motion_list.m_photo(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_stamp():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_stamp(), args=())
    m = Thread(target=motion_list.m_stamp(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_waiting():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_waiting(), args=())
    m = Thread(target=motion_list.m_waiting(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_cheer():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_cheer(), args=())
    m = Thread(target=motion_list.m_cheer(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_compliment():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_compliment(), args=())
    m = Thread(target=motion_list.m_compliment(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_concil():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_concil(), args=())
    m = Thread(target=motion_list.m_concil(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_search():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_search(), args=())
    m = Thread(target=motion_list.m_search(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_sleep():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_sleep(), args=())
    m = Thread(target=motion_list.m_sleep(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_wakeup():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_wakeup(), args=())
    m = Thread(target=motion_list.m_wakeup(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_agree():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_agree(), args=())
    m = Thread(target=motion_list.m_agree(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_deny():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_deny(), args=())
    m = Thread(target=motion_list.m_deny(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_joy():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_joy(), args=())
    m = Thread(target=motion_list.m_joy(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_angry():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_angry(), args=())
    m = Thread(target=motion_list.m_angry(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_sad():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_sad(), args=())
    m = Thread(target=motion_list.m_sad(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()


def do_tired():
    print('aaa')
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    e = Thread(target=eye_list.e_tired(), args=())
    m = Thread(target=motion_list.m_sad(), args=())

    e.daemon = True
    m.daemon = True

    e.start()
    m.start()

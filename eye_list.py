from openpibo.device import Device

"""
NEOPIXEL(20) -> ex) #20:255,255,255:!

# 20: 색 변경
# 21: 속도 d(ms)만큼 천천히 변경
# 22: 밝기 조절(기본 64)
# 25: 무지개 눈, d(ms)의 속도로 색 변화

"""

device = Device()


def e_question():
    # '#21:108,209,239,100!'
    device.send_cmd(21, '108,209,239,100')


def e_suggestion():
    # '#21:108,209,239,100!'
    device.send_cmd(21, '108,209,239,100')


def e_explain():
    # '#21:108,209,239,100:!'
    device.send_cmd(21, '108,209,239,100')


def e_photo():
    # '#20:120,230,208:!'
    device.send_cmd(20, '120,230,208')


def e_stamp():
    # '#25:20:!'
    device.send_cmd(25, '20')


def e_waiting():
    # '#21:108,209,239,200:!'
    device.send_cmd(21, '108,209,239,200')


def e_cheer():
    # '#25:10:!'
    device.send_cmd(25, '10')


def e_compliment():
    # '#25:20:!'
    device.send_cmd(25, '20')


def e_concil():
    # '#21:186,147,223,100:!'
    device.send_cmd(21, '186,147,223,100')


def e_search():
    # '#20:108,209,239:!'
    device.send_cmd(20, '108,209,239')


def e_sleep():
    # '#22:0:!'
    device.send_cmd(22, '0')


def e_wakeup():
    # '#20:108,209,239'
    device.send_cmd(20, '108,209,239')


def e_agree():
    # '#21:108,209,239,200:!'
    device.send_cmd(21, '108,209,239,200')


def e_deny():
    # '#21:255,177,190,100:!'
    device.send_cmd(21, '255,177,190,100')


def e_joy():
    # '#25:10:!'
    device.send_cmd(25, '10')


def e_angry():
    # '#21:255,177,190,300:!'
    device.send_cmd(21, '255,177,190,300')


def e_sad():
    # '#21:186,147,223,500:!'
    device.send_cmd(21, '186,147,223,500')


def e_tired():
    # '#21:251,245,155,100:!'
    device.send_cmd(21, '251,245,155,100')

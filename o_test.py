import time
import oled_list


def oled_test():
    time.sleep(2)

    print('init')
    oled_list.o_init()
    time.sleep(5)

    print('question')
    oled_list.o_question()
    time.sleep(5)

    print('suggestion')
    oled_list.o_suggestion()
    time.sleep(2)

    print('explain')
    oled_list.o_explain()
    time.sleep(5)

    print('photo')
    oled_list.o_photo()
    time.sleep(5)

    print('stamp')
    oled_list.o_stamp()
    time.sleep(5)

    print('waiting')
    oled_list.o_waiting()
    time.sleep(5)

    print('cheeeeer')
    oled_list.o_cheer()
    time.sleep(5)

    print('compli')
    oled_list.o_compliment()
    time.sleep(5)

    print('concil')
    oled_list.o_concil()
    time.sleep(5)

    print('search')
    oled_list.o_search()
    time.sleep(5)

    print('sleep')
    oled_list.o_sleep()
    time.sleep(2)

    print('wakeup')
    oled_list.o_wakeup()
    time.sleep(5)

    print('agree')
    oled_list.o_agree()
    time.sleep(5)

    print('deny')
    oled_list.o_deny()
    time.sleep(5)

    print('joy')
    oled_list.o_joy()
    time.sleep(5)

    print('angry')
    oled_list.o_angry()
    time.sleep(5)

    print('sad')
    oled_list.o_sad()
    time.sleep(5)

    print('tired')
    oled_list.o_tired()
    time.sleep(2)

    print('끝')


if __name__ == '__main__':
    oled_test()
    time.sleep(2)

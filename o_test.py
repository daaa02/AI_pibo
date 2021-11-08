import time
import oled_test_test


def oled_test():
    time.sleep(2)

    print('init')
    oled_test_test.o_init()
    time.sleep(2)

    print('question')
    oled_test_test.o_question()
    time.sleep(2)

    print('suggestion')
    oled_test_test.o_suggestion()
    time.sleep(2)

    print('explain')
    oled_test_test.o_explain()
    time.sleep(2)

    print('photo')
    oled_test_test.o_photo()
    time.sleep(2)

    print('stamp')
    oled_test_test.o_stamp()
    time.sleep(2)

    print('waiting')
    oled_test_test.o_waiting()
    time.sleep(2)

    print('cheeeeer')
    oled_test_test.o_cheer()
    time.sleep(2)

    print('compli')
    oled_test_test.o_compliment()
    time.sleep(2)

    print('concil')
    oled_test_test.o_concil()
    time.sleep(2)

    print('search')
    oled_test_test.o_search()
    time.sleep(2)

    print('sleep')
    oled_test_test.o_sleep()
    time.sleep(2)

    print('wakeup')
    oled_test_test.o_wakeup()
    time.sleep(2)

    print('agree')
    oled_test_test.o_agree()
    time.sleep(2)

    print('deny')
    oled_test_test.o_deny()
    time.sleep(2)

    print('joy')
    oled_test_test.o_joy()
    time.sleep(2)

    print('angry')
    oled_test_test.o_angry()
    time.sleep(2)

    print('sad')
    oled_test_test.o_sad()
    time.sleep(2)

    print('tired')
    oled_test_test.o_tired()
    time.sleep(2)

    print('끝')


if __name__ == '__main__':
    oled_test()
    time.sleep(2)

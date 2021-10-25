from openpibo.device import Device

class Eye_list:
    {
        """
        NEOPIXEL(20) -> ex) #20:255,255,255:!
    
        # 20: 색 변경
        # 21: 속도 d(ms)만큼 천천히 변경
        # 22: 밝기 조절(기본 64)
        # 25: 무지개 눈, d(ms)의 속도로 색 변화
    
        """

        def e_question():
            color = '#21:108,209,239,100:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_suggestion():
            color = '#21:108,209,239,100:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_explain():
            color = '#21:108,209,239,100:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_photo():
            color = '#20:120,230,208:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_stamp():
            color = '#25:20:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_waiting():
            color = '#21:108,209,239,200:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_cheer():
            color = '#25:10:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_compliment():
            color = '#25:20:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_concil():
            color = '#21:186,147,223,100:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_search():
            color = '#20:108,209,239:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_sleep():
            color = '#22:0:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_wakeup():
            color = '#20:108,209,239'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def agree():
            color = '#21:108,209,239,200:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_deny():
            color = '#21:255,177,190,100:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_joy():
            color = '#25:10:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_angry():
            color = '#21:255,177,190,300:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_sad():
            color = '#21:186,147,223,500:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

        def e_tired():
            color = '#21:251,245,155,100:!'
            obj = Device()
            data = obj.send_raw(color)

            print("send: ", color)
            print("receive: ", data)

    }





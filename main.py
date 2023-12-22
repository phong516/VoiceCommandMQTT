from mqtt import MQTT
from CommandCommunication import CommandCommunication

class main(MQTT):
    def __init__(self):
        super().__init__(client_id = "raspberypi")
        self.set_credentials(username = "raspberrypi", password = "Raspberrypi123456")
        self.set_callback(on_connect = True, on_message = True, on_publish = True)
        self.connect()
        self.subscribe(topic = "user0/test", qos = 1)
        self.uart = CommandCommunication()
        self.loop_start()
        
        # if msg == "Dừng":
        #     self.uart.write(b'0')  
        # elif msg == "Tiến":
        #     self.uart.write(b'1')
        # elif msg == "Lùi":
        #     self.uart.write(b'2')
        # elif msg == "Trái":
        #     self.uart.write(b'3')
        # elif msg == "Phải":
        #     self.uart.write(b'4')
        # elif msg == "Chậm":
        #     self.uart.write(b'5')
        # elif msg == "Nhanh":
        #     self.uart.write(b'6')  

if __name__ == '__main__':
    test = main()
    while True:
        if test.msg == "":
            continue
        if test.msg == "Dừng":
            test.uart.write(b'0')  
        elif test.msg == "Tiến":
            test.uart.write(b'1')
        elif test.msg == "Lùi":
            test.uart.write(b'2')
        elif test.msg == "Trái":
            test.uart.write(b'3')
        elif test.msg == "Phải":
            test.uart.write(b'4')
        elif test.msg == "Chậm":
            test.uart.write(b'5')
        elif test.msg == "Nhanh":
            test.uart.write(b'6')  
        test.msg = ""
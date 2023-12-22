import serial 

class CommandCommunication:
    def __init__(self, port = '/dev/ttyUSB0', baudrate = 115200, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1):
        self.serial = serial.Serial(port = port, 
                                    baudrate = baudrate,
                                    parity = parity,
                                    stopbits = stopbits,
                                    bytesize = bytesize,
                                    timeout = timeout
                                    )
        
    def write(self, data):
        self.serial.write(data)
        self.serial.flush()
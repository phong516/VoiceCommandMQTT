from PyQt5.QtWidgets import (QApplication)
import VoiceCommand as vc
from gui import Window
from mqtt import MQTT

class main(Window):
    def __init__(self):
        super().__init__()
        self.ai = vc.VoiceComamnd('saved_model_73')
        self.mqtt_user = MQTT(client_id = "user0")
        self.mqtt_user.set_credentials(username = "user0", password = "User0123456")
        self.mqtt_user.set_callback(on_connect = True, on_message = True, on_publish = True)
        self.mqtt_user.connect()
        self.mqtt_user.loop_start()
    
    def slot_PredictMic(self):
        self.Command = self.ai.PredictMic()
        self.textEdit.setText(self.Command)

    def slot_Publish(self):
        self.mqtt_user.publish(topic="user0/test", payload=self.Command, qos=1)
        self.textEdit.setText("Published: " + self.Command)
        
if __name__ == '__main__':
    app = QApplication([])
    window = main()
    window.show()
    app.exec_()
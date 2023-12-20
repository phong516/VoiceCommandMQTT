import VoiceCommand as vc
import mqtt
import GUI_test

class main():
    def __init__(self):
        #Khởi tạo MQTT
        self.mqtt_user = mqtt.MQTT(client_id = "user0")
        self.mqtt_user.set_credentials(username = "user0", password = "User0123456")
        self.mqtt_user.set_callback(on_connect = True, on_message = True, on_publish = True)
        self.mqtt_user.connect()
        self.mqtt_user.loop_start()

        #Khởi taọ AI
        self.ai = vc.VoiceComamnd('saved_model')
        self.Command = None
    
        #Khởi tạo GUI
        self.gui = GUI_test.Ui_MainWindow()
        self.gui.setup()
        self.gui.setButtonEvent(self.gui.pushButton, self.PredictEvent)
        self.gui.setButtonEvent(self.gui.pushButton_2, self.PublishCommand)
        self.gui.show()

    def PredictEvent(self):
        self.Command = self.ai.PredictMic()
        self.gui.displayText(self.Command)

    def PublishCommand(self, command : str = None):
        if command == None:
            command = self.Command
        self.mqtt_user.publish(topic = "user0/test", payload = command, qos = 1)


if __name__ == "__main__":
    main()
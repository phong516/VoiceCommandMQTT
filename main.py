import VoiceCommand as vc
import mqtt

#Khởi tạo phần nhận lệnh bằng giọng nói
ai = vc.VoiceComamnd('saved_model')

#Khởi tạo phần gửi lệnh điều khiển qua MQTT
mqtt_user = mqtt.MQTT(client_id = "user0")
mqtt_user.set_credentials(username = "user0", password = "User0123456")
mqtt_user.set_callback(on_connect = True, on_message = True, on_publish = True)
mqtt_user.connect()
mqtt_user.loop_start()

while True:
    input("Press Enter to send command")
    command = ai.PredictMic()
    mqtt_user.publish(topic="user0/test", payload=command, qos=1)

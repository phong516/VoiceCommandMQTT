import mqtt
import keyboard

pub_test = mqtt.MQTT(client_id = "user0")
pub_test.set_credentials(permission = mqtt.Permission.Pub, username = "user0", password = "User0123456")
pub_test.set_callback()
pub_test.connect()
pub_test.loop_start()

while True:
    pub_test.publish(topic="user0/test", payload="Go", qos=1)
import mqtt
import time

sub_test = mqtt.MQTT(client_id = "pi")
sub_test.set_credentials(username="raspberrypi", password="Raspberrypi123456")
sub_test.set_callback()
sub_test.connect()
sub_test.subscribe(topic="user0/test", qos=1)
sub_test.loop_forever()

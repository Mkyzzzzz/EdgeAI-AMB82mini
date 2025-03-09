import paho.mqtt.subscribe as subscribe

host = "test.mosquitto.org"

msg = subscribe.simple("ntou/edgeai/01072114/[robot1", hostname=host)
print("topic  : %s" % (msg.topic))
print()
print("payload:To turn around continuously, my motor will move like this:")
print("%s" % (msg.payload.decode("utf-8")))
print()

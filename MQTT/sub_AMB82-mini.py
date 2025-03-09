import paho.mqtt.subscribe as subscribe

host = "test.mosquitto.org"

msg = subscribe.simple("ntou/01072114/edgeai/robot1", hostname=host)
print("topic  : %s" % (msg.topic))
print()
print("payload:")
print("%s" % (msg.payload.decode("utf-8")))
print()

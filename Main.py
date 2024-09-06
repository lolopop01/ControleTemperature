import time
import paho.mqtt.client as mqtt

# Configuration de MQTT
broker = "10.4.1.202"
port = 1883
temperature_topic = "paho/Zach/Temp"
humidity_topic = "paho/Zach/Humidity"


def on_connect(client, userdata, flags, rc):
    print("Connecté avec le code : " + str(rc))
    # Abonnement aux topics
    client.subscribe(temperature_topic, qos=0)
    client.subscribe(humidity_topic, qos=0)


def on_message(client, userdata, msg):
    # Traitement des messages reçus
    if msg.topic == temperature_topic:
        print(f"Température reçue : {msg.payload.decode()}")
    elif msg.topic == humidity_topic:
        print(f"Humidité reçue : {msg.payload.decode()}")


client = mqtt.Client()  # Create a new instance of the MQTT client
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_start()

try:
    while True:
        time.sleep(1)  # Attendre en attendant les messages
except KeyboardInterrupt:
    print("Interruption par l'utilisateur")
finally:
    client.loop_stop()
    client.disconnect()

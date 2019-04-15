import time
import eventlet
eventlet.monkey_patch()
import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from flask_bootstrap import Bootstrap

# from flask_mqtt import Mqtt
# turn the flask app into a socketio app

new_template_folder = 'web/templates'
new_static_folder = 'web/static'

app = Flask(__name__, static_folder=new_static_folder, template_folder=new_template_folder)
# app.config['SECRET'] = 'SECRET!' 
# app.config['MQTT_CLIENT_ID'] = 'Pi_Flask'
# app.config['MQTT_BROKER_URL'] = '192.168.1.163'
# app.config['MQTT_BROKER_PORT'] = 1883
# app.config['MQTT_USERNAME'] = 'pi'
# app.config['MQTT__PASSWORD'] = '2504'
# app.config['MQTT_TLS_ENABLED'] = False

mqtt_username = "pi"
mqtt_password = "2504" 
mqtt_topic = "/R1D1/temperature"
mqtt_broker_ip = "192.168.1.163"
MQTT_CLIENT_ID = 'Pi_Flask'
MQTT_BROKER_PORT = 1883
timeout_reconnect = 60
# async_mode = "eventlet"

socketio = SocketIO(app)
bootstrap = Bootstrap(app)

# mqtt = Mqtt(app)

# @mqtt.on_connect()
# def handle_connect(client, userdata, flags, rc):
    # mqtt.subscribe('Temp_DHT')

# The callback for when the client receives a CONNACK response from the server.
# These functions handle what happens when the MQTT client connects
# to the broker, and what happens then the topic receives a message


def on_connect(client, userdata, flags, rc):
    # rc is the error code returned when connecting to the broker
    # print("Connected with result code "+str(rc))
    # if int(str(rc)) == 0:
        # print("Connection established")
        # print (" ")
    # else:
        # print("Error result code: " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # Once the client has connected to the broker, subscribe to the topic
    mqttClient.subscribe(mqtt_topic)


def on_message(client, userdata, message):
    # This function is called everytime the topic is published to.
    # If you want to check each message, and do something depending on
    # the content, the code to do this should be run in this function
    # socketio.emit('my variable')
    print("Received message '" +
          str(message.payload.decode()) +
          "' on topic '" +
          message.topic +
          "' with QoS '" +
          str(message.qos))
    # The message itself is stored in the msg variable
    # and details about who sent it are stored in userdata
    if message.topic == mqtt_topic:
        print("temperature update")
        socketio.emit('dht_temperature', {'temp': message.payload.decode()})


mqttClient = mqtt.Client(MQTT_CLIENT_ID)
# Set the username and password for the MQTT client
mqttClient.username_pw_set(mqtt_username, mqtt_password)
# Here, we are telling the client which functions are to be run
# on connecting, and on receiving a message
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
# Once everything has been set up, we can (finally) connect to the broker
# 1883 is the listener port that the MQTT broker is using
mqttClient.connect(mqtt_broker_ip,
                   MQTT_BROKER_PORT,
                   timeout_reconnect)
# Once we have told the client to connect, let the client object run itself
mqttClient.loop_start()

print("publishing ")
mqttClient.publish(mqtt_topic, "on")  # publish
# time.sleep(4)
# mqttClient.disconnect() #disconnect
# mqttClient.loop_stop() #stop loop
# mqttClient.loop_forever()
# mqttClient.disconnect()




@app.route('/')
def index():
    my_list = ['apples', 'oranges', 'grapes', 'pineapples']
    return render_template('index.html',
                           async_mode=socketio.async_mode,
                           my_list=my_list)

@app.route('/meow')
def meow():
    return 'MEOW.'

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
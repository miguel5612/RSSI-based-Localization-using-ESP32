"""
Contains code for MQTT subscriber thread
"""

import json
import paho.mqtt.client as paho

import const

def rssi_callback(client, userdata, message):
	m = str(message.payload.decode("utf-8")).rstrip('\n').replace('\'','\"')
	data = json.loads(m)

	anchor_mac = message.topic.split('/')[2]
	device_mac, rssi = data['MAC'], data['RSSI']

	print("callback from: ", device_mac)
	print("anchor_mac: ", anchor_mac)

	## Filtering out Target nodes
	if device_mac == "5C:5F:67:6A:E4:A6" or device_mac == "A4:50:46:52:F5:67":
		print("Data: ",anchor_mac, *data.items())
	const.data_queue.put((anchor_mac, device_mac, rssi))

def csi_callback(client, userdata, message):
	m = str(message.payload.decode("utf-8")).rstrip('\n').replace('\'','\"')
	data = json.loads(m)
	print(*data.items())

def on_connect(client, userdata, flags, rc):	
	rssi_topic, csi_topic = "/rssi/#", "/csi/#"
	client.subscribe(rssi_topic)
	client.subscribe(csi_topic)

	client.message_callback_add(rssi_topic, rssi_callback)
	client.message_callback_add(csi_topic, csi_callback)
	print("Conectado!")

def connect(broker_ip, broker_port):
	client= paho.Client("Localization listener") 
	client.on_connect = on_connect

	client.connect(broker_ip,broker_port)

	client.loop_forever()

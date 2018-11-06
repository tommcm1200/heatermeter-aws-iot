'''
/*
 * Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json
from sseclient import SSEClient
from ConfigParser import SafeConfigParser

AllowedActions = ['both', 'publish', 'subscribe']

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

############################################################
### Configuration Parse ###
parser = SafeConfigParser()

parser.read('heatermeter_IoT_Connector.ini')
print("\n")
print ("Configuration:")
print ("\taws_iot_endpoint: %s" % parser.get('DEFAULT', 'aws_iot_endpoint'))
print ("\troot_ca_cert_path: %s" % parser.get('DEFAULT', 'root_ca_cert_path'))
print ("\tcert_path: %s" % parser.get('DEFAULT', 'cert_path'))
print ("\tprivate_key_path: %s" % parser.get('DEFAULT', 'private_key_path'))
print ("\theatermeter_sse_url: %s" % parser.get('DEFAULT', 'heatermeter_sse_url'))
print ("\theatermeter_macaddress: %s" % parser.get('DEFAULT', 'heatermeter_macaddress'))
print ("\tsample_event_file_path: %s" % parser.get('DEFAULT', 'sample_event_file_path'))
print ("\twebsocket_port: %s" % parser.get('DEFAULT', 'websocket_port'))
print ("\tclient_id: %s" % parser.get('DEFAULT', 'client_id'))
print("\n")

config = {}
config['aws_iot_endpoint'] = parser.get('DEFAULT', 'aws_iot_endpoint')
config['root_ca_cert_path'] = parser.get('DEFAULT', 'root_ca_cert_path')
config['cert_path'] = parser.get('DEFAULT', 'cert_path')
config['private_key_path'] = parser.get('DEFAULT', 'private_key_path')
config['heatermeter_sse_url'] = parser.get('DEFAULT', 'heatermeter_sse_url')
config['heatermeter_macaddress'] = parser.get('DEFAULT', 'heatermeter_macaddress')
config['websocket_port'] = parser.get('DEFAULT', 'websocket_port')
config['client_id'] = parser.get('DEFAULT', 'client_id')

host = config['aws_iot_endpoint']
rootCAPath = config['root_ca_cert_path']
certificatePath = config['cert_path']
privateKeyPath = config['private_key_path']
sseURL = config['heatermeter_sse_url']
topic = "heatermeter/%s" % config['heatermeter_macaddress']
# sampleEventFilePath =  config['sample_event_file_path']
clientId = config['client_id']
port = config['websocket_port']
port = int(config['websocket_port'])

############################################################

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
# logger.setLevel(logging.DEBUG)
logger.setLevel(logging.ERROR)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myAWSIoTMQTTClient.connect()
# myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)

if config['heatermeter_sse_url']:
    sseMessages = SSEClient(config['heatermeter_sse_url'])
    for sseMsg in sseMessages:
        myAWSIoTMQTTClient.publish(topic, sseMsg.data, 1)
        print('Published topic %s: %s\n' % (topic, sseMsg.data))

# # Publish to the same topic in a loop forever
# if args.sampleEventFile:
#     with open(sampleEventFile) as f:
#         sampleEventData = json.load(f)
#         # print(sampleEventData)
#         loopCount = 0
#         while True:
#             if args.mode == 'both' or args.mode == 'publish':
#                 message = {}
#                 message = sampleEventData
#                 messageJson = json.dumps(message)
#                 myAWSIoTMQTTClient.publish(topic, messageJson, 1)
#                 print('Published topic %s: %s\n' % (topic, messageJson))
#                 loopCount += 1
#             time.sleep(1)

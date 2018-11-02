from sseclient import SSEClient
import json 

messages = SSEClient('http://192.168.1.37/luci/lm/stream/')
for msg in messages:
    # print(msg)
    print(json.loads(msg.data))
    print(json.dumps(msg.data))

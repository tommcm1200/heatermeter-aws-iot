from sseclient import SSEClient

messages = SSEClient('http://192.168.1.37/luci/lm/stream/')
for msg in messages:
    print(msg)
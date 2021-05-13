import argparse
import stomp
import time

# Commadline option
parse = argparse.ArgumentParser()
parse.add_argument('--amq_host', default='localhost')
parse.add_argument('--amq_port', default='61613')
parse.add_argument('--sub_topic', required=True)
parse.add_argument('--pub_topic', required=True)
parse.add_argument('--pub_message', required=True)
parse.add_argument('--wav', action='store_true')
args = parse.parse_args()

# Global variables
AMQ_HOST = args.amq_host
AMQ_PORT = args.amq_port
SUB_TOPIC = f'/topic/{args.sub_topic}'
PUB_TOPIC = f'/topic/{args.pub_topic}'
PUB_MESSAGE = args.pub_message
WAV = args.wav

class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_message(self, frame):
        if WAV:
            with open('subscribed.wav', 'wb') as f:
                f.write(frame.body)
        else:
            print('received a message "%s"' % frame.body.decode('utf-8'))

conn = stomp.Connection([(AMQ_HOST, AMQ_PORT)], auto_decode=False)
conn.set_listener('', MyListener())
conn.connect(wait=True)
conn.subscribe(destination=SUB_TOPIC, id=1)
conn.send(body=PUB_MESSAGE, destination=PUB_TOPIC)
time.sleep(3)
conn.disconnect()


from flask import Flask, render_template, request
import json
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET'] = 'my secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'big.forcebing.top'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 60
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_LAST_WILL_TOPIC'] = '/last/will'
app.config['MQTT_LAST_WILL_MESSAGE'] = 'bye'
app.config['MQTT_LAST_WILL_QOS'] = 2

mqtt_ws = Mqtt(app)
socketio = SocketIO(app, cors_allowed_origins="*")
# 只有我们提前写了订阅的消息，才会收到消息
mqtt_ws.subscribe('test')


@app.route('/')
def hello_world():
    return 'hello wrold '


@app.route('/ws')
def wevsocket():
    return render_template('websocket_mqtt_demo.html')


@socketio.on('publish', namespace='/test')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt_ws.publish(data['topic'], data['message'])


@socketio.on('subscribe', namespace='/test')
def handle_subscribe(json_str):
    print('get subscribe  message ')
    data = json.loads(json_str)
    mqtt_ws.subscribe(data['topic'])


@socketio.on('connect', namespace='/test')
def handel_connect():
    print('get conncet ')


@mqtt_ws.on_message()
def handle_mqtt_message(client, userdata, message):
    print('get message from server')
    print(message.topic)
    print(message.payload)
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    socketio.emit('mqtt_message', data=data)
    # socketio.emit(message.topic, message.payload.decode)


@mqtt_ws.on_log()
def handle_logging(client, userdata, level, buf):
    print(client, userdata, level, buf)
    print('get log ')


if __name__ == '__main__':
    CORS(app, supports_credentials=True, resources=r'/*')
    socketio.run(app, host='127.0.0.1', port=8083, use_reloader=True, debug=True)

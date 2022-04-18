from flask import *
import json, time
from pynput.keyboard import *
import platform

app = Flask(__name__)


def tapAll(result, keyboard):
    for i in result:
        keyboard.tap(i)


@app.route('/request/', methods=['GET'])
def home_page():
    user_query = request.args.get("connect")
    print("> Connected to " + user_query + " Time :" + time.time())
    data_set = {'Page': 'Home', 'Message': 'Connect to ' + platform.platform(), 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/img/')
def get_image():
    if request.args.get('type') == '1':
       filename = 'img.jpg'
    else:
       filename = 'img.jpg'
    return send_file(filename, mimetype='image/gif')

@app.route('/users/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('query'))  # /user/?query=User_Name
    result = str(user_query)
    data_set = {'Page': 'Request', 'Message': f'{result} ', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    # webbrowser.open(result)

    keyboard = Controller()
    tapAll(result, keyboard)

    return json_dump


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=7777)

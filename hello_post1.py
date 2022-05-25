from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def root():
    str = 'Welcome to flask ! <br/> <a href=\'/send_post2\' />post test </a>'
    return str#'Welcome to flask !'

@app.route('/handle_post', methods=['POST'])
def handle_post():
    params = json.loads(request.get_data(), encoding='utf-8')
    if len(params) == 0:
        return 'No parameter'

    params_str = ''
    for key in params.keys():
        params_str += 'key: {}, value: {}<br>'.format(key, params[key])
    return params_str


@app.route('/send_post', methods=['GET'])
def send_post():
    params = {
        "param1": "test",
        "param2": 123,
        "param3": "한글"
    }
    res = requests.post("http://127.0.0.1:81/handle_post", data=json.dumps(params))
    return res.text


@app.route('/send_post2', methods=['GET'])
def send_post2():
    # https://www.w3schools.com/python/ref_requests_post.asp
    myobj = {'somekey': 'somevalue'}

    url = "http://127.0.0.1:81/handle_post"
    res = requests.post(url, data = json.dumps(myobj))

    #res = requests.post(url, data=json.dumps(params))
    return res.text



if __name__ == '__main__':
    app.debug = True
    #app.run()
    app.run(host='0.0.0.0', port=81)
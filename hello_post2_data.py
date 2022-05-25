from flask import Flask, request
import json
import requests
from loaddata import *
import numpy as np
import time
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
    global model, t1
    
    
    #fn_pickle = './pickle/08_walking_wearable21_20210823_class18_len150_pub.pickle'
    fn_pickle = './pickle/08_walking_wearable21_20210823_class18_len100_pub.pickle'

    len_data, data_test, labels_test, feature_name = loadpicklked(fn_pickle)

    
    
    n_layers = len(model.layers)
    
    idx_to_draw = np.random.randint(0, data_test.shape[0] - 1)
    #idx_to_draw = 14065

    X = data_test[idx_to_draw]
    #x0 = np.expand_dims( testX[0], 0)
    X = np.expand_dims( X, 0)
    y = labels_test[idx_to_draw]
    y_argmax = np.argmax(y, axis=0)
    t0 = time.time()
    y_pred = model.predict(X)[0]
    dt_pred = time.time() - t0

    y_pred_argmax = np.argmax(y_pred, axis =0)
    y_pred_proba = y_pred[y_pred_argmax]

    # https://www.w3schools.com/python/ref_requests_post.asp

    if True:
        myobj = {'n_layers':n_layers, 
                'dt_load':'{:.3f}'.format(t1),
                'dt_pred':'{:.3f}'.format(dt_pred),
                'x_idx':str(idx_to_draw),
                'xshape':np.shape(X), 
                'y':y.tolist(), 
                'y_pred':y_pred.tolist(), 
                
                'y_argmax': str(y_argmax),
                'y_pred_argmax':str(y_pred_argmax),
                'y_pred_proba': '{:.3f}'.format(y_pred_proba)
                }
    else:
        myobj = {'n_layers':n_layers, 
                'len_data': len_data, 
                'feature_name': feature_name.tolist(),
                'X': X.tolist(),
                'y': y.tolist()
                
                }

    url = "http://127.0.0.1:81/handle_post"
    res = requests.post(url, data = json.dumps(myobj))

    #res = requests.post(url, data=json.dumps(params))
    return res.text

from tensorflow.keras.models import load_model


def setup_app(app):
    global model, t1
   # All your initialization code
    t0 = time.time()
    fn_model = './models/08_walking_wearable21_20210823/model_08_walking_wearable21_20210823_Conv1D_SMPL56500_EP240'
    model = load_model(fn_model)
    t1 = time.time()-t0

setup_app(app)

if __name__ == '__main__':
    
    app.debug = False#True
    
    #app.run()
    
    

    app.run(host='0.0.0.0', port=81)
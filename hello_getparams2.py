from flask import Flask, request
import numbers

app = Flask(__name__)

def calc(v1):
    v1f = float(v1)

    return v1f*v1f

@app.route('/')
def root():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return 'No parameter'

    ret = ''
    for key in parameter_dict.keys():
        if key=='num1':
            
           vout = calc(request.args[key])
           ret += '{} --> {}<br/>'.format(request.args[key], vout)
        else:
           ret += 'key: {}, value: {}<br/>'.format(key, request.args[key])

    return ret 


app.run(host='0.0.0.0', port=81)

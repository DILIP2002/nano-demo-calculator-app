from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!',200

@app.route("/calculator/add", methods=['POST'])
def add():
    data=request.json
    fn = data.get('firstNumber',0)
    sn = data.get('secondNumber',0) 
    return fn+sn,200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    fn = data.get('firstNumber',0)
    sn = data.get('secondNumber',0)
    return jsonify({fn-sn}),200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')

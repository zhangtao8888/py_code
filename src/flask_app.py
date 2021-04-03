from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index(name = None):
    if request.method == 'GET':
        name = "ADSDS WEB SERVER"
        return jsonify({"status":"success"})

if __name__ == '__main__' :
    try:
        app.run(host='0.0.0.0',port = 80 ,debug = True)
    except:
        pass
from flask import Flask,jsonify,request,Blueprint
from redund.sim_service import sim_route

app = Flask(__name__)

app.register_blueprint(sim_route)
# @app.route('/',methods=['GET'])
# def index(name = None):
#     if request.method == 'GET':
#         name = "ADSDS WEB SERVER"
#         return jsonify({"status":"success"})

if __name__ == '__main__' :
    try:
        app.run(host='0.0.0.0',port = 8080 ,debug = True)
    except:
        pass
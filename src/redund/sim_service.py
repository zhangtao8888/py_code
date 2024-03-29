from flask import Blueprint,jsonify
from redund.sim_dao import sim_dao

sim_route = Blueprint('admin',__name__)
dao = sim_dao()
@sim_route.route('/sim')
def sim_sample():
    df = dao.p_report()
    # status = "success sim"
    return df.to_json()

@sim_route.route('/exe',methods =['POST'])
def sim_exe():
    dao.p_exe()
    return jsonify({"status insert records":"c.to_char"})

@sim_route.route('/json_key',methods = ['POST'])
def json_key():
    dao.p_json()
    return jsonify({"json process":"success"})
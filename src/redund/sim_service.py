from flask import Blueprint,jsonify
from redund.sim_dao import sim_dao

sim_route = Blueprint('admin',__name__)
dao = sim_dao()
@sim_route.route('/sim')
def sim_sample():
    dao.p_report()
    status = "success sim"
    return jsonify({"status":status})

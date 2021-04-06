from flask import Blueprint,jsonify
from redund.sim_dao import sim_dao

sim_route = Blueprint('admin',__name__)
dao = sim_dao()
@sim_route.route('/sim')
def sim_sample():
    df = dao.p_report()
    # status = "success sim"
    return df.to_json()

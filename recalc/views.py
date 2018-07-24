from flask import Blueprint

from recalc.api import DemoAPI

recalc_app = Blueprint('recalc_app', __name__)
recalc_view = DemoAPI.as_view('recalc_api')

recalc_app.add_url_rule('/recalc/', view_func=recalc_view, methods=['POST', 'GET'])

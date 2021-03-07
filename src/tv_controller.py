from flask import Blueprint
from api.remoclient import NatureRemoClient

tv_controller = Blueprint('tv_controller', __name__, url_prefix='/tv/api')


@tv_controller.route('/send/<appliance_id>/<button_name>', methods=['POST'])
def send_tv(appliance_id,button_name):
    nclient = NatureRemoClient()
    result = nclient.send_tv(appliance_id=appliance_id,button=button_name)
    return result
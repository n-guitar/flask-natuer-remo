from flask import Blueprint
from api.remoclient import NatureRemoClient

other_controller = Blueprint('other_controller', __name__, url_prefix='/other/api')


@other_controller.route('/send_signal/<signal_id>', methods=['POST'])
def send_signal(signal_id):
    nclient = NatureRemoClient()
    result = nclient.send_signal(signal_id=signal_id)
    return result
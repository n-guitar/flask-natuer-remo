from flask import Blueprint

from api.json_dataclient import AppliancesDataClient
from api.remoclient import NatureRemoClient

air_controller = Blueprint('air_controller', __name__, url_prefix='/air/api')


@air_controller.route('/send/power/<appliance_id>/<signal>', methods=['POST'])
def send_power(appliance_id,signal):
    nclient = NatureRemoClient()
    if signal == "power-on":
        signal = ""
    result = nclient.send_aircon_settings(appliance_id=appliance_id,button=signal)
    return result

@air_controller.route('/send/temp/<appliance_id>/<signal>', methods=['POST'])
def send_temp(appliance_id,signal):
    nclient = NatureRemoClient()
    result = nclient.send_aircon_settings(appliance_id=appliance_id,temperature=signal)
    # update json data
    appliances_client = AppliancesDataClient()
    appliances_client.json_load()
    appliances_client.appliances_json_update_air_temp(appliance_id=appliance_id, temperature=signal)
    return result

@air_controller.route('/send/mode/<appliance_id>/<signal>', methods=['POST'])
def send_mode(appliance_id,signal):
    nclient = NatureRemoClient()
    signal = signal[5:]
    result = nclient.send_aircon_settings(appliance_id=appliance_id,operation_mode=signal)
    return result

@air_controller.route('/send/vol/<appliance_id>/<signal>', methods=['POST'])
def send_vol(appliance_id,signal):
    nclient = NatureRemoClient()
    signal = signal[4:]
    result = nclient.send_aircon_settings(appliance_id=appliance_id,air_volume=signal)
    return result

@air_controller.route('/send/dir/<appliance_id>/<signal>', methods=['POST'])
def send_dir(appliance_id,signal):
    nclient = NatureRemoClient()
    signal = signal[4:]
    result = nclient.send_aircon_settings(appliance_id=appliance_id,air_direction=signal)
    return result

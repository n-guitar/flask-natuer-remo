import os
import requests
import json


class NatureRemoClient(object):
    def __init__(self, base_url=None):
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = 'https://api.nature.global'
        token = os.environ.get('REMO_TOKEN')
        if not token:
            raise Exception('Please set your API token to REMO_TOKEN')
        self.headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }

    def call_api(self, url, method='get', params=None):
        req_method = getattr(requests, method)
        try:
            res = req_method(self.base_url+url,
                             headers=self.headers,
                             params=params)
            return res.json()
        except Exception as e:
            raise Exception('Failed to call API: %s' % str(e))

    def get_user(self):
        url = '/1/users/me'
        return self.call_api(url)

    def get_devices(self):
        url = '/1/devices'
        return self.call_api(url)

    def get_appliances(self):
        url = '/1/appliances'
        return self.call_api(url)

    def get_signals(self, appliance_id):
        url = '/1/appliances/' + appliance_id + '/signals'
        return self.call_api(url)

    def send_signal(self, signal_id):
        url = '/1/signals/' + signal_id + '/send'
        return self.call_api(url, method='post')

    def send_aircon_settings(self, appliance_id, temperature=None, operation_mode=None, air_volume=None, air_direction=None, button=None):
        url = '/1/appliances/' + appliance_id + '/aircon_settings'
        print(url)
        params = {
            "temperature": temperature,
            "operation_mode": operation_mode,
            "air_volume": air_volume,
            "air_direction": air_direction,
            "button": button
        }
        print(params)
        return self.call_api(url, method='post', params=params)

    def send_tv(self, appliance_id, button):
        url = '/1/appliances/' + appliance_id + '/tv'
        print(url)
        params = {
            "button": button
        }
        print(params)
        return self.call_api(url, method='post', params=params)

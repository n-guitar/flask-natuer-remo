import json

from api.remoclient import NatureRemoClient


class AppliancesDataClient(object):
    """
    save & load json
    json parse
    """

    def __init__(self, file_path=None):
        # json set
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = "./remo_data/appliances.json"
        self.json_data = None

    def json_save(self):
        nclient = NatureRemoClient()
        appliances = nclient.get_appliances()
        try:
            with open(self.file_path, 'w') as outfile:
                json.dump(appliances, outfile, indent=4, ensure_ascii=False)
        except Exception as e:
            self.init_error = e

    def json_load(self):
        try:
            with open(self.file_path, "r") as json_file:
                self.json_data = json.load(json_file)
        except Exception as e:
            self.init_error = e

    def appliances_get_all(self):
        if self.json_data:
            return self.json_data
        else:
            return self.init_error

    def appliances_get_air(self, air_id=None):
        self.json_load() # load json, because update temperature
        if self.json_data:
            appliances_list = []
            for data in self.json_data:
                if data['type'] == "AC":
                    appliances_list.append(data)
            return appliances_list
        else:
            return self.init_error

    def appliances_json_update_air_temp(self, appliance_id, temperature):
        update_index = 0
        for i, appliance in enumerate(self.json_data):
            if appliance['id'] == appliance_id:
                update_index = i
        self.json_data[update_index]['settings']['temp'] = str(temperature)
        with open(self.file_path, 'w') as outfile:
            json.dump(self.json_data, outfile, indent=4, ensure_ascii=False)

    def appliances_get_other(self):
        if self.json_data:
            appliances_list = []
            for data in self.json_data:
                if data['type'] == "IR":
                    appliances_list.append(data)
            return appliances_list
        else:
            return self.init_error

    def appliances_get_tv(self):
        if self.json_data:
            appliances_list = []
            for data in self.json_data:
                if data['type'] == "TV":
                    appliances_list.append(data)
            return appliances_list
        else:
            return self.init_error

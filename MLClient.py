import requests, sys, time, json

class MLClient:
	"""This is a object for an ML Client"""
	def __init__(self, host='localhost', port='5000'):
		self.client_id = client_id
		self.client_key = client_key
		self.host = host
		self.port = port
		self.header = {'Content-Type' : 'application/json'}
		self.url = '%s%s:%s' % ('http://', self.host, self.port);

	def create_virtual_sensor(name, desc, inputs):
		url = '%s/%s' % (self.url, 'sensor');
		payload = 
		{
                "name":name,
                "description":description,
                "labels":[],
                "user_id":"default",
                "sensor_uuid":"",
                "inputs":inputs,
                "training_set":[]
        }

        response = requests.post(url, headers=self.header, data=json.dumps(payload), verify=False).json();
        return response['ret'];

    def get_time(self):
    	url = '%s/%s' % (self.url, 'time');
    	return requests.get(url, headers=self.header).json()['ret'];

    def add_sample(self, virtual_sensor_id, start_time, end_time, label):
    	url = '%s/%s/%s/%s' % (self.url, 'sensor', virtual_sensor_id, 'sample');
		payload = 
		{
                "start_time":float(start_time),
                "end_time":float(end_time),
                "label":label,
        }

        response = requests.post(url, headers=self.header, data=json.dumps(payload), verify=False).json();
        return response['result'];

    def train_virtual_sensor(self, virtual_sensor_id):
    	url = '%s/%s/%s/%s/%s' % (self.url, 'sensor', virtual_sensor_id, 'classifier', 'train');
    	response = requests.post(url, headers=self.header, verify=False).json();
        return response['result'];

    def predict_virtual_sensor(self, virtual_sensor_id):
    	url = '%s/%s/%s/%s/%s' % (self.url, 'sensor', virtual_sensor_id, 'classifier', 'predict');
    	response = requests.post(url, headers=self.header, verify=False).json();
        return response['ret'];
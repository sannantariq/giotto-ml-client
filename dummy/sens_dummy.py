import requests
import json
import sys
from bd_connect.connect_bd import get_json
from config.setting import Setting

class DummySensor:
	"""This is a class for sending data to connect_BD.py"""
	def __init__(self):
		self.data = {"sensor_data": {'mac_id': 'randomac', "status": 'on', "volume": '12'}};

def main():
	d = DummySensor();
	get_json(json.dumps(d.data));

if __name__ == '__main__':
	main()
		
		
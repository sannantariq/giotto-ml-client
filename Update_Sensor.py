import requests, random, json, time

class BdConnect:
    def __init__(self, data):
        """Initialises the sensor data and client data of the sensors"""
        # bdcredentials = Setting("bd_setting")
        # self.data = bdcredentials.setting
        self.data = {
                    "building": "CMUQ",
                    "client_key": "4NZJtozNNJWFlMLpcsnXI7hgkz0rPfhETrPyAcCXGcuXpxI4rf",
                    "client_id": "J9ZgTe40XKYS1l0LueTcIEQgllif8VFX9PI5EXfC",
                    "identifier": "randomsidentifier",
                    "email": "summeriotsannan@gmail.com",
                    "name":"randomsource_name",
                    "url":"http://localhost:82"
                }
        self.sensor_data = json.loads(data)['sensor_data']
        # self.data["mac_id"] = self.sensor_data["mac_id"]
        # self.sensor_data.pop("mac_id")
        # self.url = bdcredentials.setting["url"]
        self.loginurl = 'http://localhost:81';
        self.url = 'http://localhost:82';
        self.metadata = []
        self.common_data = []

    def get_oauth_token(self):
        """Obtains the oauth token of the user from Building Depot

            Returns:
                    Oauth token of the user
        """
        url = self.loginurl + "/oauth/access_token/client_id=" + self.data['client_id'] + \
              "/client_secret=" + self.data['client_key']

        print url
        response = requests.get(url, verify=False)
        print "response>>", response
        response = response.json()
        self.oauth_token = response['access_token']
        self.header = {"Authorization": "bearer " + self.oauth_token, 'content-type': 'application/json'}
        return self.oauth_token

    def timeseries_write(self, key, uuid):
            """Updates the timeseries data of the sensor wrt to the uuid
            and sensor points
            Args :
                            key:      name of the sensor point to get the sensor
                                     reading value of the sensor point.
                            uuid     :  uuid of the sensor point to updated.

            Returns:
                            {
                                    "success": "True"
                                    "HTTP Error 400": "Bad Request"
                            }
            """
            url = self.url + "/api/sensor/timeseries"
            payload = [{
                "sensor_id": uuid,
                "samples": [
                    {
                        "time": time.time(),
                        "value": self.sensor_data[key]
                    }
                ]
            }
            ]
            header = self.header
            payload = json.dumps(payload)
            print payload
            response = requests.post(url, headers=header, data=payload, verify=False)
            print response
            response = response.json()
            return "Time Series updated " + json.dumps(response)

    def timeseries_read(self, uuid, start_time, end_time):
        url = self.url + "/api/sensor/" + uuid + "/timeseries?start_time=" + str(start_time) + "&end_time=" + str(end_time)
        

        header = self.header;
        response = requests.get(url, headers = header);
        print response;
        return response.json();

def update(data):
    """
    Function obtains a json object from sensor connector in the format
    Args :
        {
            "sensor_data":{
                            <all sensor data>
                            }
        }

    Returns:
        {
            "success": "True" 
            "HTTP Error 400": "Bad Request"
        }
    """
    info = BdConnect(data)
    # Check Valid Client id and Client key
    if 'Invalid credentials' not in info.get_oauth_token():
        # Client_id and details are correct and token Generate access token
        print'Client id Verified'
        """Function to create the meta data to be updated/created
            on Building Depot"""
        sensor_id = '134fd7f5-7ce9-44f8-bf57-335d08be7def'
        if DOOR_OPEN:
            low = 75;
            high = 100;
        else:
            low = 0;
            high = 10;

        for i in range(100):
            info.sensor_data = {'volume': str(random.randrange(low, high))};
            time.sleep(1);
            info.timeseries_write('volume', sensor_id)
        # print info.timeseries_read(sensor_id, 1496290336.112976, 1496290366.075525);
    else:
        return 'Please Enter correct client_id/client_key Details'


data = {"sensor_data": {'mac_id': 'randomac', "status": 'on', "volume": '99'}};

DOOR_OPEN = False
if __name__ == '__main__':
    update(json.dumps(data))


from com.cisco.iotsp.sdk.http_device_connector.client import *
from com.cisco.iotsp.sdk.http_device_connector.client.apis import *
from com.cisco.iotsp.sdk.http_device_connector.client.models import *
import json
import requests
class SampleHttpDeviceConnector(object) :
    def __init__(self, service_address, access_token):
        print('Start HttpDeviceConnector API testing at %s' % service_address)

        host = 'https://' + service_address
        self._api = HttpDeviceConnectorApi()
        self._api.api_client.host = host
        configuration.access_token = access_token

        self.service_address = service_address
        self.token = access_token

    def postMessage(self,data_json, thing_uid):
        try:
            #all_params = ['message', 'route']
            #Service post_message only takes byt array.   convert message string to byte array

            #msg_byte = message_string.encode('utf-8')
            #msg_byte = message_string.encode('ascii')

            #byte_message = bytearray()
            #byte_message.extend(message_string)

            '''
            msg_list = []
            msg_list.append(message_string)
            self._api.post_message( message=message_string, route=route)

            print("\n---SampleHttpDeviceConnector postMessage is successful!!! ---")
            print("message posted: {0}", message_string);
            '''
            ######################

            route = '/v1/{0}/json-env/dev2app/'.format(thing_uid)
            url = 'https://' + self.service_address + '/v1/observations/publish'

            input = json.dumps(data_json)
            headers = {'content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer {0}'.format(self.token), 'route': '{0}'.format(route)}
            r = requests.post(url, data=input, headers=headers, verify=False)
            r.raise_for_status()

            print("\n---SampleHttpDeviceConnector postMessage succeed --- ")

            ##########
        except Exception as e:
            print("\n---SampleHttpDeviceConnector postMessage failed!!! ---")
            print(str(e))
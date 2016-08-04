from com.cisco.iotsp.sdk.presence.client import *
from com.cisco.iotsp.sdk.presence.client.rest import ApiException
import time
import sys

from com.cisco.iotsp.sdk.presence.client import *

class SampleLastNObservations(object) :
    def __init__(self, service_address, access_token):
        print('Start LastNObservations API testing at %s' % service_address)

        host = 'https://' + service_address
        self._api = LastNObservationsApi()
        self._api.api_client.host = host
        configuration.access_token = access_token

    def get_lastNObservations(self, thing_uid):
        try:
            #all_params = ['thing_uid', 'limit', 'offset']
            my_thing_observation = self._api.get_last_observations(thing_uid=thing_uid, offset=0, limit=10)
            print("\n--- get_last_observations is successful: ---")
            print(my_thing_observation)
            return True
        except ApiException as ae:
            print("\n--- get_last_observations failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_last_observations failed!!! ---")
            print(str(e))
            return False


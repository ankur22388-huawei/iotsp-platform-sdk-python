import time
import sys

from com.cisco.iotsp.sdk.observations.client import *
from com.cisco.iotsp.sdk.observations.client.rest import ApiException
import pprint
class SampleObservations(object) :
    def __init__(self, service_address, access_token):
        host = 'https://' + service_address
        self._api = ObservationsApi()
        self._api.api_client.host = host
        configuration.access_token = access_token

    def get_observation(self, observation_uid):
        try :
            ob = self._api.get_observation(observation_uid)
            print("\n--- get_observation is successful: ---")
            print(ob)
            return True
        except ApiException as ae:
            print("\n--- get_observation failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_observation failed!!! ---")
            print(str(e))
            return False

    def get_observations(self, query_string):
        try :
            limit = 20
            offset = 0
            obs = self._api.get_observations(query=query_string, limit=limit, offset=offset)
            print("\n--- get_observations, query string =  {0}, limit={1}, offset={2} is successful: ---".format(query_string, limit, offset))
            print(obs)
            return True
        except ApiException as ae:
            print("\n--- get_observations failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_observations failed!!! ---")
            print(str(e))
            return False


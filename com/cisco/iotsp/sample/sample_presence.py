#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
import time
import sys

from com.cisco.iotsp.sdk.presence.client import *
from com.cisco.iotsp.sdk.presence.client.rest import  ApiException
import pprint
class SamplePresence(object) :
    def __init__(self, service_address, access_token):
        print('Start Presence API testing at %s' % service_address)

        host = 'https://' + service_address
        self._api = PresenceApi()
        self._api.api_client.host = host
        pres_update_obj = PresenceApi()
        configuration.access_token = access_token

    def get_presence(self, thing_uid):
        try:
            pres = self._api.get_presence(thing_uid=thing_uid)
            print("\n--- get_presence is successful: ---")
            print(pres)
            return True
        except ApiException as ae:
            print("\n--- get_presence failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_presence failed!!! ---")
            print(str(e))

    def update_keep_alive(self, thing_uid):
        try:
            self._api.update_keep_alive_timestamp(thing_uid=thing_uid, keep_alive_ts=10)
            print("\n--- update_keep_alive_timestamp successful---")
            return True
        except ApiException as ae:
            print("\n--- update_keep_alive_timestamp failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- update_keep_alive_timestamp failed!!! ---")
            print(str(e))
            return False
        
    def delete_presence(self, thing_uid):    
        try :
            pres = self._api.delete_presence(thing_uid=thing_uid)

            print("\n--- delete_presence successful: ---")
            print(pres)
            return True
        except ApiException as ae:
            print("\n--- delete_presence failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- delete_presence failed!!! ---")
            print(str(e))
            return False

#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.

import time
import sys
import pprint
from com.cisco.iotsp.sdk.registration.client import *
from com.cisco.iotsp.sdk.registration.client.apis import *
from com.cisco.iotsp.sdk.registration.client.models import *

class SampleRegistration(object) :
    def __init__(self, service_address, access_token):
        print('Start Registration API testing at %s' % service_address)
        host = 'https://' + service_address
        self._api = RegistrationApi()
        self._api.api_client.host = host
        configuration.access_token = access_token

    def register_thing(self):
        # for now, the only property needed is the uuid a
        try:
            unique_id = UniqueIdentifier()
            unique_id.manufacturing_id = "a151c893-c7bc-48d6-8494-7e7775dcf3e5"
            #my_thing = Thing(make="Cisco Systems", model="SensorX", firmware_version="1.1", hardware_version="1.0", unique_identifiers=unique_id)
            my_thing = Thing(unique_identifiers=unique_id)


            req = RegistrationRequest()
            req.thing = my_thing

            print("Register thing with request:")
            print(req)
            resp = self._api.register_thing(registration_request=req)
            print("\n--- Register thing is successful: ---")
            print(resp)

        except Exception as e:
            print("\n--- Register thing failed!!! ---")
            print(str(e))


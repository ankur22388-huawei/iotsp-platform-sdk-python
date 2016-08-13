#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
from com.cisco.iotsp.sdk.thing_credentials.client import *
from com.cisco.iotsp.sdk.thing_credentials.client.apis import *
from com.cisco.iotsp.sdk.thing_credentials.client.models import *

class SampleThingCredentialsCreate(object) :
    def __init__(self, service_address, access_token):
        print('Start thing creadentials API testing at %s' % service_address)

        host = 'https://' + service_address
        self._api = ThingCredentialsApi()
        self._api.api_client.host = host
        configuration.access_token = access_token

    def createCredential(self, thing_uid, secret ):
        try:

            thingCredentialRequest = ThingBaseCredential()
            thingCredentialRequest.credential_type =  "secret"  #allowed_values = ["secret", "certificate"]
            thingCredentialRequest.thing_uid = thing_uid
            credential = Secret()
            credential.name = thing_uid
            credential.secret = secret
            thingCredentialRequest.credential = credential

            resp = self._api.create_credential(thingCredentialRequest)
            print("\n--- createCredential is successful: ---");
            print(resp)
        except Exception as e:
            print("\n---createCredential failed!!! ---")
            print(str(e))
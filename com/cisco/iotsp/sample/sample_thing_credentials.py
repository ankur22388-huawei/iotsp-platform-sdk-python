from com.cisco.iotsp.sdk.thing_credentials.client import *
from com.cisco.iotsp.sdk.thing_credentials.client.apis import *
from com.cisco.iotsp.sdk.thing_credentials.client.models import *

class SampleThingCredentials(object) :
    def __init__(self, service_address, access_token):
        print('Start HttpDeviceConnector API testing at %s' % service_address)

        host = 'https://' + service_address
        self._api = ThingCredentialsApi()
        self._api.api_client.host = host
        configuration.access_token = access_token

    def authenticateCredential(self, name, secret ):
        try:
            credential = Secret()
            credential.name= name
            credential.secret = secret
            resp = self._api.authenticateCredential(credential)
            print("\n--- authenticateCredential is successful: ---");
            print(resp)
        except Exception as e:
            print("\n---authenticateCredential!!! ---")
            print(str(e))

    def deleteCredential(self, credential_uid):
        try:
            resp = self._api.deleteCredential(credential_uid)
            print("\n--- deleteCredential is successful: ---");
            print(resp)
        except Exception as e:
            print("\n---deleteCredential failed!!! ---")
            print(str(e))

    def resetCredential(self, thing_uid, name, secret):
        try:

            thingCredentialRequest = ThingBaseCredential()
            thingCredentialRequest.credential_type = "secret"  # allowed_values = ["secret", "certificate"]
            thingCredentialRequest.thing_uid = thing_uid
            credential = Secret()
            credential.name = name
            credential.secret = secret
            thingCredentialRequest.credential = credential

            resp = self._api.resetCredential(thingCredentialRequest)
            print("\n--- resetCredential is successful: ---");
            print(resp)
        except Exception as e:
            print("\n---resetCredential failed!!! ---")
            print(str(e))
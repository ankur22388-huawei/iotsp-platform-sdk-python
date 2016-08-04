
import time
import pprint
import json
from com.cisco.iotsp.sdk.claims.client import *
from com.cisco.iotsp.sdk.claims.client.rest import ApiException
class SampleClaimsCreate(object) :
    def __init__(self, service_address, access_token):
        print('Start claim API testing at %s' % service_address)

        host = 'https://' + service_address
        self._api = ClaimsApi()
        self._api.api_client.host = host
        configuration.access_token = access_token

    def create_claim_from_file(self, json_file_path):
        try :
            with open(json_file_path) as data_file:
                root_map = json.load(data_file)

            return self.create_claim(root_map)
        except Exception as e:
            print("\n--- create_claim_from_file failed!!! ---")
            print(str(e))

    def create_claim(self, claimMap):
        try :
            claim_id = UniqueIdentifier()
            claim_id.mac_address = claimMap["uniqueIdentifiers"]["macAddress"]
            claim_id.manufacturing_id = claimMap["uniqueIdentifiers"]["manufacturingId"]
            claim_id.serial_number = claimMap["uniqueIdentifiers"]["serialNumber"]

            thing_details = ThingDescriptor()
            thing_details.name = claimMap["thingDetails"]["name"]
            thing_details.type = claimMap["thingDetails"]["type"]
            thing_details.description = claimMap["thingDetails"]["description"]

            new_claim = ThingClaimRequest(uid=None, make=claimMap["make"], model=claimMap["model"], unique_identifiers=claim_id, thing_details=thing_details, tags=claimMap["tags"])

            created_claim = self._api.create_claim(new_claim)
            print("createClaim is successful. New Claim = {0}".format(created_claim ))
            return created_claim.uid
        except ApiException as ae:
            print("\n--- create_claim failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- create_claim failed!!! ---")
            print(str(e))
            return ""

        
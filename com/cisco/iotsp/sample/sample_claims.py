#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
from com.cisco.iotsp.sdk.claims.client import *
from com.cisco.iotsp.sdk.claims.client.rest import ApiException
class SampleClaims(object) :
    def __init__(self, service_address, access_token):
        print('Start claim API testing at %s' % service_address)

        host = 'https://' + service_address
        self._api = ClaimsApi()
        self._api.api_client.host = host
        configuration.access_token = access_token

    def create_claim(self):
        try:
            claim_id = UniqueIdentifier(mac_address='38:4f:3e:99:47:29',
                                        manufacturing_id='a151c893-c7bc-48d6-8494-7e7775dcf3e5',
                                        serial_number='d361945a-453b-4504-9226-eb825dda7822')
            thing_details = ThingDescriptor(name='sensorABC', type='tempSensor',
                                            description='Temperature Sensor in Control Room')
            my_tags = ['Control Room', 'Temperature Sensor']
            new_claim = ThingClaimRequest(uid=None, make='Cisco Systems', model='SensorX', unique_identifiers=claim_id,
                                          thing_details=thing_details, tags=my_tags)

            created_claim = self._api.create_claim(new_claim)
            print("createClaim is successful. New Claim = {0}".format(created_claim))
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

    def get_claim(self, claim_uid):
        try:
            claim = self._api.get_claim(claim_uid=claim_uid)
            print("get_claim is successful")
            print(claim)
            print("\n")
            return True
        except ApiException as ae:
            print("\n--- get_claim failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_claim failed!!! ---")
            print(str(e))
            return False


    def get_claims(self):
        try:
            mac_claim = self._api.get_claims(key='unique_identifiers.mac_address', value='38:4f:3e:99:47:29',
                                             sort_key='thing_details.name', sort_order='Ascending', limit=20, offset=0)

            print("get_claims by mac_address is successful")
            print(mac_claim)

            type_claim = self._api.get_claims(key="thing_details.type", value="tempSensor", sort_key="make", sort_order="Ascending", limit=20, offset=0)
            print("get_claims by thingDetails.type is successful")
            print(type_claim)

            make_claim= self._api.get_claims(key="make", value="Cisco Systems", sort_key="model", sort_order="Descending", limit=20, offset=0)
            print("get_claims by make is successful")
            print(make_claim)
            return True
        except ApiException as ae:
            print("\n--- get_claims failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_claims failed!!! ---")
            print(str(e))
            return False

    def get_claims_by_filter(self):
        try :
            crit1 = FilterCriteria(key="thingDetails.name", value="temp", value_filter_type="STARTSWITH")
            crit2 = FilterCriteria(key="make", value="Cisco", value_filter_type="STARTSWITH")
            crit_list = [crit1, crit2]
            page = PageInfo(offset=0, limit=20)
            sort = SortCriteria(sort_key="model", sort_order= "Ascending")
            filter = ThingClaimFilter(page_info=page, sort_criteria=sort, filter_criteria=crit_list, filter_operator_enum="MATCH_ANY") #MATCH_ALL, MATCH_ANY, MATCH_NONE

            pageClaim = self._api.get_claims_by_filter(filter)
            print("---- get_claims_by_filter is successful -- ")
            print("ThingClaimFilter is: {0}", filter)
            print("PageThingClaim is: {0}", pageClaim)
            return True
        except ApiException as ae:
            print("\n--- get_claims_by_filter failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_claims_by_filter failed!!! ---")
            print(str(e))
            return False


    def delete_claim(self, claim_uid):
        try :
            delete_var  = self._api.delete_claim(claim_uid)
            print("delete_claim is successful. Claim is deleted: \n{0}".format(delete_var))
            return True
        except ApiException as ae:
            print("\n--- delete_claim failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- delete_claim failed!!! ---")
            print(str(e))
            return False
        
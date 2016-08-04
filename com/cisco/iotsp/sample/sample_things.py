import time
import sys
import pprint
import json
from com.cisco.iotsp.sdk.things.client import *
from com.cisco.iotsp.sdk.things.client.models import *
from com.cisco.iotsp.sdk.things.client.rest import ApiException

class SampleThings(object):
    def __init__(self, service_address, access_token):
        print('Start Registry Thing API testing at %s' % service_address)

        host = 'https://' + service_address
        self._api = ThingsApi()
        self._api.api_client.host = host
        configuration.access_token = access_token


    def get_thing(self, thing_uid):
        try:
            my_thing = self._api.get_thing(thing_uid)
            print("\n--- get_thing is successful: ---")
            print(my_thing)
            return True
        except ApiException as ae:
            print("\n--- get_thing failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_thing failed!!! ---")
            print(e.message)
            return False

    def get_things(self):
        try:
            mac_address =  '38:4f:3e:99:47:29'
            manufacturing_id =  'a151c893-c7bc-48d6-8494-7e7775dcf3e5'
            serial_number = 'd361945a-453b-4504-9226-eb825dda7822'

            #get things by key value pair
            #all_params = ['key', 'value', 'sort_key', 'sort_order', 'limit', 'offset']
            by_serialNum_thing=self._api.get_things(key="uniqueIdentifiers.serialNumber", value= serial_number,sort_key="sections.descriptor.name",sort_order="Ascending", limit=5, offset=0 )
            print("\n--- Get thing by serialNumber is successful: ---")
            print(by_serialNum_thing)

            by_schema_things=self._api.get_things(key="sectionSchemas.sectionName", value= "vendor", sort_key="uniqueIdentifiers.serialNumber", sort_order="Ascending", limit=5, offset=0  )
            print("\n--- Get thing by schema name is successful: ---")
            print(by_schema_things)

            by_man_things = self._api.get_things(key="uniqueIdentifiers.manufacturingId", value=manufacturing_id,
                                                 sort_key="uniqueIdentifiers.serialNumber", sort_order="Ascending",
                                                 limit=20, offset=0)
            print("\n--- Get thing by manufacturingId is successful: ---")
            print(by_man_things)

            by_make=self._api.get_things(key="sections.vendor.make", value= "Cisco Systems", sort_key="sections.vendor.model", sort_order="Ascending", limit=5, offset=0  )
            print("\n--- Get thing by make is successful: ---")
            print(by_make)
            return True
        except ApiException as ae:
            print("\n--- get_things failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers, ae.message))
            return False
        except Exception as e:
            print("\n--- get_things failed!!! ---")
            print(e.message)
            return False

    def get_things_by_filter(self):
        """
        Query a Page of Things by Filter
        """
        try:
            page = PageInfo(0, 10)
            sort = SortCriteria(sort_key="sections.vendor.model", sort_order="Ascending")
            crit1 = FilterCriteria(key="sections.vendor.make", value="Cisco", value_filter_type="STARTSWITH")
            crit2 = FilterCriteria(key="sections.descriptor.type", value="tempSensor", value_filter_type="EXACT")
            criteria = []
            criteria.append(crit1)
            criteria.append(crit2)

            filter = ThingFilter(page_info=page, sort_criteria=sort, filter_criteria=criteria, filter_operator_enum="MATCH_ANY")
            by_filter_things = self._api.get_things_by_filter(filter)
            print("\n---get_things_by_filter is successful: ---")
            print(by_filter_things)
            return True
        except ApiException as ae:
            print("\n--- get_things_by_filter failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers, ae.message))
            return False
        except Exception as e:
            print("\n--- Get thing by filter failed!!! ---")
            print(str(e))
            return False

    def delete_thing(self, thing_uid):
        try :
            delete_var  = self._api.delete_thing(thing_uid)

            print("\n--- delete_thing is successful. Delete thing: ---")
            return True
        except ApiException as ae:
            print("\n--- delete_thing failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- delete_thing failed!!! ---")
            print(str(e))
            return False


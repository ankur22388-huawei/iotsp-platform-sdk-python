#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
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

    def create_thing(self, json_file_path, account_alias):
        try:
            with open(json_file_path) as data_file:
                root_map = json.load(data_file)

            request = ThingCreateRequest()
            uid_map = root_map['uniqueIdentifiers']
            thing_id = ThingIdentifier()
            thing_id.mac_address = uid_map['macAddress']
            thing_id.manufacturing_id = uid_map['manufacturingId']
            thing_id.serial_number = uid_map['serialNumber']
            request.unique_identifiers = thing_id

            # Update the schema uid to be "account_aliase~~schemaName"
            # due to testing purpose, the sample code generates random account_aliase every run.
            sec_schema_list = root_map['sectionSchemas'];
            for sec_schema in sec_schema_list:
                scheam_uid = account_alias + sec_schema['schemaUid']
                sec_schema['schemaUid'] = scheam_uid

            request.section_schemas = sec_schema_list
            request.sections = root_map['sections']

            # User can assign a uid (must be unique) to the new Thing object
            # The Thing Uid must be in the formation of accountAlias~region~id.  Region is empty string for now
            # If user does not assign uid in createThing request, then system will assign a uid
            region = '';
            request.uid = account_alias + '~' + region + '~' + 'MyUniqueyDeviceUid'
            new_thing = self._api.create_thing(request)

            print("\n--- create_thing is successful: ---");
            print(new_thing)
            return new_thing.uid
        except Exception as e:
            print("\n--- create_thing failed!!! ---")
            print(e.message)
            return ""

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


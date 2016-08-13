#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
import time
import sys
import pprint
import json
from com.cisco.iotsp.sdk.things.client import *
from com.cisco.iotsp.sdk.things.client.models import *

class SampleThingsCreate(object):
    def __init__(self, service_address, access_token):
        print('Start Registry Thing API testing at %s' % service_address)

        host = 'https://' + service_address
        self._api = ThingsApi()
        self._api.api_client.host = host
        configuration.access_token = access_token

    def create_thing(self, json_file_path, account_alias):
        try :
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
            for sec_schema in sec_schema_list :
                scheam_uid = account_alias + sec_schema['schemaUid']
                sec_schema['schemaUid'] = scheam_uid

            request.section_schemas = sec_schema_list
            request.sections = root_map['sections']

            #User can assign a uid (must be unique) to the new Thing object
		    #The Thing Uid must be in the formation of accountAlias~region~id.  Region is empty string for now
			#If user does not assign uid in createThing request, then system will assign a uid
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


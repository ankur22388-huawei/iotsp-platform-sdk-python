#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
import json
from pprint import pprint
from com.cisco.iotsp.sdk.schemas.client import *
from com.cisco.iotsp.sdk.schemas.client.models import *
from com.cisco.iotsp.sdk.schemas.client.apis import *
from com.cisco.iotsp.sdk.schemas.client.rest import ApiException
class SampleSchemasCreate(object) :
    def __init__(self, service_address, access_token):
        print('Start Registry Schema API testing at %s' % service_address)

        host = 'https://' + service_address
        self.api = SchemasApi()
        self.api.api_client.host = host
        configuration.access_token = access_token

    def creat_schema_from_file(self, json_file_path):
        try:
            with open(json_file_path) as data_file:
                schema_json = json.load(data_file)
            pprint(schema_json)
            return self.creat_schema(schema_json)
        except Exception as e:
            print("\n--- creat_schema_from_file failed!!! ---")
            print(str(e))
            return ""


    def creat_schema(self, schema_json):
        try:
            request = SchemaCreateRequest()
            request.name = schema_json["name"]
            request.schema_type = schema_json["schemaType"]
            request.schema = schema_json["schema"]
            create_var = self.api.create_schema(request)
            print("\n--- create_schema is successful: ---")
            pprint(create_var)
            return create_var.uid
        except ApiException as ae:
            print("\n--- create_schema failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return ""
        except Exception as e:
            print("\n--- create_schema failed!!! ---")
            print(str(e))
            return ""


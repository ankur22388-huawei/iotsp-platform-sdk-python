from pprint import pprint
from com.cisco.iotsp.sdk.schemas.client import *
from com.cisco.iotsp.sdk.schemas.client.apis import *
from com.cisco.iotsp.sdk.schemas.client.rest import ApiException
class SampleSchemas(object) :
    def __init__(self, service_address, access_token):
        print('Start Registry Schema API testing at %s' % service_address)

        host = 'https://' + service_address
        self.api = SchemasApi()
        self.api.api_client.host = host
        configuration.access_token = access_token


    def get_schema(self, schema_uid):
        try:
            #get schema by schema uid
            my_schema = self.api.get_schema(schema_uid=schema_uid)
            print("\n--- get_schema is successful: ---")
            pprint(my_schema)
            return True
        except ApiException as ae:
            print("\n--- get_schema failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_schema  failed!!! ---")
            print(e.message)
            return False

    def get_schemas(self, schema_name, limit, offset):
        try:
            # get schema by schema name
            page_schemas = self.api.get_schemas(schema_name=schema_name, limit = limit, offset=offset)
            print("\n--- get_schemas is successful: ---")
            pprint(page_schemas)
            return page_schemas
        except ApiException as ae:
            print("\n--- get_schemas failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_schemas  failed!!! ---")
            print(e.message)
            return False

    def delete_schema(self, schema_uid):
        try :
            #delete schema, requires schema uid
            delete_var  = self.api.delete_schema(schema_uid=schema_uid)
            print("\n--- delete_schema is successful: ---")
            print(delete_var)
            return True
        except ApiException as ae:
            print("\n--- delete_schema failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- delete_schema failed!!! ---")
            print(e.message)
            return False

    def delete_schema_by_name(self, schema_name):
        try:
            page_schema = self.get_schemas(schema_name, 1, 0)
            uid = page_schema.items[0].uid
            self.delete_schema(schema_uid=uid)
            return True
        except ApiException as ae:
            print("\n--- delete_schema_by_name failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- delete_schema_by_name failed!!! ---")
            print(e.message)
            return False


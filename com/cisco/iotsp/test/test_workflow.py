import os.path
import os
import time

from com.cisco.iotsp.helper import authentication_helper
from com.cisco.iotsp.sample import sample_accounts
from com.cisco.iotsp.sample import sample_accounts_create
from com.cisco.iotsp.sample import sample_things
from com.cisco.iotsp.sample import sample_things_create
from com.cisco.iotsp.sample.workflow import sample_extend_thing
from com.cisco.iotsp.sample.workflow import sample_post_observation
from com.cisco.iotsp.sample import sample_schemas


class TestWorkflow(object) :

    def __init__(self, service_address):
        self.service_address = service_address

    def Test(self, service_address, account_alias):
        admin_password = 'incorrect'
        admin_email = account_alias + '@cisco.com'

        account_uid = sample_accounts_create.SampleAccountCreate.create_account(service_address, account_alias,
                                                                                admin_email, admin_password)

        print("account uid = {0}".format(account_uid))
        print("Sleep 1 second after create a new account before query")
        time.sleep(1)

        token = authentication_helper.AuthenticationHelper.get_token(service_address, admin_email, admin_password)
        print("user account token  = {0}".format(token))


        thingCreateApi = sample_things_create.SampleThingsCreate(service_address, token)
        parent = os.path.normpath(os.path.join(os.getcwd(), ".."))
        file_thing = os.path.join(parent, 'sample', 'data', 'sampleThing.json')
        thing_uid = thingCreateApi.create_thing(file_thing, account_alias)
        time.sleep(1)

        success_merge = self.test_merge_thing(service_address, token)

        #Must delete sampleSchemaLocation before call update_thing
		#because update_thing will create sampleSchemaLocation
        schema = sample_schemas.SampleSchemas(service_address, token)
        schema.delete_schema_by_name('sampleSchemaLocation')

        success_update = self.test_update_thing(service_address, token, account_alias)

        thingApi = sample_things.SampleThings(service_address, token)
        thingApi.delete_thing(thing_uid)
        time.sleep(1)

        success_post = self.test_post_observation(service_address, token, account_alias)


        account = sample_accounts.SampleAccount(service_address, token)
        success_delete_account = account.delete_account(account_uid)
        success =  success_merge & success_update & success_delete_account & success_post
        if (success == True):
            print("\n--- Workflow test success!!! ---")

        else:
            print("\n--- Workflow test failed!!! ---")
        return success

    def test_merge_thing(self, service_address, token) :
        extend_thing_api = sample_extend_thing.SampleExtendThings(service_address=service_address, access_token=token )
        return extend_thing_api.merge_thing()

    def test_update_thing(self, service_address, token, account_alias) :
        extend_thing_api = sample_extend_thing.SampleExtendThings(service_address=service_address, access_token=token )
        return extend_thing_api.update_thing(account_alias=account_alias)


    def test_post_observation(self, service_address, token, account_alias):
        ob_api = sample_post_observation.SamplePostObservation(service_address=service_address, user_account_access_token=token)
        return ob_api.postMessage(account_alias )

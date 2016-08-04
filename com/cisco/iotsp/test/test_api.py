import time
import os.path
import os

from com.cisco.iotsp.helper import authentication_helper
from com.cisco.iotsp.sample import sample_accounts
from com.cisco.iotsp.sample import sample_accounts_create
from com.cisco.iotsp.sample import sample_users
from com.cisco.iotsp.sample import sample_users_create
from com.cisco.iotsp.sample import sample_user_policies
from com.cisco.iotsp.sample import sample_schemas
from com.cisco.iotsp.sample import sample_schemas_create
from com.cisco.iotsp.sample import sample_things
from com.cisco.iotsp.sample import sample_things_create
from com.cisco.iotsp.sample import sample_last_n_observations
from com.cisco.iotsp.sample import sample_observations
from com.cisco.iotsp.sample import sample_claims
from com.cisco.iotsp.sample import sample_claims_create
from com.cisco.iotsp.sample import sample_presence

class TestApi(object) :
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
        print("token  = {0}".format(token))

        success_account = self.test_accounts(service_address, token, account_alias, account_uid)
        success_policy = self.test_user_policies(service_address, token)
        success_user = self.test_users(service_address, token, admin_email)
        sucess_schema = self.test_schemas(service_address, token)
        thing_uid = self.test_things(service_address, token, account_alias)
        success_thing = (thing_uid != "")
        sucess_presence = self.testPresence(service_address, token, thing_uid )
        success_ob = self.testObservation(service_address, token)

        thingApi = sample_things.SampleThings(service_address, token)
        success_thing_delete = thingApi.delete_thing(thing_uid )

        success_claim = self.testClaims(service_address, token)

        account = sample_accounts.SampleAccount(service_address, token)
        success_account_delete = account.delete_account(account_uid)
        success = success_account & success_policy & success_user & sucess_schema & success_thing & sucess_presence & success_ob & success_thing_delete & success_claim & success_account_delete
        if(success==True):
            print("\n--- API test success!!! ---")

        else :
            print("\n--- API test failed!!! ---")
        return success
    def test_accounts(self, service_address, token, account_alias, account_uid):
        # Test Accounts service
        account = sample_accounts.SampleAccount(service_address, token)
        success1 = account.get_account(account_uid)
        success2 = account.get_accounts(account_alias, 20, 0)
        return success1 & success2

    def test_user_policies(self, service_address, token):
        # Test user policies service
        policy = sample_user_policies.SampleUserPolicies(service_address, token)
        policy_uid = policy.get_user_policies()
        success = policy.get_user_policy(policy_uid)
        return success

    def test_users(self, service_address, token, admin_email) :
        # Test Users service
        user_create = sample_users_create.SampleUserCreate(service_address, token)
        user = sample_users.SampleUser(service_address, token)
        #policy_uid = account_alias + '~~admin-policy'
        user_uid = user_create.create_user()
        time.sleep(1)
        success_get = user.get_user(user_uid)
        success_gets = user.get_users(admin_email)
        success_delete = user.delete_user(user_uid)
        return success_get & success_gets & success_delete

    def test_schemas(self, service_address, token):
        # Test Schemas service
        schema_create = sample_schemas_create.SampleSchemasCreate(service_address, token)
        schema = sample_schemas.SampleSchemas(service_address, token)
        parent = os.path.normpath(os.path.join(os.getcwd(), ".."))
        file1 = os.path.join(parent, 'sample', 'data', 'sampleSchemaCustomerAddress.json')
        schemaUid = schema_create.creat_schema(os.path.normpath(file1))
        time.sleep(1)
        success_get = schema.get_schema(schemaUid)
        success_delete = schema.delete_schema(schemaUid)
        return success_get & success_delete

    def test_things(self, service_address, token, account_alias):
        # Test Things service
        thingCreateApi = sample_things_create.SampleThingsCreate(service_address, token)
        thingApi = sample_things.SampleThings(service_address, token)
        parent = os.path.normpath(os.path.join(os.getcwd(), ".."))
        file_thing = os.path.join(parent, 'sample', 'data', 'sampleThing.json')
        thing_uid = thingCreateApi.create_thing(file_thing, account_alias)
        time.sleep(1)
        thingApi.get_thing(thing_uid)
        thingApi.get_things()
        thingApi.get_things_by_filter()
        return thing_uid

    def testPresence(self, service_address, token, thing_uid):
        # Test Presence service
        presence = sample_presence.SamplePresence(service_address, token)
        success_update = presence.update_keep_alive(thing_uid)
        time.sleep(1)
        success_get = presence.get_presence(thing_uid)
        observ = sample_last_n_observations.SampleLastNObservations(service_address, token)
        success_lastN = observ.get_lastNObservations(thing_uid)
        success_delete = presence.delete_presence(thing_uid)
        return success_update & success_get & success_lastN & success_delete

    def testObservation(self, service_address, token):
        # Test Observation service
        obApi = sample_observations.SampleObservations(service_address, token)
        observationUid = 'Where do I get Observation Uid?'
        success_ob = obApi.get_observation(observationUid)
        queryString = 'how does query string look like?'
        success_obs = obApi.get_observations(queryString)
        return success_ob & success_obs

    def testClaims(self, service_address, token):
        # Test Claims service
        claim_create = sample_claims_create.SampleClaimsCreate(service_address, token)
        claim = sample_claims.SampleClaims(service_address, token)
        parent = os.path.normpath(os.path.join(os.getcwd(), ".."))
        file_claim = os.path.join(parent, 'sample', 'data', 'sampleClaim.json')
        claimUid = claim_create.create_claim_from_file(file_claim)
        success_create = (claimUid != "")
        time.sleep(1)
        sucess_get = claim.get_claim(claimUid)
        sucess_gets = claim.get_claims()
        sucess_getf = claim.get_claims_by_filter()
        # Test Registration service
        #registration = sample_registration.SampleRegistration(service_address, token)
        #registration.register_thing()
        success_delete = claim.delete_claim(claim_uid=claimUid)
        return success_create & sucess_get & sucess_gets & sucess_getf & success_delete

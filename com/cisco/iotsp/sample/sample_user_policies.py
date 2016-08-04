
from com.cisco.iotsp.sdk.users.client import *
from com.cisco.iotsp.sdk.users.client.rest import ApiException
class SampleUserPolicies(object):
    def __init__(self, service_address, token):
        print('Create Sample UserPolicies with users service at %s' % service_address)
        host = 'https://' + service_address
        self._api = UserPoliciesApi()
        self._api.api_client.host = host
        configuration.access_token = token

    def get_user_policy(self, userPolicyUid):
        try:
            policy = self._api.get_user_policy(user_policy_uid=userPolicyUid)
            print("\n--- get_user_policy succeed !!! ---")
            print policy
            return True
        except ApiException as ae:
            print("\n--- get_user_policy failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get policy failed!!! ---")
            print(str(e))
            return False

    def get_user_policies(self):
        try:
            '''
            :param str sort_key: sort by a key in userPolicy. Nested fields can be . delimited
            :param str sort_order: sort in ascending or descending order
            :param int limit: maximum number of user policies to return
            :param int offset: starting index of user policies in return payload
            '''
            policies = self._api.get_user_policies(sort_key="name", sort_order="Ascending", limit=10, offset=0)
            print("\n--- get_user_policies is successfull !!! ---")
            print policies
            policy_uid = policies.items[0].uid
            return policy_uid
        except ApiException as ae:
            print("\n--- get_user_policies failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_user_policies failed!!! ---")
            print(str(e))
            return ""




'''
####Not supported for now
def create_policy(self):
    try:
        request = UserPolicyCreateObject()
        request.name = 'testPolicy'
        request.policy_units = 'policyUnits'
        newPolicy = self._api.create_user_policy(user_policy_create_request=request)
        print newPolicy
        return newPolicy
    except Exception as e:
        print("\n--- create policy failed!!! ---")
        print(str(e))
'''
import random
import string
from com.cisco.iotsp.sdk.users.client import *
from com.cisco.iotsp.sdk.users.client.rest import ApiException
class SampleUserCreate(object):

    def __init__(self, service_address, token):
        print('Create Sample User with users service at %s' % service_address)
        host = 'https://' + service_address
        self._api = UsersApi()
        self._api.api_client.host = host

        self._api_policy = UserPoliciesApi()
        self._api_policy.api_client.host = host

        configuration.access_token = token

    def create_user(self):
        '''
        Create a user
        :param account_alias: the alias that was used to create the account
        :param policy_uid: the uid of the policy that is used to create the user, for now, only supports admin policy.
                for a given account, its admin policy uid is : account_alias + '~~admin-policy'
        :return:True for success, False for failure
        '''
        try:
            #for now, there is only one policy under each account. It's the admin policy, that can be used to create a user
            policies = self._api_policy.get_user_policies(sort_key="name", sort_order="Ascending", limit=10, offset=0)
            policy_uid = policies.items[0].uid
            user_email_prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

            request = UserCreateObject()
            request.first_name = 'MIKE'
            request.last_name = 'WAZOWSKI'
            request.email_address = "{0}@Monsters.com".format(user_email_prefix)
            request.password = 'Celia';

            address = Address()
            address.address_line1 = 'One Eye Apt.'
            address.address_line2 = 'Top Scarer Street'
            address.city = 'Monster City'
            address.state = 'CA';
            address.country = 'USA'
            address.zip4 = 1234
            address.zip5 = 12345
            request.address = address
            request.user_policy_uid = policy_uid

            user = self._api.create_user(request)
            print("\n --- create_user success ---, user = \n{0}".format(user))

            return user.uid
        except ApiException as ae:
            print("\n--- create_user failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return ""
        except Exception as e:
            print("\n--- create_user failed!!! ---")
            print(str(e))
            return "";



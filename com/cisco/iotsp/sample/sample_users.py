#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.

from com.cisco.iotsp.sdk.users.client import *
from com.cisco.iotsp.sdk.users.client.rest import ApiException
import random
import string
class SampleUser(object):

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

    def get_users(self, user_email):
        try:
            users = self._api.get_users(email_address=user_email, limit=20, offset=0)  #'email_address', 'limit', 'offset'
            print("\n --- get_users success ---. Users are: ")
            for user in users.items:
                print user
                print user.user_policy_uid

            return True
        except ApiException as ae:
            print("\n--- get_users failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n --- get_users failed!!! ---")
            print(e.message)
            return False

    def get_user(self, user_uid):
        try:
            user=self._api.get_user(user_uid=user_uid)
            print("\n --- get_user success ---. User is:")
            print user
            return True
        except ApiException as ae:
            print("\n--- get_user failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers, ae.message))
            return False
        except Exception as e:
            print("\n--- get_user failed!!! ---")
            print(e.message)
            return False


    def delete_user(self, user_uid):
        try:
            user = self._api.delete_user(user_uid=user_uid)
            print("\ndelete_user success ---. user is deleted:")
            print user
            return True
        except ApiException as ae:
            print("\n--- delete_user failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers, ae.message))
            return False
        except Exception as e:
            print("\n--- delete_user failed!!! ---")
            print(e.message)
            return False



from com.cisco.iotsp.sdk.users.client import *
from com.cisco.iotsp.sdk.users.client.rest import ApiException

class SampleUser(object):

    def __init__(self, service_address, token):
        print('Create Sample User with users service at %s' % service_address)
        host = 'https://' + service_address
        self._api = UsersApi()
        self._api.api_client.host = host
        configuration.access_token = token

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


from com.cisco.iotsp.sdk.acounts.client import *
from com.cisco.iotsp.sdk.acounts.client.rest import ApiException
class SampleAccount(object):

    def __init__(self, service_address, token) :
        print('Create Sample Account with account service at %s' % service_address)
        host = 'https://' + service_address
        self._api = AccountsApi()
        self._api.api_client.host = host
        configuration.access_token = token

    def get_account(self, account_uid):
        '''
        get account by account uid.  For now, account service only supports get your own account
        In the future, a global admin account can get all accounts.
        :param account_uid: the account uid returned by create_account
        :return:True for success, False for failure
        '''
        try:
            my_account = self._api.get_account(account_uid=account_uid)
            print('\n--- get_account is successful. --- \n The account is:')
            print (my_account)
            return True
        except ApiException as ae:
            print("\n--- get_account failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                              ae.message))
            return False
        except Exception as e:
            print("\n--- get_account failed!!! ---")
            print(str(e))
            return False

    def get_accounts(self, alias, limit, offset):
        '''
        Get all accounts if this account instance is a global admin account
        :param limit: used for pagination, such as the page size, it's the number of accounts returned from this call
        :param offset:  the start number of the page.
        :return:True for success, False for failure
        '''
        try:
            accounts = self._api.get_accounts(alias = alias, limit=limit, offset=offset)
            print('\n--- get_accounts is successful.---' )

            if accounts.items != None:
                for item in accounts.items:
                    print(item)

            return True
        except ApiException as ae:
            print("\n--- get_accounts failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- get_accounts failed!!! ---")
            print(str(e))
            return False

    def delete_account(self, account_uid):
        '''
        Delete an account with account_uid.
        :param account_uid: the account uid to be deleted
        :return:True for success, False for failure
        '''
        try:
            deleted_account = self._api.delete_account(account_uid=account_uid)
            print('\n --- delete_account is successful. --- \n Account is deleted: ')
            print(deleted_account)
            return True
        except ApiException as ae:
            print("\n--- delete_account failed!!! ---")
            print ("status = {0}, reason = {1} \nheads = {2} \n message ={3}".format(ae.status, ae.reason, ae.headers,
                                                                                     ae.message))
            return False
        except Exception as e:
            print("\n--- delete_account failed!!! ---")
            print(str(e))
            return False

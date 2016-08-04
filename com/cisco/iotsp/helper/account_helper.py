import requests
import json
class AccountHelper(object) :
    @staticmethod
    def create_account(serviceAddr, account_alias, account_name, account_type, admin_first_name,
                            admin_last_name, admin_password, admin_email):


        ''' Create a new account wtih Cisco IOTSP accounts service.
        :return:   the newly create account uid
        '''
        try:

            url = 'https://' + serviceAddr + '/v1/user-services/accounts'

            d = {'name': account_name, 'alias': account_alias, 'accountType': 'TRIAL',
                 'accountAdminUser': {'firstName': admin_first_name, 'lastName': admin_last_name,
                                      'emailAddress': admin_email, 'password': admin_password}}

            input = json.dumps(d)
            # r = requests.post(url, json=input, verify=False)

            headers = {'content-type': 'application/json'}
            r = requests.post(url, data=input, headers=headers, verify=False)
            print("createAccount, response sstatus = {0}, headers = {1}\n, response text = {2}".format(r.status_code, r.headers,
                                                                                                       r.text))

            r.raise_for_status()
            response_json = r.json()
            print("response json = {0}".format(response_json))
            response_dict = json.loads(r.text)
            account_uid = response_dict.get('uid')

            return account_uid

        except Exception as e:
            print("\n--- Create Account failed!!! ---\n")
            print(str(e))
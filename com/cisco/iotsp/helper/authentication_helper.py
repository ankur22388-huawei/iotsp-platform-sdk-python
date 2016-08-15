#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
import requests
import ast

class AuthenticationHelper(object) :
    """
       This class shows how to obtain access toke from OAuth2 server
    """
    @staticmethod
    def get_token(service_address, admin_email, password, client_id ='iotspoauth2client', client_secret ='iotspoauth2client'):
        """
        Get access token from OAuth2 server
        Input params:
        admin_email:   Cluster HA IP address
        admin_email:   account's admin email
        password:       password
        client_id:          user application registration id, for now, hard coded to 'iotspoauth2client'
        client_secret:      user app secret, for now, hard coded to 'iotspoauth2client'

        :return:  access token
        """
        try:
            d = {'grant_type': 'password', 'username': admin_email, 'password': password,
                 'client_id': client_id, 'client_secret': client_secret}

            url = 'https://' + service_address + '/v1/user-services/oauth2/token'
            r = requests.post(url, data=d, verify=False)
            token_dict = ast.literal_eval(r.text)
            return token_dict.get('access_token')

        except Exception as e:
            print('Failed to obtain access token')
            print(e)



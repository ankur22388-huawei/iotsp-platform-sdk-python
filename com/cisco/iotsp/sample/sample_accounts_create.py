
from com.cisco.iotsp.helper import account_helper
class SampleAccountCreate(object):
    @staticmethod
    def create_account(service_address, account_alias, admin_email, admin_password):
        account_name = 'Cisco IOT Python SDK Test Account'
        account_type = 'TRIAL'
        admin_first_name = "admin"
        admin_last_name = 'Python_SDK_Test_LastName'
        account_uid = account_helper.AccountHelper.create_account(service_address, account_alias, account_name,
                                                                  account_type, admin_first_name, admin_last_name,
                                                                  admin_password, admin_email)
        return account_uid
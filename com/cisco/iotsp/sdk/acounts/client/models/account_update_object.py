# coding: utf-8

"""
    API documentation for Account management service

    The service provides APIs for managing the accounts on Cisco IOT Software Platform

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class AccountUpdateObject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, account_type=None, admin_user_uid=None):
        """
        AccountUpdateObject - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'account_type': 'str',
            'admin_user_uid': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'account_type': 'accountType',
            'admin_user_uid': 'adminUserUid'
        }

        self._name = name
        self._account_type = account_type
        self._admin_user_uid = admin_user_uid

    @property
    def name(self):
        """
        Gets the name of this AccountUpdateObject.
        Name of the account to be created..

        :return: The name of this AccountUpdateObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AccountUpdateObject.
        Name of the account to be created..

        :param name: The name of this AccountUpdateObject.
        :type: str
        """

        self._name = name

    @property
    def account_type(self):
        """
        Gets the account_type of this AccountUpdateObject.
        Type of the account to be created.

        :return: The account_type of this AccountUpdateObject.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this AccountUpdateObject.
        Type of the account to be created.

        :param account_type: The account_type of this AccountUpdateObject.
        :type: str
        """
        allowed_values = ["TRIAL", "PAID"]
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type`, must be one of {0}"
                .format(allowed_values)
            )

        self._account_type = account_type

    @property
    def admin_user_uid(self):
        """
        Gets the admin_user_uid of this AccountUpdateObject.
        UID of the admin user to be associated with the account.

        :return: The admin_user_uid of this AccountUpdateObject.
        :rtype: str
        """
        return self._admin_user_uid

    @admin_user_uid.setter
    def admin_user_uid(self, admin_user_uid):
        """
        Sets the admin_user_uid of this AccountUpdateObject.
        UID of the admin user to be associated with the account.

        :param admin_user_uid: The admin_user_uid of this AccountUpdateObject.
        :type: str
        """

        self._admin_user_uid = admin_user_uid

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

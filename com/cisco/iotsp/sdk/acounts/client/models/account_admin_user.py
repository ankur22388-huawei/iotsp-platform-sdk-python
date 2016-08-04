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


class AccountAdminUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, first_name=None, last_name=None, email_address=None, password=None):
        """
        AccountAdminUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'first_name': 'str',
            'last_name': 'str',
            'email_address': 'str',
            'password': 'str'
        }

        self.attribute_map = {
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email_address': 'emailAddress',
            'password': 'password'
        }

        self._first_name = first_name
        self._last_name = last_name
        self._email_address = email_address
        self._password = password

    @property
    def first_name(self):
        """
        Gets the first_name of this AccountAdminUser.


        :return: The first_name of this AccountAdminUser.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this AccountAdminUser.


        :param first_name: The first_name of this AccountAdminUser.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this AccountAdminUser.


        :return: The last_name of this AccountAdminUser.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this AccountAdminUser.


        :param last_name: The last_name of this AccountAdminUser.
        :type: str
        """

        self._last_name = last_name

    @property
    def email_address(self):
        """
        Gets the email_address of this AccountAdminUser.
        Email address of the admin user to be created while creating a new account. The email address must be a valid email address.

        :return: The email_address of this AccountAdminUser.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this AccountAdminUser.
        Email address of the admin user to be created while creating a new account. The email address must be a valid email address.

        :param email_address: The email_address of this AccountAdminUser.
        :type: str
        """

        self._email_address = email_address

    @property
    def password(self):
        """
        Gets the password of this AccountAdminUser.
        Password of the admin user.

        :return: The password of this AccountAdminUser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this AccountAdminUser.
        Password of the admin user.

        :param password: The password of this AccountAdminUser.
        :type: str
        """

        self._password = password

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

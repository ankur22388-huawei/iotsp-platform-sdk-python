#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
# coding: utf-8

"""
    API documentation for User Service

    These are all the APIs for the User Service

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


class UserUpdateObject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, first_name=None, last_name=None, email_address=None, address=None, user_policy_uid=None):
        """
        UserUpdateObject - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'first_name': 'str',
            'last_name': 'str',
            'email_address': 'str',
            'address': 'Address',
            'user_policy_uid': 'str'
        }

        self.attribute_map = {
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email_address': 'emailAddress',
            'address': 'address',
            'user_policy_uid': 'userPolicyUid'
        }

        self._first_name = first_name
        self._last_name = last_name
        self._email_address = email_address
        self._address = address
        self._user_policy_uid = user_policy_uid

    @property
    def first_name(self):
        """
        Gets the first_name of this UserUpdateObject.


        :return: The first_name of this UserUpdateObject.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UserUpdateObject.


        :param first_name: The first_name of this UserUpdateObject.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this UserUpdateObject.


        :return: The last_name of this UserUpdateObject.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UserUpdateObject.


        :param last_name: The last_name of this UserUpdateObject.
        :type: str
        """

        self._last_name = last_name

    @property
    def email_address(self):
        """
        Gets the email_address of this UserUpdateObject.
        Email address of the user. The email address must be a valid email address.

        :return: The email_address of this UserUpdateObject.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this UserUpdateObject.
        Email address of the user. The email address must be a valid email address.

        :param email_address: The email_address of this UserUpdateObject.
        :type: str
        """

        self._email_address = email_address

    @property
    def address(self):
        """
        Gets the address of this UserUpdateObject.


        :return: The address of this UserUpdateObject.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this UserUpdateObject.


        :param address: The address of this UserUpdateObject.
        :type: Address
        """

        self._address = address

    @property
    def user_policy_uid(self):
        """
        Gets the user_policy_uid of this UserUpdateObject.
        UID of the user policy to be associated with the user.

        :return: The user_policy_uid of this UserUpdateObject.
        :rtype: str
        """
        return self._user_policy_uid

    @user_policy_uid.setter
    def user_policy_uid(self, user_policy_uid):
        """
        Sets the user_policy_uid of this UserUpdateObject.
        UID of the user policy to be associated with the user.

        :param user_policy_uid: The user_policy_uid of this UserUpdateObject.
        :type: str
        """

        self._user_policy_uid = user_policy_uid

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

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


class Address(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address_line1=None, address_line2=None, zip5=None, zip4=None, city=None, state=None, country=None):
        """
        Address - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address_line1': 'str',
            'address_line2': 'str',
            'zip5': 'int',
            'zip4': 'int',
            'city': 'str',
            'state': 'str',
            'country': 'str'
        }

        self.attribute_map = {
            'address_line1': 'addressLine1',
            'address_line2': 'addressLine2',
            'zip5': 'zip5',
            'zip4': 'zip4',
            'city': 'city',
            'state': 'state',
            'country': 'country'
        }

        self._address_line1 = address_line1
        self._address_line2 = address_line2
        self._zip5 = zip5
        self._zip4 = zip4
        self._city = city
        self._state = state
        self._country = country

    @property
    def address_line1(self):
        """
        Gets the address_line1 of this Address.


        :return: The address_line1 of this Address.
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """
        Sets the address_line1 of this Address.


        :param address_line1: The address_line1 of this Address.
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """
        Gets the address_line2 of this Address.


        :return: The address_line2 of this Address.
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """
        Sets the address_line2 of this Address.


        :param address_line2: The address_line2 of this Address.
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def zip5(self):
        """
        Gets the zip5 of this Address.


        :return: The zip5 of this Address.
        :rtype: int
        """
        return self._zip5

    @zip5.setter
    def zip5(self, zip5):
        """
        Sets the zip5 of this Address.


        :param zip5: The zip5 of this Address.
        :type: int
        """

        self._zip5 = zip5

    @property
    def zip4(self):
        """
        Gets the zip4 of this Address.


        :return: The zip4 of this Address.
        :rtype: int
        """
        return self._zip4

    @zip4.setter
    def zip4(self, zip4):
        """
        Sets the zip4 of this Address.


        :param zip4: The zip4 of this Address.
        :type: int
        """

        self._zip4 = zip4

    @property
    def city(self):
        """
        Gets the city of this Address.


        :return: The city of this Address.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Address.


        :param city: The city of this Address.
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """
        Gets the state of this Address.


        :return: The state of this Address.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Address.


        :param state: The state of this Address.
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """
        Gets the country of this Address.


        :return: The country of this Address.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Address.


        :param country: The country of this Address.
        :type: str
        """

        self._country = country

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

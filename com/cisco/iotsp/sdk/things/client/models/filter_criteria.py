#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
# coding: utf-8

"""
    API Documentation


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


class FilterCriteria(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, key=None, value=None, value_filter_type=None):
        """
        FilterCriteria - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key': 'str',
            'value': 'str',
            'value_filter_type': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value',
            'value_filter_type': 'valueFilterType'
        }

        self._key = key
        self._value = value
        self._value_filter_type = value_filter_type

    @property
    def key(self):
        """
        Gets the key of this FilterCriteria.


        :return: The key of this FilterCriteria.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this FilterCriteria.


        :param key: The key of this FilterCriteria.
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """
        Gets the value of this FilterCriteria.


        :return: The value of this FilterCriteria.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this FilterCriteria.


        :param value: The value of this FilterCriteria.
        :type: str
        """

        self._value = value

    @property
    def value_filter_type(self):
        """
        Gets the value_filter_type of this FilterCriteria.


        :return: The value_filter_type of this FilterCriteria.
        :rtype: str
        """
        return self._value_filter_type

    @value_filter_type.setter
    def value_filter_type(self, value_filter_type):
        """
        Sets the value_filter_type of this FilterCriteria.


        :param value_filter_type: The value_filter_type of this FilterCriteria.
        :type: str
        """
        allowed_values = ["EXACT", "STARTSWITH"]
        if value_filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `value_filter_type`, must be one of {0}"
                .format(allowed_values)
            )

        self._value_filter_type = value_filter_type

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

#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
# coding: utf-8

"""
    API documentation for Claims

    APIs for operations on Claims

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


class PageInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, offset=None, limit=None):
        """
        PageInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'offset': 'int',
            'limit': 'int'
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit'
        }

        self._offset = offset
        self._limit = limit

    @property
    def offset(self):
        """
        Gets the offset of this PageInfo.


        :return: The offset of this PageInfo.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this PageInfo.


        :param offset: The offset of this PageInfo.
        :type: int
        """

        if not offset:
            raise ValueError("Invalid value for `offset`, must not be `None`")
        if offset > 4500.0:
            raise ValueError("Invalid value for `offset`, must be a value less than or equal to `4500.0`")
        if offset < 0.0:
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0.0`")

        self._offset = offset

    @property
    def limit(self):
        """
        Gets the limit of this PageInfo.


        :return: The limit of this PageInfo.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this PageInfo.


        :param limit: The limit of this PageInfo.
        :type: int
        """

        if not limit:
            raise ValueError("Invalid value for `limit`, must not be `None`")
        if limit > 500.0:
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `500.0`")
        if limit < 1.0:
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `1.0`")

        self._limit = limit

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

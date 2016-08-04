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


class PageThing(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, total_rows=None, items=None, next_page_exists=False, previous_page_exists=False):
        """
        PageThing - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total_rows': 'int',
            'items': 'list[Thing]',
            'next_page_exists': 'bool',
            'previous_page_exists': 'bool'
        }

        self.attribute_map = {
            'total_rows': 'totalRows',
            'items': 'items',
            'next_page_exists': 'nextPageExists',
            'previous_page_exists': 'previousPageExists'
        }

        self._total_rows = total_rows
        self._items = items
        self._next_page_exists = next_page_exists
        self._previous_page_exists = previous_page_exists

    @property
    def total_rows(self):
        """
        Gets the total_rows of this PageThing.


        :return: The total_rows of this PageThing.
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """
        Sets the total_rows of this PageThing.


        :param total_rows: The total_rows of this PageThing.
        :type: int
        """

        self._total_rows = total_rows

    @property
    def items(self):
        """
        Gets the items of this PageThing.


        :return: The items of this PageThing.
        :rtype: list[Thing]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this PageThing.


        :param items: The items of this PageThing.
        :type: list[Thing]
        """

        self._items = items

    @property
    def next_page_exists(self):
        """
        Gets the next_page_exists of this PageThing.


        :return: The next_page_exists of this PageThing.
        :rtype: bool
        """
        return self._next_page_exists

    @next_page_exists.setter
    def next_page_exists(self, next_page_exists):
        """
        Sets the next_page_exists of this PageThing.


        :param next_page_exists: The next_page_exists of this PageThing.
        :type: bool
        """

        self._next_page_exists = next_page_exists

    @property
    def previous_page_exists(self):
        """
        Gets the previous_page_exists of this PageThing.


        :return: The previous_page_exists of this PageThing.
        :rtype: bool
        """
        return self._previous_page_exists

    @previous_page_exists.setter
    def previous_page_exists(self, previous_page_exists):
        """
        Sets the previous_page_exists of this PageThing.


        :param previous_page_exists: The previous_page_exists of this PageThing.
        :type: bool
        """

        self._previous_page_exists = previous_page_exists

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

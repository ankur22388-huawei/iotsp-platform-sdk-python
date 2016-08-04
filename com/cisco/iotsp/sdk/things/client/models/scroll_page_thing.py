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


class ScrollPageThing(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, items=None, next_scroll_id=None):
        """
        ScrollPageThing - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'items': 'list[Thing]',
            'next_scroll_id': 'str'
        }

        self.attribute_map = {
            'items': 'items',
            'next_scroll_id': 'nextScrollId'
        }

        self._items = items
        self._next_scroll_id = next_scroll_id

    @property
    def items(self):
        """
        Gets the items of this ScrollPageThing.


        :return: The items of this ScrollPageThing.
        :rtype: list[Thing]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ScrollPageThing.


        :param items: The items of this ScrollPageThing.
        :type: list[Thing]
        """

        self._items = items

    @property
    def next_scroll_id(self):
        """
        Gets the next_scroll_id of this ScrollPageThing.


        :return: The next_scroll_id of this ScrollPageThing.
        :rtype: str
        """
        return self._next_scroll_id

    @next_scroll_id.setter
    def next_scroll_id(self, next_scroll_id):
        """
        Sets the next_scroll_id of this ScrollPageThing.


        :param next_scroll_id: The next_scroll_id of this ScrollPageThing.
        :type: str
        """

        self._next_scroll_id = next_scroll_id

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

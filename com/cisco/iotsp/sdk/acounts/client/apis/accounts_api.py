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

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AccountsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_account(self, account_create_request, **kwargs):
        """
        Creates a new account
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_account(account_create_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AccountCreateObject account_create_request: The account to be created (required)
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_account_with_http_info(account_create_request, **kwargs)
        else:
            (data) = self.create_account_with_http_info(account_create_request, **kwargs)
            return data

    def create_account_with_http_info(self, account_create_request, **kwargs):
        """
        Creates a new account
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_account_with_http_info(account_create_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AccountCreateObject account_create_request: The account to be created (required)
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_create_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_create_request' is set
        if ('account_create_request' not in params) or (params['account_create_request'] is None):
            raise ValueError("Missing the required parameter `account_create_request` when calling `create_account`")

        resource_path = '/v1/user-services/accounts'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account_create_request' in params:
            body_params = params['account_create_request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuthScheme']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Account',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def delete_account(self, account_uid, **kwargs):
        """
        Delete account by accountUid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_account(account_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_uid: Uid of account (required)
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_account_with_http_info(account_uid, **kwargs)
        else:
            (data) = self.delete_account_with_http_info(account_uid, **kwargs)
            return data

    def delete_account_with_http_info(self, account_uid, **kwargs):
        """
        Delete account by accountUid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_account_with_http_info(account_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_uid: Uid of account (required)
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_uid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_uid' is set
        if ('account_uid' not in params) or (params['account_uid'] is None):
            raise ValueError("Missing the required parameter `account_uid` when calling `delete_account`")

        resource_path = '/v1/user-services/accounts/{accountUid}'.replace('{format}', 'json')
        path_params = {}
        if 'account_uid' in params:
            path_params['accountUid'] = params['account_uid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['tokenAuthScheme']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Account',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_account(self, account_uid, **kwargs):
        """
        Get account by accountUid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account(account_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_uid: Uid of account (required)
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_account_with_http_info(account_uid, **kwargs)
        else:
            (data) = self.get_account_with_http_info(account_uid, **kwargs)
            return data

    def get_account_with_http_info(self, account_uid, **kwargs):
        """
        Get account by accountUid
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_with_http_info(account_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_uid: Uid of account (required)
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_uid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_uid' is set
        if ('account_uid' not in params) or (params['account_uid'] is None):
            raise ValueError("Missing the required parameter `account_uid` when calling `get_account`")

        resource_path = '/v1/user-services/accounts/{accountUid}'.replace('{format}', 'json')
        path_params = {}
        if 'account_uid' in params:
            path_params['accountUid'] = params['account_uid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['tokenAuthScheme']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Account',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_accounts(self, **kwargs):
        """
        Get a page of accounts
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_accounts(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str alias: search by alias of the account
        :param str sort_key: sort by a key in account. Nested fields can be . delimited
        :param str sort_order: sort in ascending or descending order
        :param int limit: start index of page
        :param int offset: size of page
        :return: PageAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_accounts_with_http_info(**kwargs)
        else:
            (data) = self.get_accounts_with_http_info(**kwargs)
            return data

    def get_accounts_with_http_info(self, **kwargs):
        """
        Get a page of accounts
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_accounts_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str alias: search by alias of the account
        :param str sort_key: sort by a key in account. Nested fields can be . delimited
        :param str sort_order: sort in ascending or descending order
        :param int limit: start index of page
        :param int offset: size of page
        :return: PageAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alias', 'sort_key', 'sort_order', 'limit', 'offset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_accounts" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/user-services/accounts'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'alias' in params:
            query_params['alias'] = params['alias']
        if 'sort_key' in params:
            query_params['sortKey'] = params['sort_key']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['tokenAuthScheme']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PageAccount',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_account(self, account_uid, account_update_request, **kwargs):
        """
        Update account
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_account(account_uid, account_update_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_uid: Uid of account (required)
        :param AccountUpdateObject account_update_request: The account data to be updated (required)
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_account_with_http_info(account_uid, account_update_request, **kwargs)
        else:
            (data) = self.update_account_with_http_info(account_uid, account_update_request, **kwargs)
            return data

    def update_account_with_http_info(self, account_uid, account_update_request, **kwargs):
        """
        Update account
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_account_with_http_info(account_uid, account_update_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_uid: Uid of account (required)
        :param AccountUpdateObject account_update_request: The account data to be updated (required)
        :return: Account
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_uid', 'account_update_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_uid' is set
        if ('account_uid' not in params) or (params['account_uid'] is None):
            raise ValueError("Missing the required parameter `account_uid` when calling `update_account`")
        # verify the required parameter 'account_update_request' is set
        if ('account_update_request' not in params) or (params['account_update_request'] is None):
            raise ValueError("Missing the required parameter `account_update_request` when calling `update_account`")

        resource_path = '/v1/user-services/accounts/{accountUid}'.replace('{format}', 'json')
        path_params = {}
        if 'account_uid' in params:
            path_params['accountUid'] = params['account_uid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account_update_request' in params:
            body_params = params['account_update_request']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuthScheme']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Account',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
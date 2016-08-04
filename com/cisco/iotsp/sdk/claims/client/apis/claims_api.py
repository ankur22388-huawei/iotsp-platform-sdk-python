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

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ClaimsApi(object):
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

    def create_claim(self, claim_create_request, **kwargs):
        """
        Create a claim.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_claim(claim_create_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ThingClaimRequest claim_create_request: claim to create (required)
        :return: ThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_claim_with_http_info(claim_create_request, **kwargs)
        else:
            (data) = self.create_claim_with_http_info(claim_create_request, **kwargs)
            return data

    def create_claim_with_http_info(self, claim_create_request, **kwargs):
        """
        Create a claim.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_claim_with_http_info(claim_create_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ThingClaimRequest claim_create_request: claim to create (required)
        :return: ThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['claim_create_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_claim" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'claim_create_request' is set
        if ('claim_create_request' not in params) or (params['claim_create_request'] is None):
            raise ValueError("Missing the required parameter `claim_create_request` when calling `create_claim`")

        resource_path = '/v1/thing-services/claims'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'claim_create_request' in params:
            body_params = params['claim_create_request']

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
                                            response_type='ThingClaim',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def delete_claim(self, claim_uid, **kwargs):
        """
        Delete a claim.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_claim(claim_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str claim_uid: Uid of claim (required)
        :return: ThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_claim_with_http_info(claim_uid, **kwargs)
        else:
            (data) = self.delete_claim_with_http_info(claim_uid, **kwargs)
            return data

    def delete_claim_with_http_info(self, claim_uid, **kwargs):
        """
        Delete a claim.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_claim_with_http_info(claim_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str claim_uid: Uid of claim (required)
        :return: ThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['claim_uid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_claim" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'claim_uid' is set
        if ('claim_uid' not in params) or (params['claim_uid'] is None):
            raise ValueError("Missing the required parameter `claim_uid` when calling `delete_claim`")

        resource_path = '/v1/thing-services/claims/{claimUid}'.replace('{format}', 'json')
        path_params = {}
        if 'claim_uid' in params:
            path_params['claimUid'] = params['claim_uid']

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
                                            response_type='ThingClaim',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_claim(self, claim_uid, **kwargs):
        """
        Get a claim by claim uid.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_claim(claim_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str claim_uid: Uid of claim (required)
        :return: ThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_claim_with_http_info(claim_uid, **kwargs)
        else:
            (data) = self.get_claim_with_http_info(claim_uid, **kwargs)
            return data

    def get_claim_with_http_info(self, claim_uid, **kwargs):
        """
        Get a claim by claim uid.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_claim_with_http_info(claim_uid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str claim_uid: Uid of claim (required)
        :return: ThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['claim_uid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_claim" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'claim_uid' is set
        if ('claim_uid' not in params) or (params['claim_uid'] is None):
            raise ValueError("Missing the required parameter `claim_uid` when calling `get_claim`")

        resource_path = '/v1/thing-services/claims/{claimUid}'.replace('{format}', 'json')
        path_params = {}
        if 'claim_uid' in params:
            path_params['claimUid'] = params['claim_uid']

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
                                            response_type='ThingClaim',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_claims(self, **kwargs):
        """
        Get claims using query string parameters.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_claims(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key: key to search on
        :param str value: value to search on
        :param str sort_key: sort by a key
        :param str sort_order: sort in ascending or descending order
        :param int limit: maximum number of thing claims to return
        :param int offset: starting index of thing claims in return payload
        :return: PageThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_claims_with_http_info(**kwargs)
        else:
            (data) = self.get_claims_with_http_info(**kwargs)
            return data

    def get_claims_with_http_info(self, **kwargs):
        """
        Get claims using query string parameters.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_claims_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key: key to search on
        :param str value: value to search on
        :param str sort_key: sort by a key
        :param str sort_order: sort in ascending or descending order
        :param int limit: maximum number of thing claims to return
        :param int offset: starting index of thing claims in return payload
        :return: PageThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'value', 'sort_key', 'sort_order', 'limit', 'offset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_claims" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/thing-services/claims'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'key' in params:
            query_params['key'] = params['key']
        if 'value' in params:
            query_params['value'] = params['value']
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
                                            response_type='PageThingClaim',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_claims_by_filter(self, filter, **kwargs):
        """
        Get a page of thing claims by filter
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_claims_by_filter(filter, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ThingClaimFilter filter: The filter criteria on which to return paginated thing claims (required)
        :return: PageThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_claims_by_filter_with_http_info(filter, **kwargs)
        else:
            (data) = self.get_claims_by_filter_with_http_info(filter, **kwargs)
            return data

    def get_claims_by_filter_with_http_info(self, filter, **kwargs):
        """
        Get a page of thing claims by filter
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_claims_by_filter_with_http_info(filter, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ThingClaimFilter filter: The filter criteria on which to return paginated thing claims (required)
        :return: PageThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_claims_by_filter" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filter' is set
        if ('filter' not in params) or (params['filter'] is None):
            raise ValueError("Missing the required parameter `filter` when calling `get_claims_by_filter`")

        resource_path = '/v1/thing-services/claims/actions/getPageByFilter'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'filter' in params:
            body_params = params['filter']

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
                                            response_type='PageThingClaim',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_claim(self, claim_uid, claim_update_request, **kwargs):
        """
        Update a claim.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_claim(claim_uid, claim_update_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str claim_uid: Uid of claim (required)
        :param ThingClaimUpdateRequest claim_update_request: Updated claim object (required)
        :return: ThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_claim_with_http_info(claim_uid, claim_update_request, **kwargs)
        else:
            (data) = self.update_claim_with_http_info(claim_uid, claim_update_request, **kwargs)
            return data

    def update_claim_with_http_info(self, claim_uid, claim_update_request, **kwargs):
        """
        Update a claim.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_claim_with_http_info(claim_uid, claim_update_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str claim_uid: Uid of claim (required)
        :param ThingClaimUpdateRequest claim_update_request: Updated claim object (required)
        :return: ThingClaim
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['claim_uid', 'claim_update_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_claim" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'claim_uid' is set
        if ('claim_uid' not in params) or (params['claim_uid'] is None):
            raise ValueError("Missing the required parameter `claim_uid` when calling `update_claim`")
        # verify the required parameter 'claim_update_request' is set
        if ('claim_update_request' not in params) or (params['claim_update_request'] is None):
            raise ValueError("Missing the required parameter `claim_update_request` when calling `update_claim`")

        resource_path = '/v1/thing-services/claims/{claimUid}'.replace('{format}', 'json')
        path_params = {}
        if 'claim_uid' in params:
            path_params['claimUid'] = params['claim_uid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'claim_update_request' in params:
            body_params = params['claim_update_request']

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
                                            response_type='ThingClaim',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
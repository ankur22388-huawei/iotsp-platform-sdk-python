#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
from distutils.core import setup

REQUIRES = ["requests>=2.10.0", "urllib3 >= 1.15.1", "six >= 1.8.0", "certifi", "python-dateutil"]
setup(
    name='iotsp-sdk-python',
    version='1.0.0',
    packages=['com', 'com.cisco', 'com.cisco.iotsp', 'com.cisco.iotsp.sdk', 'com.cisco.iotsp.sdk.users',
              'com.cisco.iotsp.sdk.users.client', 'com.cisco.iotsp.sdk.users.client.apis',
              'com.cisco.iotsp.sdk.users.client.models', 'com.cisco.iotsp.sdk.claims',
              'com.cisco.iotsp.sdk.claims.client', 'com.cisco.iotsp.sdk.claims.client.apis',
              'com.cisco.iotsp.sdk.claims.client.models', 'com.cisco.iotsp.sdk.things',
              'com.cisco.iotsp.sdk.things.client', 'com.cisco.iotsp.sdk.things.client.apis',
              'com.cisco.iotsp.sdk.things.client.models', 'com.cisco.iotsp.sdk.acounts',
              'com.cisco.iotsp.sdk.acounts.client', 'com.cisco.iotsp.sdk.acounts.client.apis',
              'com.cisco.iotsp.sdk.acounts.client.models', 'com.cisco.iotsp.sdk.schemas',
              'com.cisco.iotsp.sdk.schemas.client', 'com.cisco.iotsp.sdk.schemas.client.apis',
              'com.cisco.iotsp.sdk.schemas.client.models', 'com.cisco.iotsp.sdk.presence',
              'com.cisco.iotsp.sdk.presence.client', 'com.cisco.iotsp.sdk.presence.client.apis',
              'com.cisco.iotsp.sdk.presence.client.models', 'com.cisco.iotsp.sdk.observations',
              'com.cisco.iotsp.sdk.observations.client', 'com.cisco.iotsp.sdk.observations.client.apis',
              'com.cisco.iotsp.sdk.observations.client.models', 'com.cisco.iotsp.sdk.registration',
              'com.cisco.iotsp.sdk.registration.client', 'com.cisco.iotsp.sdk.registration.client.apis',
              'com.cisco.iotsp.sdk.registration.client.models', 'com.cisco.iotsp.sdk.thing_credentials',
              'com.cisco.iotsp.sdk.thing_credentials.client', 'com.cisco.iotsp.sdk.thing_credentials.client.apis',
              'com.cisco.iotsp.sdk.thing_credentials.client.models', 'com.cisco.iotsp.sdk.http_device_connector',
              'com.cisco.iotsp.sdk.http_device_connector.client',
              'com.cisco.iotsp.sdk.http_device_connector.client.apis',
              'com.cisco.iotsp.sdk.http_device_connector.client.models', 'com.cisco.iotsp.test',
              'com.cisco.iotsp.helper', 'com.cisco.iotsp.sample', 'com.cisco.iotsp.sample.data', 'com.cisco.iotsp.sample.workflow'],
    package_data={'com.cisco.iotsp.sample.data': ['*.json'], 'com.cisco.iotsp' :['*.properties']},
    include_package_data=True,
    url='https://github.com/CiscoDevNet/iotsp-platform-sdk-python',
    license='License.pdf',
    author='Melinda Xiao-Devins',
    author_email='mexiaode@cisco.com',
    description='Cisco IOT software platform SDK in Python'
)

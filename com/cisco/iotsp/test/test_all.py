#Copyright (c) 2016 by Cisco Systems, Inc. All rights reserved.
from __future__ import absolute_import

import ConfigParser
import os.path
import os
import time
import random
import string

from com.cisco.iotsp.test import test_api
from com.cisco.iotsp.test import test_workflow

def read_config():
    try:
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "..", "services.properties"))

        section = 'servicesSection'
        Config = ConfigParser.ConfigParser()
        Config.read(filepath)

        #print Config.sections()
        services = {}
        options = Config.options(section)
        for option in options:
            try:
                services[option] = Config.get(section, option)
                if services[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                services[option] = None

        return services
    except Exception as e:
        print (str(e))

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

account_alias = id_generator();

service_config = read_config()
service_address = service_config['service_address']

success_api = True
api_test = test_api.TestApi(service_address)
success_api = api_test.Test(service_address, account_alias)

account_alias = id_generator();
wf_test = test_workflow.TestWorkflow(service_address)
success_workflow = wf_test.Test(service_address,account_alias)
if(success_api & success_workflow) :
    print("========  All Test is successful ========== ")
else:
    print("========  Some Test failed ========== ")
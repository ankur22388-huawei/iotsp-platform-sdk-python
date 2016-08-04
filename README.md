# Cisco IOT Software Platform SDK in Python

## Description

A software development kit to enable you to build Python applications on the IOT Software Platform.

## Getting Started

1. Download or clone Cisco IOT Software Platform SDK in Python
2. Install Python 2.7
3. Run the following command to install the required libraries listed in requirements.txt:
    pip install -r requirements.txt
4. Choose the IoTSP services, and import the corresponding packages under com/cisco/iotsp/sdk into your Python application

Once downloaded or cloned, you will see a project structure like below:
```shell

├── com
|   ├── cisco
|      └── iotsp
|          ├── helper                          # helper package that a cloud app can import
|          |   └── account_helper.py           # helper class to create an account with IoTSP
|          |   └── authentication_helper.py    # helper class togenerate access token used to communicate with IoTSP
|          ├── sample                          # sample code on how cloud app can communicate with IoTSP's services
|          |   └── workflow                    # sample code on how to implement several use cases
|          |   └── data                        # sample data files used by sample code
|          ├── sdk                             # Libary packages for a cloud app to import and use to communicate with IoTSP services
|          |   └── accounts                    # Libary package to communicate with IoTSP accounts service
|          |   └── claims                      # Libary package to communicate with IoTSP claims service
|          |   └── http_device_connector       # Libary package to communicate with IoTSP http_device_connector service
|          |   └── observations                # Libary package to communicate with IoTSP observations service
|          |   └── presence                    # Libary package to communicate with IoTSP presence service
|          |   └── registration                # Libary package to communicate with IoTSP registration service
|          |   └── schemas                     # Libary package to communicate with IoTSP schemas service
|          |   └── thing_credentials           # Libary package to communicate with IoTSP thing_credentials service
|          |   └── things                      # Libary package to communicate with IoTSP things service
|          |   └── users                       # Libary package to communicate with IoTSP users service
|          └── test                            # testing app that a cloud app developer may run to step into each sample code
|              └── test_all.py                 # testing app that test all the sample code
|              └── test_api.py                 # testing class that test sample code under sample\
|              └── test_workflow.py            # testing calss that test sample code under sample\workflow
├── services.properties                        # contains IoTSP cluster IP address that test_all.py uses to run testing app
└── requirements.txt                           # contains required libraries
```
***Note: when run testing app, it creates accounts, users, schemas, devices on IoTSP, then delete all of them if testing app is ran successfully.

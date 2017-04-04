# coding: utf-8

"""
    Samsara API

    # Introduction The Samsara REST API lets you interact with the Samsara Cloud from anything that can send an HTTP request. With the Samsara API you can build powerful applications and custom solutions with sensor data.  Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets. If you’re familiar with what you can build with a REST API, the following API reference guide will be your go-to resource.  API access to the Samsara cloud is available to all Samsara administrators. If you’d like to try the API, [contact us](https://www.samsara.com/free-trial). The API is currently in beta and may be subject to frequent changes.  # Connecting to the API There are two ways to connect to the API. If you prefer to use the API in Javascript or Python, we supply SDKs which you can download here: [Javascript SDK](https://github.com/samsarahq/samsara-js), [Python SDK](https://github.com/samsarahq/samsara-python).  If you’d rather use another language to interact with the Samsara API, the endpoints and examples are in the reference guide below.  

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import samsara
from samsara.rest import ApiException
from samsara.models.hos_authentication_logs_response_authentication_logs import HosAuthenticationLogsResponseAuthenticationLogs


class TestHosAuthenticationLogsResponseAuthenticationLogs(unittest.TestCase):
    """ HosAuthenticationLogsResponseAuthenticationLogs unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHosAuthenticationLogsResponseAuthenticationLogs(self):
        """
        Test HosAuthenticationLogsResponseAuthenticationLogs
        """
        model = samsara.models.hos_authentication_logs_response_authentication_logs.HosAuthenticationLogsResponseAuthenticationLogs()


if __name__ == '__main__':
    unittest.main()

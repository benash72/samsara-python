# coding: utf-8

"""
    Samsara API

    # Introduction The Samsara REST API lets you interact with the Samsara Cloud from anything that can send an HTTP request. With the Samsara API you can build powerful applications and custom solutions with sensor data.  Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets. If you’re familiar with what you can build with a REST API, the following API reference guide will be your go-to resource.  API access to the Samsara cloud is available to all Samsara administrators. If you’d like to try the API, [contact us](https://www.samsara.com/free-trial). The API is currently in beta and may be subject to frequent changes.  # Connecting to the API There are two ways to connect to the API. If you prefer to use the API in Javascript or Python, we supply SDKs which you can download here: [Javascript SDK](https://github.com/samsarahq/samsara-js), [Python SDK](https://github.com/samsarahq/samsara-python).  If you’d rather use another language to interact with the Samsara API, the endpoints and examples are in the reference guide below.  

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


class DriversSummaryParam(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, org_id=None, start_ms=None, end_ms=None):
        """
        DriversSummaryParam - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'org_id': 'int',
            'start_ms': 'int',
            'end_ms': 'int'
        }

        self.attribute_map = {
            'org_id': 'orgId',
            'start_ms': 'startMs',
            'end_ms': 'endMs'
        }

        self._org_id = org_id
        self._start_ms = start_ms
        self._end_ms = end_ms

    @property
    def org_id(self):
        """
        Gets the org_id of this DriversSummaryParam.
        Org ID to query.

        :return: The org_id of this DriversSummaryParam.
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """
        Sets the org_id of this DriversSummaryParam.
        Org ID to query.

        :param org_id: The org_id of this DriversSummaryParam.
        :type: int
        """

        self._org_id = org_id

    @property
    def start_ms(self):
        """
        Gets the start_ms of this DriversSummaryParam.
        Start time (ms) of queried time period.

        :return: The start_ms of this DriversSummaryParam.
        :rtype: int
        """
        return self._start_ms

    @start_ms.setter
    def start_ms(self, start_ms):
        """
        Sets the start_ms of this DriversSummaryParam.
        Start time (ms) of queried time period.

        :param start_ms: The start_ms of this DriversSummaryParam.
        :type: int
        """

        self._start_ms = start_ms

    @property
    def end_ms(self):
        """
        Gets the end_ms of this DriversSummaryParam.
        End time (ms) of queried time period.

        :return: The end_ms of this DriversSummaryParam.
        :rtype: int
        """
        return self._end_ms

    @end_ms.setter
    def end_ms(self, end_ms):
        """
        Sets the end_ms of this DriversSummaryParam.
        End time (ms) of queried time period.

        :param end_ms: The end_ms of this DriversSummaryParam.
        :type: int
        """

        self._end_ms = end_ms

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

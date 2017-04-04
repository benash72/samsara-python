# coding: utf-8

"""
    Samsara API

    # Introduction The Samsara REST API lets you interact with the Samsara Cloud from anything that can send an HTTP request. With the Samsara API you can build powerful applications and custom solutions with sensor data.  Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets. If you’re familiar with what you can build with a REST API, the following API reference guide will be your go-to resource.  API access to the Samsara cloud is available to all Samsara administrators. If you’d like to try the API, [contact us](https://www.samsara.com/free-trial). The API is currently in beta and may be subject to frequent changes.  # Connecting to the API There are two ways to connect to the API. If you prefer to use the API in Javascript or Python, we supply SDKs which you can download here: [Javascript SDK](https://github.com/samsarahq/samsara-js), [Python SDK](https://github.com/samsarahq/samsara-python).  If you’d rather use another language to interact with the Samsara API, the endpoints and examples are in the reference guide below.  

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HosAuthenticationLogsResponseAuthenticationLogs(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, action_type=None, happened_at_ms=None, city=None, state=None, address_name=None, address=None):
        """
        HosAuthenticationLogsResponseAuthenticationLogs - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action_type': 'str',
            'happened_at_ms': 'int',
            'city': 'str',
            'state': 'str',
            'address_name': 'str',
            'address': 'str'
        }

        self.attribute_map = {
            'action_type': 'actionType',
            'happened_at_ms': 'happenedAtMs',
            'city': 'city',
            'state': 'state',
            'address_name': 'addressName',
            'address': 'address'
        }

        self._action_type = action_type
        self._happened_at_ms = happened_at_ms
        self._city = city
        self._state = state
        self._address_name = address_name
        self._address = address

    @property
    def action_type(self):
        """
        Gets the action_type of this HosAuthenticationLogsResponseAuthenticationLogs.
        The log type - one of 'signin' or 'signout'

        :return: The action_type of this HosAuthenticationLogsResponseAuthenticationLogs.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this HosAuthenticationLogsResponseAuthenticationLogs.
        The log type - one of 'signin' or 'signout'

        :param action_type: The action_type of this HosAuthenticationLogsResponseAuthenticationLogs.
        :type: str
        """

        self._action_type = action_type

    @property
    def happened_at_ms(self):
        """
        Gets the happened_at_ms of this HosAuthenticationLogsResponseAuthenticationLogs.
        The time at which the event was recorded in UNIX milliseconds.

        :return: The happened_at_ms of this HosAuthenticationLogsResponseAuthenticationLogs.
        :rtype: int
        """
        return self._happened_at_ms

    @happened_at_ms.setter
    def happened_at_ms(self, happened_at_ms):
        """
        Sets the happened_at_ms of this HosAuthenticationLogsResponseAuthenticationLogs.
        The time at which the event was recorded in UNIX milliseconds.

        :param happened_at_ms: The happened_at_ms of this HosAuthenticationLogsResponseAuthenticationLogs.
        :type: int
        """

        self._happened_at_ms = happened_at_ms

    @property
    def city(self):
        """
        Gets the city of this HosAuthenticationLogsResponseAuthenticationLogs.
        City in which the log was recorded, if applicable.

        :return: The city of this HosAuthenticationLogsResponseAuthenticationLogs.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this HosAuthenticationLogsResponseAuthenticationLogs.
        City in which the log was recorded, if applicable.

        :param city: The city of this HosAuthenticationLogsResponseAuthenticationLogs.
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """
        Gets the state of this HosAuthenticationLogsResponseAuthenticationLogs.
        State in which the log was recorded, if applicable.

        :return: The state of this HosAuthenticationLogsResponseAuthenticationLogs.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this HosAuthenticationLogsResponseAuthenticationLogs.
        State in which the log was recorded, if applicable.

        :param state: The state of this HosAuthenticationLogsResponseAuthenticationLogs.
        :type: str
        """

        self._state = state

    @property
    def address_name(self):
        """
        Gets the address_name of this HosAuthenticationLogsResponseAuthenticationLogs.
        Address name from the group address book at which the log was recorded, if applicable.

        :return: The address_name of this HosAuthenticationLogsResponseAuthenticationLogs.
        :rtype: str
        """
        return self._address_name

    @address_name.setter
    def address_name(self, address_name):
        """
        Sets the address_name of this HosAuthenticationLogsResponseAuthenticationLogs.
        Address name from the group address book at which the log was recorded, if applicable.

        :param address_name: The address_name of this HosAuthenticationLogsResponseAuthenticationLogs.
        :type: str
        """

        self._address_name = address_name

    @property
    def address(self):
        """
        Gets the address of this HosAuthenticationLogsResponseAuthenticationLogs.
        Address at which the log was recorded, if applicable.

        :return: The address of this HosAuthenticationLogsResponseAuthenticationLogs.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this HosAuthenticationLogsResponseAuthenticationLogs.
        Address at which the log was recorded, if applicable.

        :param address: The address of this HosAuthenticationLogsResponseAuthenticationLogs.
        :type: str
        """

        self._address = address

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
        if not isinstance(other, HosAuthenticationLogsResponseAuthenticationLogs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class TripResponseTrips(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, start_ms=None, start_coordinates=None, start_location=None, end_ms=None, end_coordinates=None, end_location=None, distance_meters=None):
        """
        TripResponseTrips - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_ms': 'int',
            'start_coordinates': 'TripResponseStartCoordinates',
            'start_location': 'str',
            'end_ms': 'int',
            'end_coordinates': 'TripResponseEndCoordinates',
            'end_location': 'str',
            'distance_meters': 'int'
        }

        self.attribute_map = {
            'start_ms': 'startMs',
            'start_coordinates': 'startCoordinates',
            'start_location': 'startLocation',
            'end_ms': 'endMs',
            'end_coordinates': 'endCoordinates',
            'end_location': 'endLocation',
            'distance_meters': 'distanceMeters'
        }

        self._start_ms = start_ms
        self._start_coordinates = start_coordinates
        self._start_location = start_location
        self._end_ms = end_ms
        self._end_coordinates = end_coordinates
        self._end_location = end_location
        self._distance_meters = distance_meters

    @property
    def start_ms(self):
        """
        Gets the start_ms of this TripResponseTrips.
        Beginning of the trip in UNIX milliseconds.

        :return: The start_ms of this TripResponseTrips.
        :rtype: int
        """
        return self._start_ms

    @start_ms.setter
    def start_ms(self, start_ms):
        """
        Sets the start_ms of this TripResponseTrips.
        Beginning of the trip in UNIX milliseconds.

        :param start_ms: The start_ms of this TripResponseTrips.
        :type: int
        """

        self._start_ms = start_ms

    @property
    def start_coordinates(self):
        """
        Gets the start_coordinates of this TripResponseTrips.

        :return: The start_coordinates of this TripResponseTrips.
        :rtype: TripResponseStartCoordinates
        """
        return self._start_coordinates

    @start_coordinates.setter
    def start_coordinates(self, start_coordinates):
        """
        Sets the start_coordinates of this TripResponseTrips.

        :param start_coordinates: The start_coordinates of this TripResponseTrips.
        :type: TripResponseStartCoordinates
        """

        self._start_coordinates = start_coordinates

    @property
    def start_location(self):
        """
        Gets the start_location of this TripResponseTrips.
        Text representation of nearest identifiable location to the start (latitude, longitude) coordinates.

        :return: The start_location of this TripResponseTrips.
        :rtype: str
        """
        return self._start_location

    @start_location.setter
    def start_location(self, start_location):
        """
        Sets the start_location of this TripResponseTrips.
        Text representation of nearest identifiable location to the start (latitude, longitude) coordinates.

        :param start_location: The start_location of this TripResponseTrips.
        :type: str
        """

        self._start_location = start_location

    @property
    def end_ms(self):
        """
        Gets the end_ms of this TripResponseTrips.
        End of the trip in UNIX milliseconds.

        :return: The end_ms of this TripResponseTrips.
        :rtype: int
        """
        return self._end_ms

    @end_ms.setter
    def end_ms(self, end_ms):
        """
        Sets the end_ms of this TripResponseTrips.
        End of the trip in UNIX milliseconds.

        :param end_ms: The end_ms of this TripResponseTrips.
        :type: int
        """

        self._end_ms = end_ms

    @property
    def end_coordinates(self):
        """
        Gets the end_coordinates of this TripResponseTrips.

        :return: The end_coordinates of this TripResponseTrips.
        :rtype: TripResponseEndCoordinates
        """
        return self._end_coordinates

    @end_coordinates.setter
    def end_coordinates(self, end_coordinates):
        """
        Sets the end_coordinates of this TripResponseTrips.

        :param end_coordinates: The end_coordinates of this TripResponseTrips.
        :type: TripResponseEndCoordinates
        """

        self._end_coordinates = end_coordinates

    @property
    def end_location(self):
        """
        Gets the end_location of this TripResponseTrips.
        Text representation of nearest identifiable location to the end (latitude, longitude) coordinates.

        :return: The end_location of this TripResponseTrips.
        :rtype: str
        """
        return self._end_location

    @end_location.setter
    def end_location(self, end_location):
        """
        Sets the end_location of this TripResponseTrips.
        Text representation of nearest identifiable location to the end (latitude, longitude) coordinates.

        :param end_location: The end_location of this TripResponseTrips.
        :type: str
        """

        self._end_location = end_location

    @property
    def distance_meters(self):
        """
        Gets the distance_meters of this TripResponseTrips.
        Length of the trip in meters.

        :return: The distance_meters of this TripResponseTrips.
        :rtype: int
        """
        return self._distance_meters

    @distance_meters.setter
    def distance_meters(self, distance_meters):
        """
        Sets the distance_meters of this TripResponseTrips.
        Length of the trip in meters.

        :param distance_meters: The distance_meters of this TripResponseTrips.
        :type: int
        """

        self._distance_meters = distance_meters

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
        if not isinstance(other, TripResponseTrips):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

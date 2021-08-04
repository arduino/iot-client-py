# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from arduino_iot_rest.configuration import Configuration


class ArduinoSeriesRawLastValueResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'count_values': 'int'
        'property_id': 'str'
        'thing_id': 'str'
        'times': '[datetime]'
        'values': '[bool, date, datetime, dict, float, int, list, str, none_type]'
    }

    attribute_map = {
        'count_values': 'count_values'
        'property_id': 'property_id'
        'thing_id': 'thing_id'
        'times': 'times'
        'values': 'values'
    }

    def __init__(self, count_values=None, property_id=None, thing_id=None, times=None, values=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoSeriesRawLastValueResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count_values = None
        self._property_id = None
        self._thing_id = None
        self._times = None
        self._values = None
        self.discriminator = None

        self.count_values = count_values
        self.property_id = property_id
        self.thing_id = thing_id
        self.times = times
        self.values = values

    @property
    def count_values(self):
        """Gets the count_values of this ArduinoSeriesRawLastValueResponse.  # noqa: E501

        Total number of values in the array 'values'  # noqa: E501

        :return: The count_values of this ArduinoSeriesRawLastValueResponse.  # noqa: E501
        :rtype: int
        """
        return self._count_values

    @count_values.setter
    def count_values(self, count_values):
        """Sets the count_values of this ArduinoSeriesRawLastValueResponse.

        Total number of values in the array 'values'  # noqa: E501

        :param count_values: The count_values of this ArduinoSeriesRawLastValueResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and count_values is None:  # noqa: E501
            raise ValueError("Invalid value for `count_values`, must not be `None`")  # noqa: E501

        self._count_values = count_values

    @property
    def property_id(self):
        """Gets the property_id of this ArduinoSeriesRawLastValueResponse.  # noqa: E501

        Property id  # noqa: E501

        :return: The property_id of this ArduinoSeriesRawLastValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this ArduinoSeriesRawLastValueResponse.

        Property id  # noqa: E501

        :param property_id: The property_id of this ArduinoSeriesRawLastValueResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and property_id is None:  # noqa: E501
            raise ValueError("Invalid value for `property_id`, must not be `None`")  # noqa: E501

        self._property_id = property_id

    @property
    def thing_id(self):
        """Gets the thing_id of this ArduinoSeriesRawLastValueResponse.  # noqa: E501

        Thing id  # noqa: E501

        :return: The thing_id of this ArduinoSeriesRawLastValueResponse.  # noqa: E501
        :rtype: str
        """
        return self._thing_id

    @thing_id.setter
    def thing_id(self, thing_id):
        """Sets the thing_id of this ArduinoSeriesRawLastValueResponse.

        Thing id  # noqa: E501

        :param thing_id: The thing_id of this ArduinoSeriesRawLastValueResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and thing_id is None:  # noqa: E501
            raise ValueError("Invalid value for `thing_id`, must not be `None`")  # noqa: E501

        self._thing_id = thing_id

    @property
    def times(self):
        """Gets the times of this ArduinoSeriesRawLastValueResponse.  # noqa: E501

        Timestamp in RFC3339  # noqa: E501

        :return: The times of this ArduinoSeriesRawLastValueResponse.  # noqa: E501
        :rtype: [datetime]
        """
        return self._times

    @times.setter
    def times(self, times):
        """Sets the times of this ArduinoSeriesRawLastValueResponse.

        Timestamp in RFC3339  # noqa: E501

        :param times: The times of this ArduinoSeriesRawLastValueResponse.  # noqa: E501
        :type: [datetime]
        """
        if self.local_vars_configuration.client_side_validation and times is None:  # noqa: E501
            raise ValueError("Invalid value for `times`, must not be `None`")  # noqa: E501

        self._times = times

    @property
    def values(self):
        """Gets the values of this ArduinoSeriesRawLastValueResponse.  # noqa: E501

        Values can be in Float, String, Bool, Object  # noqa: E501

        :return: The values of this ArduinoSeriesRawLastValueResponse.  # noqa: E501
        :rtype: [bool, date, datetime, dict, float, int, list, str, none_type]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ArduinoSeriesRawLastValueResponse.

        Values can be in Float, String, Bool, Object  # noqa: E501

        :param values: The values of this ArduinoSeriesRawLastValueResponse.  # noqa: E501
        :type: [bool, date, datetime, dict, float, int, list, str, none_type]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArduinoSeriesRawLastValueResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoSeriesRawLastValueResponse):
            return True

        return self.to_dict() != other.to_dict()

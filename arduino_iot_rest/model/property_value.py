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


class PropertyValue(object):
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
        'device_id': 'str'
        'value': 'bool, date, datetime, dict, float, int, list, str, none_type'
    }

    attribute_map = {
        'device_id': 'device_id'
        'value': 'value'
    }

    def __init__(self, device_id=None, value=None, local_vars_configuration=None):  # noqa: E501
        """PropertyValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._value = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        self.value = value

    @property
    def device_id(self):
        """Gets the device_id of this PropertyValue.  # noqa: E501

        The device who send the property  # noqa: E501

        :return: The device_id of this PropertyValue.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this PropertyValue.

        The device who send the property  # noqa: E501

        :param device_id: The device_id of this PropertyValue.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def value(self):
        """Gets the value of this PropertyValue.  # noqa: E501

        The property value  # noqa: E501

        :return: The value of this PropertyValue.  # noqa: E501
        :rtype: bool, date, datetime, dict, float, int, list, str, none_type
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PropertyValue.

        The property value  # noqa: E501

        :param value: The value of this PropertyValue.  # noqa: E501
        :type: bool, date, datetime, dict, float, int, list, str, none_type
        """

        self._value = value

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
        if not isinstance(other, PropertyValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PropertyValue):
            return True

        return self.to_dict() != other.to_dict()

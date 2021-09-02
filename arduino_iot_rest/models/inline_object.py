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


class InlineObject(object):
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
        'expire_in_mins': 'int',
        'ota_file': 'file'
    }

    attribute_map = {
        'expire_in_mins': 'expire_in_mins',
        'ota_file': 'ota_file'
    }

    def __init__(self, expire_in_mins=10, ota_file=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._expire_in_mins = None
        self._ota_file = None
        self.discriminator = None

        if expire_in_mins is not None:
            self.expire_in_mins = expire_in_mins
        self.ota_file = ota_file

    @property
    def expire_in_mins(self):
        """Gets the expire_in_mins of this InlineObject.  # noqa: E501

        Binary expire time in minutes, default 10 mins  # noqa: E501

        :return: The expire_in_mins of this InlineObject.  # noqa: E501
        :rtype: int
        """
        return self._expire_in_mins

    @expire_in_mins.setter
    def expire_in_mins(self, expire_in_mins):
        """Sets the expire_in_mins of this InlineObject.

        Binary expire time in minutes, default 10 mins  # noqa: E501

        :param expire_in_mins: The expire_in_mins of this InlineObject.  # noqa: E501
        :type: int
        """

        self._expire_in_mins = expire_in_mins

    @property
    def ota_file(self):
        """Gets the ota_file of this InlineObject.  # noqa: E501

        OTA file  # noqa: E501

        :return: The ota_file of this InlineObject.  # noqa: E501
        :rtype: file
        """
        return self._ota_file

    @ota_file.setter
    def ota_file(self, ota_file):
        """Sets the ota_file of this InlineObject.

        OTA file  # noqa: E501

        :param ota_file: The ota_file of this InlineObject.  # noqa: E501
        :type: file
        """
        if self.local_vars_configuration.client_side_validation and ota_file is None:  # noqa: E501
            raise ValueError("Invalid value for `ota_file`, must not be `None`")  # noqa: E501

        self._ota_file = ota_file

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
        if not isinstance(other, InlineObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject):
            return True

        return self.to_dict() != other.to_dict()

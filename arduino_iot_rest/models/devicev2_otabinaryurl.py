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


class Devicev2Otabinaryurl(object):
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
        '_async': 'bool',
        'binary_key': 'str',
        'expire_in_mins': 'int'
    }

    attribute_map = {
        '_async': 'async',
        'binary_key': 'binary_key',
        'expire_in_mins': 'expire_in_mins'
    }

    def __init__(self, _async=True, binary_key=None, expire_in_mins=10, local_vars_configuration=None):  # noqa: E501
        """Devicev2Otabinaryurl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__async = None
        self._binary_key = None
        self._expire_in_mins = None
        self.discriminator = None

        if _async is not None:
            self._async = _async
        self.binary_key = binary_key
        if expire_in_mins is not None:
            self.expire_in_mins = expire_in_mins

    @property
    def _async(self):
        """Gets the _async of this Devicev2Otabinaryurl.  # noqa: E501

        If false, wait for the full OTA process, until it gets a result from the device  # noqa: E501

        :return: The _async of this Devicev2Otabinaryurl.  # noqa: E501
        :rtype: bool
        """
        return self.__async

    @_async.setter
    def _async(self, _async):
        """Sets the _async of this Devicev2Otabinaryurl.

        If false, wait for the full OTA process, until it gets a result from the device  # noqa: E501

        :param _async: The _async of this Devicev2Otabinaryurl.  # noqa: E501
        :type: bool
        """

        self.__async = _async

    @property
    def binary_key(self):
        """Gets the binary_key of this Devicev2Otabinaryurl.  # noqa: E501

        The object key of the binary  # noqa: E501

        :return: The binary_key of this Devicev2Otabinaryurl.  # noqa: E501
        :rtype: str
        """
        return self._binary_key

    @binary_key.setter
    def binary_key(self, binary_key):
        """Sets the binary_key of this Devicev2Otabinaryurl.

        The object key of the binary  # noqa: E501

        :param binary_key: The binary_key of this Devicev2Otabinaryurl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and binary_key is None:  # noqa: E501
            raise ValueError("Invalid value for `binary_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                binary_key is not None and not re.search(r'^ota\/[a-zA-Z0-9_-]+\/[a-zA-Z0-9_-]+.ota$', binary_key)):  # noqa: E501
            raise ValueError(r"Invalid value for `binary_key`, must be a follow pattern or equal to `/^ota\/[a-zA-Z0-9_-]+\/[a-zA-Z0-9_-]+.ota$/`")  # noqa: E501

        self._binary_key = binary_key

    @property
    def expire_in_mins(self):
        """Gets the expire_in_mins of this Devicev2Otabinaryurl.  # noqa: E501

        Binary expire time in minutes, default 10 mins  # noqa: E501

        :return: The expire_in_mins of this Devicev2Otabinaryurl.  # noqa: E501
        :rtype: int
        """
        return self._expire_in_mins

    @expire_in_mins.setter
    def expire_in_mins(self, expire_in_mins):
        """Sets the expire_in_mins of this Devicev2Otabinaryurl.

        Binary expire time in minutes, default 10 mins  # noqa: E501

        :param expire_in_mins: The expire_in_mins of this Devicev2Otabinaryurl.  # noqa: E501
        :type: int
        """

        self._expire_in_mins = expire_in_mins

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
        if not isinstance(other, Devicev2Otabinaryurl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Devicev2Otabinaryurl):
            return True

        return self.to_dict() != other.to_dict()

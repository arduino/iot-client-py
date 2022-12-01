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

from iot_api_client.configuration import Configuration


class BatchLastValueRequestsMediaV1(object):
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
        'requests': 'list[BatchQueryRawLastValueRequestMediaV1]'
    }

    attribute_map = {
        'requests': 'requests'
    }

    def __init__(self, requests=None, local_vars_configuration=None):  # noqa: E501
        """BatchLastValueRequestsMediaV1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._requests = None
        self.discriminator = None

        self.requests = requests

    @property
    def requests(self):
        """Gets the requests of this BatchLastValueRequestsMediaV1.  # noqa: E501

        Requests  # noqa: E501

        :return: The requests of this BatchLastValueRequestsMediaV1.  # noqa: E501
        :rtype: list[BatchQueryRawLastValueRequestMediaV1]
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this BatchLastValueRequestsMediaV1.

        Requests  # noqa: E501

        :param requests: The requests of this BatchLastValueRequestsMediaV1.  # noqa: E501
        :type: list[BatchQueryRawLastValueRequestMediaV1]
        """
        if self.local_vars_configuration.client_side_validation and requests is None:  # noqa: E501
            raise ValueError("Invalid value for `requests`, must not be `None`")  # noqa: E501

        self._requests = requests

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
        if not isinstance(other, BatchLastValueRequestsMediaV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchLastValueRequestsMediaV1):
            return True

        return self.to_dict() != other.to_dict()

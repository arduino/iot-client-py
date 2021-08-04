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


class ArduinoDevicev2EventProperties(object):
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
        'events': 'ArduinoDevicev2SimplePropertiesCollection'
        'id': 'str'
    }

    attribute_map = {
        'events': 'events'
        'id': 'id'
    }

    def __init__(self, events=None, id=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoDevicev2EventProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._events = None
        self._id = None
        self.discriminator = None

        self.events = events
        self.id = id

    @property
    def events(self):
        """Gets the events of this ArduinoDevicev2EventProperties.  # noqa: E501


        :return: The events of this ArduinoDevicev2EventProperties.  # noqa: E501
        :rtype: ArduinoDevicev2SimplePropertiesCollection
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ArduinoDevicev2EventProperties.


        :param events: The events of this ArduinoDevicev2EventProperties.  # noqa: E501
        :type: ArduinoDevicev2SimplePropertiesCollection
        """
        if self.local_vars_configuration.client_side_validation and events is None:  # noqa: E501
            raise ValueError("Invalid value for `events`, must not be `None`")  # noqa: E501

        self._events = events

    @property
    def id(self):
        """Gets the id of this ArduinoDevicev2EventProperties.  # noqa: E501

        The device of the property  # noqa: E501

        :return: The id of this ArduinoDevicev2EventProperties.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArduinoDevicev2EventProperties.

        The device of the property  # noqa: E501

        :param id: The id of this ArduinoDevicev2EventProperties.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, ArduinoDevicev2EventProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoDevicev2EventProperties):
            return True

        return self.to_dict() != other.to_dict()

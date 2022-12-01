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


class ArduinoLinkedvariable(object):
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
        'id': 'str',
        'last_value': 'object',
        'last_value_updated_at': 'datetime',
        'name': 'str',
        'permission': 'str',
        'thing_id': 'str',
        'thing_name': 'str',
        'thing_timezone': 'ArduinoTimezone',
        'type': 'str',
        'variable_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'last_value': 'last_value',
        'last_value_updated_at': 'last_value_updated_at',
        'name': 'name',
        'permission': 'permission',
        'thing_id': 'thing_id',
        'thing_name': 'thing_name',
        'thing_timezone': 'thing_timezone',
        'type': 'type',
        'variable_name': 'variable_name'
    }

    def __init__(self, id=None, last_value=None, last_value_updated_at=None, name=None, permission=None, thing_id=None, thing_name=None, thing_timezone=None, type=None, variable_name=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoLinkedvariable - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._last_value = None
        self._last_value_updated_at = None
        self._name = None
        self._permission = None
        self._thing_id = None
        self._thing_name = None
        self._thing_timezone = None
        self._type = None
        self._variable_name = None
        self.discriminator = None

        self.id = id
        if last_value is not None:
            self.last_value = last_value
        if last_value_updated_at is not None:
            self.last_value_updated_at = last_value_updated_at
        self.name = name
        self.permission = permission
        self.thing_id = thing_id
        self.thing_name = thing_name
        if thing_timezone is not None:
            self.thing_timezone = thing_timezone
        self.type = type
        self.variable_name = variable_name

    @property
    def id(self):
        """Gets the id of this ArduinoLinkedvariable.  # noqa: E501

        The id of the linked variable  # noqa: E501

        :return: The id of this ArduinoLinkedvariable.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArduinoLinkedvariable.

        The id of the linked variable  # noqa: E501

        :param id: The id of this ArduinoLinkedvariable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_value(self):
        """Gets the last_value of this ArduinoLinkedvariable.  # noqa: E501

        Last value of the linked property  # noqa: E501

        :return: The last_value of this ArduinoLinkedvariable.  # noqa: E501
        :rtype: object
        """
        return self._last_value

    @last_value.setter
    def last_value(self, last_value):
        """Sets the last_value of this ArduinoLinkedvariable.

        Last value of the linked property  # noqa: E501

        :param last_value: The last_value of this ArduinoLinkedvariable.  # noqa: E501
        :type: object
        """

        self._last_value = last_value

    @property
    def last_value_updated_at(self):
        """Gets the last_value_updated_at of this ArduinoLinkedvariable.  # noqa: E501

        Update date of the last value  # noqa: E501

        :return: The last_value_updated_at of this ArduinoLinkedvariable.  # noqa: E501
        :rtype: datetime
        """
        return self._last_value_updated_at

    @last_value_updated_at.setter
    def last_value_updated_at(self, last_value_updated_at):
        """Sets the last_value_updated_at of this ArduinoLinkedvariable.

        Update date of the last value  # noqa: E501

        :param last_value_updated_at: The last_value_updated_at of this ArduinoLinkedvariable.  # noqa: E501
        :type: datetime
        """

        self._last_value_updated_at = last_value_updated_at

    @property
    def name(self):
        """Gets the name of this ArduinoLinkedvariable.  # noqa: E501

        The name of the variable  # noqa: E501

        :return: The name of this ArduinoLinkedvariable.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArduinoLinkedvariable.

        The name of the variable  # noqa: E501

        :param name: The name of this ArduinoLinkedvariable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def permission(self):
        """Gets the permission of this ArduinoLinkedvariable.  # noqa: E501

        The permission of the linked variable  # noqa: E501

        :return: The permission of this ArduinoLinkedvariable.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ArduinoLinkedvariable.

        The permission of the linked variable  # noqa: E501

        :param permission: The permission of this ArduinoLinkedvariable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and permission is None:  # noqa: E501
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501

        self._permission = permission

    @property
    def thing_id(self):
        """Gets the thing_id of this ArduinoLinkedvariable.  # noqa: E501

        The id of the related thing  # noqa: E501

        :return: The thing_id of this ArduinoLinkedvariable.  # noqa: E501
        :rtype: str
        """
        return self._thing_id

    @thing_id.setter
    def thing_id(self, thing_id):
        """Sets the thing_id of this ArduinoLinkedvariable.

        The id of the related thing  # noqa: E501

        :param thing_id: The thing_id of this ArduinoLinkedvariable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and thing_id is None:  # noqa: E501
            raise ValueError("Invalid value for `thing_id`, must not be `None`")  # noqa: E501

        self._thing_id = thing_id

    @property
    def thing_name(self):
        """Gets the thing_name of this ArduinoLinkedvariable.  # noqa: E501

        The name of the related thing  # noqa: E501

        :return: The thing_name of this ArduinoLinkedvariable.  # noqa: E501
        :rtype: str
        """
        return self._thing_name

    @thing_name.setter
    def thing_name(self, thing_name):
        """Sets the thing_name of this ArduinoLinkedvariable.

        The name of the related thing  # noqa: E501

        :param thing_name: The thing_name of this ArduinoLinkedvariable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and thing_name is None:  # noqa: E501
            raise ValueError("Invalid value for `thing_name`, must not be `None`")  # noqa: E501

        self._thing_name = thing_name

    @property
    def thing_timezone(self):
        """Gets the thing_timezone of this ArduinoLinkedvariable.  # noqa: E501


        :return: The thing_timezone of this ArduinoLinkedvariable.  # noqa: E501
        :rtype: ArduinoTimezone
        """
        return self._thing_timezone

    @thing_timezone.setter
    def thing_timezone(self, thing_timezone):
        """Sets the thing_timezone of this ArduinoLinkedvariable.


        :param thing_timezone: The thing_timezone of this ArduinoLinkedvariable.  # noqa: E501
        :type: ArduinoTimezone
        """

        self._thing_timezone = thing_timezone

    @property
    def type(self):
        """Gets the type of this ArduinoLinkedvariable.  # noqa: E501

        The type of the variable  # noqa: E501

        :return: The type of this ArduinoLinkedvariable.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ArduinoLinkedvariable.

        The type of the variable  # noqa: E501

        :param type: The type of this ArduinoLinkedvariable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def variable_name(self):
        """Gets the variable_name of this ArduinoLinkedvariable.  # noqa: E501

        The name of the variable in the code  # noqa: E501

        :return: The variable_name of this ArduinoLinkedvariable.  # noqa: E501
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this ArduinoLinkedvariable.

        The name of the variable in the code  # noqa: E501

        :param variable_name: The variable_name of this ArduinoLinkedvariable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and variable_name is None:  # noqa: E501
            raise ValueError("Invalid value for `variable_name`, must not be `None`")  # noqa: E501

        self._variable_name = variable_name

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
        if not isinstance(other, ArduinoLinkedvariable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoLinkedvariable):
            return True

        return self.to_dict() != other.to_dict()

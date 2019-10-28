# coding: utf-8

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from arduino_iot_rest.configuration import Configuration


class ArduinoDevicev2(object):
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
        'created_at': 'datetime',
        'href': 'str',
        'id': 'str',
        'metadata': 'dict(str, object)',
        'name': 'str',
        'serial': 'str',
        'type': 'str',
        'user_id': 'str',
        'webhooks': 'list[ArduinoDevicev2Webhook]'
    }

    attribute_map = {
        'created_at': 'created_at',
        'href': 'href',
        'id': 'id',
        'metadata': 'metadata',
        'name': 'name',
        'serial': 'serial',
        'type': 'type',
        'user_id': 'user_id',
        'webhooks': 'webhooks'
    }

    def __init__(self, created_at=None, href=None, id=None, metadata=None, name=None, serial=None, type=None, user_id=None, webhooks=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoDevicev2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._href = None
        self._id = None
        self._metadata = None
        self._name = None
        self._serial = None
        self._type = None
        self._user_id = None
        self._webhooks = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        self.href = href
        self.id = id
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        self.serial = serial
        self.type = type
        self.user_id = user_id
        if webhooks is not None:
            self.webhooks = webhooks

    @property
    def created_at(self):
        """Gets the created_at of this ArduinoDevicev2.  # noqa: E501

        Creation date of the device  # noqa: E501

        :return: The created_at of this ArduinoDevicev2.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ArduinoDevicev2.

        Creation date of the device  # noqa: E501

        :param created_at: The created_at of this ArduinoDevicev2.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def href(self):
        """Gets the href of this ArduinoDevicev2.  # noqa: E501

        The api reference of this device  # noqa: E501

        :return: The href of this ArduinoDevicev2.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ArduinoDevicev2.

        The api reference of this device  # noqa: E501

        :param href: The href of this ArduinoDevicev2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and href is None:  # noqa: E501
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def id(self):
        """Gets the id of this ArduinoDevicev2.  # noqa: E501

        The arn of the device  # noqa: E501

        :return: The id of this ArduinoDevicev2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArduinoDevicev2.

        The arn of the device  # noqa: E501

        :param id: The id of this ArduinoDevicev2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this ArduinoDevicev2.  # noqa: E501

        The metadata of the device  # noqa: E501

        :return: The metadata of this ArduinoDevicev2.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ArduinoDevicev2.

        The metadata of the device  # noqa: E501

        :param metadata: The metadata of this ArduinoDevicev2.  # noqa: E501
        :type: dict(str, object)
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this ArduinoDevicev2.  # noqa: E501

        The friendly name of the device  # noqa: E501

        :return: The name of this ArduinoDevicev2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArduinoDevicev2.

        The friendly name of the device  # noqa: E501

        :param name: The name of this ArduinoDevicev2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def serial(self):
        """Gets the serial of this ArduinoDevicev2.  # noqa: E501

        The serial uuid of the device  # noqa: E501

        :return: The serial of this ArduinoDevicev2.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this ArduinoDevicev2.

        The serial uuid of the device  # noqa: E501

        :param serial: The serial of this ArduinoDevicev2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and serial is None:  # noqa: E501
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501

        self._serial = serial

    @property
    def type(self):
        """Gets the type of this ArduinoDevicev2.  # noqa: E501

        The type of the device  # noqa: E501

        :return: The type of this ArduinoDevicev2.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ArduinoDevicev2.

        The type of the device  # noqa: E501

        :param type: The type of this ArduinoDevicev2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def user_id(self):
        """Gets the user_id of this ArduinoDevicev2.  # noqa: E501

        The id of the user  # noqa: E501

        :return: The user_id of this ArduinoDevicev2.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ArduinoDevicev2.

        The id of the user  # noqa: E501

        :param user_id: The user_id of this ArduinoDevicev2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def webhooks(self):
        """Gets the webhooks of this ArduinoDevicev2.  # noqa: E501

        ArduinoDevicev2WebhookCollection is the media type for an array of ArduinoDevicev2Webhook (default view)  # noqa: E501

        :return: The webhooks of this ArduinoDevicev2.  # noqa: E501
        :rtype: list[ArduinoDevicev2Webhook]
        """
        return self._webhooks

    @webhooks.setter
    def webhooks(self, webhooks):
        """Sets the webhooks of this ArduinoDevicev2.

        ArduinoDevicev2WebhookCollection is the media type for an array of ArduinoDevicev2Webhook (default view)  # noqa: E501

        :param webhooks: The webhooks of this ArduinoDevicev2.  # noqa: E501
        :type: list[ArduinoDevicev2Webhook]
        """

        self._webhooks = webhooks

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
        if not isinstance(other, ArduinoDevicev2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoDevicev2):
            return True

        return self.to_dict() != other.to_dict()

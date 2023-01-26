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


class Devicev2(object):
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
        'connection_type': 'str',
        'fqbn': 'str',
        'name': 'str',
        'serial': 'str',
        'type': 'str',
        'user_id': 'str',
        'wifi_fw_version': 'str'
    }

    attribute_map = {
        'connection_type': 'connection_type',
        'fqbn': 'fqbn',
        'name': 'name',
        'serial': 'serial',
        'type': 'type',
        'user_id': 'user_id',
        'wifi_fw_version': 'wifi_fw_version'
    }

    def __init__(self, connection_type=None, fqbn=None, name=None, serial=None, type=None, user_id=None, wifi_fw_version=None, local_vars_configuration=None):  # noqa: E501
        """Devicev2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._connection_type = None
        self._fqbn = None
        self._name = None
        self._serial = None
        self._type = None
        self._user_id = None
        self._wifi_fw_version = None
        self.discriminator = None

        if connection_type is not None:
            self.connection_type = connection_type
        if fqbn is not None:
            self.fqbn = fqbn
        if name is not None:
            self.name = name
        if serial is not None:
            self.serial = serial
        if type is not None:
            self.type = type
        if user_id is not None:
            self.user_id = user_id
        if wifi_fw_version is not None:
            self.wifi_fw_version = wifi_fw_version

    @property
    def connection_type(self):
        """Gets the connection_type of this Devicev2.  # noqa: E501

        The type of the connections selected by the user when multiple connections are available  # noqa: E501

        :return: The connection_type of this Devicev2.  # noqa: E501
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this Devicev2.

        The type of the connections selected by the user when multiple connections are available  # noqa: E501

        :param connection_type: The connection_type of this Devicev2.  # noqa: E501
        :type: str
        """
        allowed_values = ["wifi", "eth", "wifiandsecret", "gsm", "nb", "lora"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and connection_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `connection_type` ({0}), must be one of {1}"  # noqa: E501
                .format(connection_type, allowed_values)
            )

        self._connection_type = connection_type

    @property
    def fqbn(self):
        """Gets the fqbn of this Devicev2.  # noqa: E501

        The fully qualified board name  # noqa: E501

        :return: The fqbn of this Devicev2.  # noqa: E501
        :rtype: str
        """
        return self._fqbn

    @fqbn.setter
    def fqbn(self, fqbn):
        """Sets the fqbn of this Devicev2.

        The fully qualified board name  # noqa: E501

        :param fqbn: The fqbn of this Devicev2.  # noqa: E501
        :type: str
        """

        self._fqbn = fqbn

    @property
    def name(self):
        """Gets the name of this Devicev2.  # noqa: E501

        The friendly name of the device  # noqa: E501

        :return: The name of this Devicev2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Devicev2.

        The friendly name of the device  # noqa: E501

        :param name: The name of this Devicev2.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'[a-zA-Z0-9_.@-]+', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/[a-zA-Z0-9_.@-]+/`")  # noqa: E501

        self._name = name

    @property
    def serial(self):
        """Gets the serial of this Devicev2.  # noqa: E501

        The serial uuid of the device  # noqa: E501

        :return: The serial of this Devicev2.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this Devicev2.

        The serial uuid of the device  # noqa: E501

        :param serial: The serial of this Devicev2.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) > 64):
            raise ValueError("Invalid value for `serial`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and not re.search(r'[a-zA-Z0-9_.@-]+', serial)):  # noqa: E501
            raise ValueError(r"Invalid value for `serial`, must be a follow pattern or equal to `/[a-zA-Z0-9_.@-]+/`")  # noqa: E501

        self._serial = serial

    @property
    def type(self):
        """Gets the type of this Devicev2.  # noqa: E501

        The type of the device  # noqa: E501

        :return: The type of this Devicev2.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Devicev2.

        The type of the device  # noqa: E501

        :param type: The type of this Devicev2.  # noqa: E501
        :type: str
        """
        allowed_values = ["mkrwifi1010", "mkr1000", "nano_33_iot", "mkrgsm1400", "mkrwan1310", "mkrwan1300", "mkrnb1500", "lora-device", "login_and_secretkey_wifi", "envie_m7", "nanorp2040connect", "nicla_vision", "phone", "portenta_x8", "opta"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def user_id(self):
        """Gets the user_id of this Devicev2.  # noqa: E501

        The user_id associated to the device. If absent it will be inferred from the authentication header  # noqa: E501

        :return: The user_id of this Devicev2.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Devicev2.

        The user_id associated to the device. If absent it will be inferred from the authentication header  # noqa: E501

        :param user_id: The user_id of this Devicev2.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def wifi_fw_version(self):
        """Gets the wifi_fw_version of this Devicev2.  # noqa: E501

        The version of the NINA/WIFI101 firmware running on the device  # noqa: E501

        :return: The wifi_fw_version of this Devicev2.  # noqa: E501
        :rtype: str
        """
        return self._wifi_fw_version

    @wifi_fw_version.setter
    def wifi_fw_version(self, wifi_fw_version):
        """Sets the wifi_fw_version of this Devicev2.

        The version of the NINA/WIFI101 firmware running on the device  # noqa: E501

        :param wifi_fw_version: The wifi_fw_version of this Devicev2.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                wifi_fw_version is not None and len(wifi_fw_version) > 10):
            raise ValueError("Invalid value for `wifi_fw_version`, length must be less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                wifi_fw_version is not None and not re.search(r'^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$', wifi_fw_version)):  # noqa: E501
            raise ValueError(r"Invalid value for `wifi_fw_version`, must be a follow pattern or equal to `/^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$/`")  # noqa: E501

        self._wifi_fw_version = wifi_fw_version

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
        if not isinstance(other, Devicev2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Devicev2):
            return True

        return self.to_dict() != other.to_dict()

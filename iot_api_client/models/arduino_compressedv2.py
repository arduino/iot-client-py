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


class ArduinoCompressedv2(object):
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
        'authority_key_identifier': 'str',
        'not_after': 'datetime',
        'not_before': 'datetime',
        'serial': 'str',
        'signature': 'str',
        'signature_asn1_x': 'str',
        'signature_asn1_y': 'str'
    }

    attribute_map = {
        'authority_key_identifier': 'authority_key_identifier',
        'not_after': 'not_after',
        'not_before': 'not_before',
        'serial': 'serial',
        'signature': 'signature',
        'signature_asn1_x': 'signature_asn1_x',
        'signature_asn1_y': 'signature_asn1_y'
    }

    def __init__(self, authority_key_identifier=None, not_after=None, not_before=None, serial=None, signature=None, signature_asn1_x=None, signature_asn1_y=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoCompressedv2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authority_key_identifier = None
        self._not_after = None
        self._not_before = None
        self._serial = None
        self._signature = None
        self._signature_asn1_x = None
        self._signature_asn1_y = None
        self.discriminator = None

        if authority_key_identifier is not None:
            self.authority_key_identifier = authority_key_identifier
        self.not_after = not_after
        self.not_before = not_before
        self.serial = serial
        self.signature = signature
        self.signature_asn1_x = signature_asn1_x
        self.signature_asn1_y = signature_asn1_y

    @property
    def authority_key_identifier(self):
        """Gets the authority_key_identifier of this ArduinoCompressedv2.  # noqa: E501

        The Authority Key Identifier of the certificate  # noqa: E501

        :return: The authority_key_identifier of this ArduinoCompressedv2.  # noqa: E501
        :rtype: str
        """
        return self._authority_key_identifier

    @authority_key_identifier.setter
    def authority_key_identifier(self, authority_key_identifier):
        """Sets the authority_key_identifier of this ArduinoCompressedv2.

        The Authority Key Identifier of the certificate  # noqa: E501

        :param authority_key_identifier: The authority_key_identifier of this ArduinoCompressedv2.  # noqa: E501
        :type: str
        """

        self._authority_key_identifier = authority_key_identifier

    @property
    def not_after(self):
        """Gets the not_after of this ArduinoCompressedv2.  # noqa: E501

        The ending date of the certificate  # noqa: E501

        :return: The not_after of this ArduinoCompressedv2.  # noqa: E501
        :rtype: datetime
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this ArduinoCompressedv2.

        The ending date of the certificate  # noqa: E501

        :param not_after: The not_after of this ArduinoCompressedv2.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and not_after is None:  # noqa: E501
            raise ValueError("Invalid value for `not_after`, must not be `None`")  # noqa: E501

        self._not_after = not_after

    @property
    def not_before(self):
        """Gets the not_before of this ArduinoCompressedv2.  # noqa: E501

        The starting date of the certificate  # noqa: E501

        :return: The not_before of this ArduinoCompressedv2.  # noqa: E501
        :rtype: datetime
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this ArduinoCompressedv2.

        The starting date of the certificate  # noqa: E501

        :param not_before: The not_before of this ArduinoCompressedv2.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and not_before is None:  # noqa: E501
            raise ValueError("Invalid value for `not_before`, must not be `None`")  # noqa: E501

        self._not_before = not_before

    @property
    def serial(self):
        """Gets the serial of this ArduinoCompressedv2.  # noqa: E501

        The serial number of the certificate  # noqa: E501

        :return: The serial of this ArduinoCompressedv2.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this ArduinoCompressedv2.

        The serial number of the certificate  # noqa: E501

        :param serial: The serial of this ArduinoCompressedv2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and serial is None:  # noqa: E501
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501

        self._serial = serial

    @property
    def signature(self):
        """Gets the signature of this ArduinoCompressedv2.  # noqa: E501

        The signature of the certificate  # noqa: E501

        :return: The signature of this ArduinoCompressedv2.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this ArduinoCompressedv2.

        The signature of the certificate  # noqa: E501

        :param signature: The signature of this ArduinoCompressedv2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signature is None:  # noqa: E501
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def signature_asn1_x(self):
        """Gets the signature_asn1_x of this ArduinoCompressedv2.  # noqa: E501

        The ASN1 X component of certificate signature  # noqa: E501

        :return: The signature_asn1_x of this ArduinoCompressedv2.  # noqa: E501
        :rtype: str
        """
        return self._signature_asn1_x

    @signature_asn1_x.setter
    def signature_asn1_x(self, signature_asn1_x):
        """Sets the signature_asn1_x of this ArduinoCompressedv2.

        The ASN1 X component of certificate signature  # noqa: E501

        :param signature_asn1_x: The signature_asn1_x of this ArduinoCompressedv2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signature_asn1_x is None:  # noqa: E501
            raise ValueError("Invalid value for `signature_asn1_x`, must not be `None`")  # noqa: E501

        self._signature_asn1_x = signature_asn1_x

    @property
    def signature_asn1_y(self):
        """Gets the signature_asn1_y of this ArduinoCompressedv2.  # noqa: E501

        The ASN1 Y component of certificate signature  # noqa: E501

        :return: The signature_asn1_y of this ArduinoCompressedv2.  # noqa: E501
        :rtype: str
        """
        return self._signature_asn1_y

    @signature_asn1_y.setter
    def signature_asn1_y(self, signature_asn1_y):
        """Sets the signature_asn1_y of this ArduinoCompressedv2.

        The ASN1 Y component of certificate signature  # noqa: E501

        :param signature_asn1_y: The signature_asn1_y of this ArduinoCompressedv2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signature_asn1_y is None:  # noqa: E501
            raise ValueError("Invalid value for `signature_asn1_y`, must not be `None`")  # noqa: E501

        self._signature_asn1_y = signature_asn1_y

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
        if not isinstance(other, ArduinoCompressedv2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoCompressedv2):
            return True

        return self.to_dict() != other.to_dict()

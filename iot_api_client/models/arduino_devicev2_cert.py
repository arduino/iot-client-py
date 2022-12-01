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


class ArduinoDevicev2Cert(object):
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
        'ca': 'str',
        'compressed': 'ArduinoCompressedv2',
        'der': 'str',
        'device_id': 'str',
        'enabled': 'bool',
        'href': 'str',
        'id': 'str',
        'pem': 'str'
    }

    attribute_map = {
        'ca': 'ca',
        'compressed': 'compressed',
        'der': 'der',
        'device_id': 'device_id',
        'enabled': 'enabled',
        'href': 'href',
        'id': 'id',
        'pem': 'pem'
    }

    def __init__(self, ca=None, compressed=None, der=None, device_id=None, enabled=True, href=None, id=None, pem=None, local_vars_configuration=None):  # noqa: E501
        """ArduinoDevicev2Cert - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ca = None
        self._compressed = None
        self._der = None
        self._device_id = None
        self._enabled = None
        self._href = None
        self._id = None
        self._pem = None
        self.discriminator = None

        if ca is not None:
            self.ca = ca
        self.compressed = compressed
        self.der = der
        self.device_id = device_id
        self.enabled = enabled
        self.href = href
        self.id = id
        self.pem = pem

    @property
    def ca(self):
        """Gets the ca of this ArduinoDevicev2Cert.  # noqa: E501

        The Certification Authority used to sign the certificate  # noqa: E501

        :return: The ca of this ArduinoDevicev2Cert.  # noqa: E501
        :rtype: str
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this ArduinoDevicev2Cert.

        The Certification Authority used to sign the certificate  # noqa: E501

        :param ca: The ca of this ArduinoDevicev2Cert.  # noqa: E501
        :type: str
        """

        self._ca = ca

    @property
    def compressed(self):
        """Gets the compressed of this ArduinoDevicev2Cert.  # noqa: E501


        :return: The compressed of this ArduinoDevicev2Cert.  # noqa: E501
        :rtype: ArduinoCompressedv2
        """
        return self._compressed

    @compressed.setter
    def compressed(self, compressed):
        """Sets the compressed of this ArduinoDevicev2Cert.


        :param compressed: The compressed of this ArduinoDevicev2Cert.  # noqa: E501
        :type: ArduinoCompressedv2
        """
        if self.local_vars_configuration.client_side_validation and compressed is None:  # noqa: E501
            raise ValueError("Invalid value for `compressed`, must not be `None`")  # noqa: E501

        self._compressed = compressed

    @property
    def der(self):
        """Gets the der of this ArduinoDevicev2Cert.  # noqa: E501

        The certificate in DER format  # noqa: E501

        :return: The der of this ArduinoDevicev2Cert.  # noqa: E501
        :rtype: str
        """
        return self._der

    @der.setter
    def der(self, der):
        """Sets the der of this ArduinoDevicev2Cert.

        The certificate in DER format  # noqa: E501

        :param der: The der of this ArduinoDevicev2Cert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and der is None:  # noqa: E501
            raise ValueError("Invalid value for `der`, must not be `None`")  # noqa: E501

        self._der = der

    @property
    def device_id(self):
        """Gets the device_id of this ArduinoDevicev2Cert.  # noqa: E501

        The unique identifier of the device  # noqa: E501

        :return: The device_id of this ArduinoDevicev2Cert.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ArduinoDevicev2Cert.

        The unique identifier of the device  # noqa: E501

        :param device_id: The device_id of this ArduinoDevicev2Cert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def enabled(self):
        """Gets the enabled of this ArduinoDevicev2Cert.  # noqa: E501

        Whether the certificate is enabled  # noqa: E501

        :return: The enabled of this ArduinoDevicev2Cert.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ArduinoDevicev2Cert.

        Whether the certificate is enabled  # noqa: E501

        :param enabled: The enabled of this ArduinoDevicev2Cert.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def href(self):
        """Gets the href of this ArduinoDevicev2Cert.  # noqa: E501

        The api reference of this cert  # noqa: E501

        :return: The href of this ArduinoDevicev2Cert.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ArduinoDevicev2Cert.

        The api reference of this cert  # noqa: E501

        :param href: The href of this ArduinoDevicev2Cert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and href is None:  # noqa: E501
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def id(self):
        """Gets the id of this ArduinoDevicev2Cert.  # noqa: E501

        The unique identifier of the key  # noqa: E501

        :return: The id of this ArduinoDevicev2Cert.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ArduinoDevicev2Cert.

        The unique identifier of the key  # noqa: E501

        :param id: The id of this ArduinoDevicev2Cert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def pem(self):
        """Gets the pem of this ArduinoDevicev2Cert.  # noqa: E501

        The certificate in pem format  # noqa: E501

        :return: The pem of this ArduinoDevicev2Cert.  # noqa: E501
        :rtype: str
        """
        return self._pem

    @pem.setter
    def pem(self, pem):
        """Sets the pem of this ArduinoDevicev2Cert.

        The certificate in pem format  # noqa: E501

        :param pem: The pem of this ArduinoDevicev2Cert.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pem is None:  # noqa: E501
            raise ValueError("Invalid value for `pem`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pem is not None and len(pem) > 512):
            raise ValueError("Invalid value for `pem`, length must be less than or equal to `512`")  # noqa: E501

        self._pem = pem

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
        if not isinstance(other, ArduinoDevicev2Cert):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArduinoDevicev2Cert):
            return True

        return self.to_dict() != other.to_dict()

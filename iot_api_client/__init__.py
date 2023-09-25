# coding: utf-8

# flake8: noqa

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

__version__ = "2.0.0"

# import ApiClient
from iot_api_client.api_client import ApiClient

# import Configuration
from iot_api_client.configuration import Configuration

# import exceptions
from iot_api_client.exceptions import OpenApiException
from iot_api_client.exceptions import ApiAttributeError
from iot_api_client.exceptions import ApiTypeError
from iot_api_client.exceptions import ApiValueError
from iot_api_client.exceptions import ApiKeyError
from iot_api_client.exceptions import ApiException

# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

from iot_api_client.paths.v1_network_credentials_type.get import NetworkCredentialsV1Show
from iot_api_client.paths.v1_network_credentials_type_connections.get import NetworkCredentialsV1ShowByDevice


class NetworkCredentialsV1Api(
    NetworkCredentialsV1Show,
    NetworkCredentialsV1ShowByDevice,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

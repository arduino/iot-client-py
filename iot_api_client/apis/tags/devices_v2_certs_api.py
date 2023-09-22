# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

from iot_api_client.paths.v2_devices_id_certs.put import DevicesV2CertsCreate
from iot_api_client.paths.v2_devices_id_certs_cid.delete import DevicesV2CertsDelete
from iot_api_client.paths.v2_devices_id_certs.get import DevicesV2CertsList
from iot_api_client.paths.v2_devices_id_certs_cid.get import DevicesV2CertsShow
from iot_api_client.paths.v2_devices_id_certs_cid.post import DevicesV2CertsUpdate


class DevicesV2CertsApi(
    DevicesV2CertsCreate,
    DevicesV2CertsDelete,
    DevicesV2CertsList,
    DevicesV2CertsShow,
    DevicesV2CertsUpdate,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from iot_api_client import schemas  # noqa: F401


class ArduinoTemplatevariableCollection(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ArduinoTemplatevariableCollection is the media type for an array of ArduinoTemplatevariable (default view)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ArduinoTemplatevariable']:
            return ArduinoTemplatevariable

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['ArduinoTemplatevariable'], typing.List['ArduinoTemplatevariable']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ArduinoTemplatevariableCollection':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ArduinoTemplatevariable':
        return super().__getitem__(i)

from iot_api_client.model.arduino_templatevariable import ArduinoTemplatevariable
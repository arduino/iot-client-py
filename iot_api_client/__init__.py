# coding: utf-8

# flake8: noqa

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.0.1"

# import apis into sdk package
from iot_api_client.api.devices_v2_api import DevicesV2Api
from iot_api_client.api.properties_v2_api import PropertiesV2Api
from iot_api_client.api.series_v2_api import SeriesV2Api
from iot_api_client.api.things_v2_api import ThingsV2Api

# import ApiClient
from iot_api_client.api_client import ApiClient
from iot_api_client.configuration import Configuration
from iot_api_client.exceptions import OpenApiException
from iot_api_client.exceptions import ApiTypeError
from iot_api_client.exceptions import ApiValueError
from iot_api_client.exceptions import ApiKeyError
from iot_api_client.exceptions import ApiException
# import models into sdk package
from iot_api_client.models.arduino_devicev2 import ArduinoDevicev2
from iot_api_client.models.arduino_devicev2_webhook import ArduinoDevicev2Webhook
from iot_api_client.models.arduino_devicev2properties import ArduinoDevicev2properties
from iot_api_client.models.arduino_devicev2propertyvalue import ArduinoDevicev2propertyvalue
from iot_api_client.models.arduino_devicev2propertyvalue_value import ArduinoDevicev2propertyvalueValue
from iot_api_client.models.arduino_devicev2propertyvalue_value_statistics import ArduinoDevicev2propertyvalueValueStatistics
from iot_api_client.models.arduino_devicev2propertyvalues import ArduinoDevicev2propertyvalues
from iot_api_client.models.arduino_devicev2propertyvalues_last_evaluated_key import ArduinoDevicev2propertyvaluesLastEvaluatedKey
from iot_api_client.models.arduino_property import ArduinoProperty
from iot_api_client.models.arduino_series_batch import ArduinoSeriesBatch
from iot_api_client.models.arduino_series_raw_batch import ArduinoSeriesRawBatch
from iot_api_client.models.arduino_series_raw_batch_lastvalue import ArduinoSeriesRawBatchLastvalue
from iot_api_client.models.arduino_series_raw_last_value_response import ArduinoSeriesRawLastValueResponse
from iot_api_client.models.arduino_series_raw_response import ArduinoSeriesRawResponse
from iot_api_client.models.arduino_series_response import ArduinoSeriesResponse
from iot_api_client.models.arduino_thing import ArduinoThing
from iot_api_client.models.batch_last_value_requests_media_v1 import BatchLastValueRequestsMediaV1
from iot_api_client.models.batch_query_raw_last_value_request_media_v1 import BatchQueryRawLastValueRequestMediaV1
from iot_api_client.models.batch_query_raw_request_media_v1 import BatchQueryRawRequestMediaV1
from iot_api_client.models.batch_query_raw_requests_media_v1 import BatchQueryRawRequestsMediaV1
from iot_api_client.models.batch_query_raw_response_series_media_v1 import BatchQueryRawResponseSeriesMediaV1
from iot_api_client.models.batch_query_request_media_v1 import BatchQueryRequestMediaV1
from iot_api_client.models.batch_query_requests_media_v1 import BatchQueryRequestsMediaV1
from iot_api_client.models.create_devices_v2_payload import CreateDevicesV2Payload
from iot_api_client.models.create_things_v2_payload import CreateThingsV2Payload
from iot_api_client.models.devicev2 import Devicev2
from iot_api_client.models.error import Error
from iot_api_client.models.model_property import ModelProperty
from iot_api_client.models.properties_value import PropertiesValue
from iot_api_client.models.properties_values import PropertiesValues
from iot_api_client.models.property_value import PropertyValue
from iot_api_client.models.thing import Thing
from iot_api_client.models.thing_sketch import ThingSketch


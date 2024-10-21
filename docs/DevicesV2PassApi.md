# iot_api_client.DevicesV2PassApi

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_pass_check**](DevicesV2PassApi.md#devices_v2_pass_check) | **POST** /v2/devices/{id}/pass | check devices_v2_pass
[**devices_v2_pass_delete**](DevicesV2PassApi.md#devices_v2_pass_delete) | **DELETE** /v2/devices/{id}/pass | delete devices_v2_pass
[**devices_v2_pass_get**](DevicesV2PassApi.md#devices_v2_pass_get) | **GET** /v2/devices/{id}/pass | get devices_v2_pass
[**devices_v2_pass_set**](DevicesV2PassApi.md#devices_v2_pass_set) | **PUT** /v2/devices/{id}/pass | set devices_v2_pass


# **devices_v2_pass_check**
> devices_v2_pass_check(id, check_devices_v2_pass_payload)

check devices_v2_pass

Check if the password matches.

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import iot_api_client
from iot_api_client.models.check_devices_v2_pass_payload import CheckDevicesV2PassPayload
from iot_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2PassApi(api_client)
    id = 'id_example' # str | The id of the device
    check_devices_v2_pass_payload = iot_api_client.CheckDevicesV2PassPayload() # CheckDevicesV2PassPayload | 

    try:
        # check devices_v2_pass
        api_instance.devices_v2_pass_check(id, check_devices_v2_pass_payload)
    except Exception as e:
        print("Exception when calling DevicesV2PassApi->devices_v2_pass_check: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **check_devices_v2_pass_payload** | [**CheckDevicesV2PassPayload**](CheckDevicesV2PassPayload.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.goa.error+json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_pass_delete**
> devices_v2_pass_delete(id)

delete devices_v2_pass

Removes the password for the device.

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2PassApi(api_client)
    id = 'id_example' # str | The id of the device

    try:
        # delete devices_v2_pass
        api_instance.devices_v2_pass_delete(id)
    except Exception as e:
        print("Exception when calling DevicesV2PassApi->devices_v2_pass_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.goa.error+json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_pass_get**
> ArduinoDevicev2Pass devices_v2_pass_get(id, suggested_password=suggested_password)

get devices_v2_pass

Returns whether the password for this device is set or not. It doesn't return the password.

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import iot_api_client
from iot_api_client.models.arduino_devicev2_pass import ArduinoDevicev2Pass
from iot_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2PassApi(api_client)
    id = 'id_example' # str | The id of the device
    suggested_password = False # bool | If true, return a suggested password (optional) (default to False)

    try:
        # get devices_v2_pass
        api_response = api_instance.devices_v2_pass_get(id, suggested_password=suggested_password)
        print("The response of DevicesV2PassApi->devices_v2_pass_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2PassApi->devices_v2_pass_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **suggested_password** | **bool**| If true, return a suggested password | [optional] [default to False]

### Return type

[**ArduinoDevicev2Pass**](ArduinoDevicev2Pass.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2.pass+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_pass_set**
> ArduinoDevicev2Pass devices_v2_pass_set(id, devicev2_pass)

set devices_v2_pass

Sets the password for the device. It can never be read back.

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import iot_api_client
from iot_api_client.models.arduino_devicev2_pass import ArduinoDevicev2Pass
from iot_api_client.models.devicev2_pass import Devicev2Pass
from iot_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2PassApi(api_client)
    id = 'id_example' # str | The id of the device
    devicev2_pass = iot_api_client.Devicev2Pass() # Devicev2Pass | 

    try:
        # set devices_v2_pass
        api_response = api_instance.devices_v2_pass_set(id, devicev2_pass)
        print("The response of DevicesV2PassApi->devices_v2_pass_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2PassApi->devices_v2_pass_set: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **devicev2_pass** | [**Devicev2Pass**](Devicev2Pass.md)|  | 

### Return type

[**ArduinoDevicev2Pass**](ArduinoDevicev2Pass.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.arduino.devicev2.pass+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


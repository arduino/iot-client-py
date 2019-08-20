# iot_api_client.DevicesV2PassApi

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_pass_check**](DevicesV2PassApi.md#devices_v2_pass_check) | **POST** /iot/v2/devices/{id}/pass | check devices_v2_pass
[**devices_v2_pass_delete**](DevicesV2PassApi.md#devices_v2_pass_delete) | **DELETE** /iot/v2/devices/{id}/pass | delete devices_v2_pass
[**devices_v2_pass_get**](DevicesV2PassApi.md#devices_v2_pass_get) | **GET** /iot/v2/devices/{id}/pass | get devices_v2_pass
[**devices_v2_pass_set**](DevicesV2PassApi.md#devices_v2_pass_set) | **PUT** /iot/v2/devices/{id}/pass | set devices_v2_pass


# **devices_v2_pass_check**
> devices_v2_pass_check(id, check_devices_v2_pass_payload)

check devices_v2_pass

Check if the password matches.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2PassApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
check_devices_v2_pass_payload = iot_api_client.CheckDevicesV2PassPayload() # CheckDevicesV2PassPayload | 

try:
    # check devices_v2_pass
    api_instance.devices_v2_pass_check(id, check_devices_v2_pass_payload)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_pass_delete**
> devices_v2_pass_delete(id)

delete devices_v2_pass

Removes the password for the device.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2PassApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device

try:
    # delete devices_v2_pass
    api_instance.devices_v2_pass_delete(id)
except ApiException as e:
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_pass_get**
> ArduinoDevicev2Pass devices_v2_pass_get(id)

get devices_v2_pass

Returns whether the password for this device is set or not. It doesn't return the password.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2PassApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device

try:
    # get devices_v2_pass
    api_response = api_instance.devices_v2_pass_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2PassApi->devices_v2_pass_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 

### Return type

[**ArduinoDevicev2Pass**](ArduinoDevicev2Pass.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2.pass+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_pass_set**
> devices_v2_pass_set(id, set_devices_v2_pass_payload)

set devices_v2_pass

Sets the password for the device. It can never be read back.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2PassApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
set_devices_v2_pass_payload = iot_api_client.SetDevicesV2PassPayload() # SetDevicesV2PassPayload | 

try:
    # set devices_v2_pass
    api_instance.devices_v2_pass_set(id, set_devices_v2_pass_payload)
except ApiException as e:
    print("Exception when calling DevicesV2PassApi->devices_v2_pass_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **set_devices_v2_pass_payload** | [**SetDevicesV2PassPayload**](SetDevicesV2PassPayload.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.goa.error+json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


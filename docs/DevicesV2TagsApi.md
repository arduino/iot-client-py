# iot_api_client.DevicesV2TagsApi

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_tags_delete**](DevicesV2TagsApi.md#devices_v2_tags_delete) | **DELETE** /v2/devices/{id}/tags/{key} | delete devices_v2_tags
[**devices_v2_tags_list**](DevicesV2TagsApi.md#devices_v2_tags_list) | **GET** /v2/devices/{id}/tags | list devices_v2_tags
[**devices_v2_tags_upsert**](DevicesV2TagsApi.md#devices_v2_tags_upsert) | **PUT** /v2/devices/{id}/tags | upsert devices_v2_tags


# **devices_v2_tags_delete**
> devices_v2_tags_delete(id, key)

delete devices_v2_tags

Delete a tag associated to the device given its key.

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
    api_instance = iot_api_client.DevicesV2TagsApi(api_client)
    id = 'id_example' # str | The id of the device
    key = 'key_example' # str | The key of the tag

    try:
        # delete devices_v2_tags
        api_instance.devices_v2_tags_delete(id, key)
    except Exception as e:
        print("Exception when calling DevicesV2TagsApi->devices_v2_tags_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **key** | **str**| The key of the tag | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_tags_list**
> ArduinoTags devices_v2_tags_list(id)

list devices_v2_tags

List tags associated to the device.

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import iot_api_client
from iot_api_client.models.arduino_tags import ArduinoTags
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
    api_instance = iot_api_client.DevicesV2TagsApi(api_client)
    id = 'id_example' # str | The id of the device

    try:
        # list devices_v2_tags
        api_response = api_instance.devices_v2_tags_list(id)
        print("The response of DevicesV2TagsApi->devices_v2_tags_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2TagsApi->devices_v2_tags_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 

### Return type

[**ArduinoTags**](ArduinoTags.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.tags+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_tags_upsert**
> devices_v2_tags_upsert(id, tag)

upsert devices_v2_tags

Creates or updates a tag associated to the device.

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import iot_api_client
from iot_api_client.models.tag import Tag
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
    api_instance = iot_api_client.DevicesV2TagsApi(api_client)
    id = 'id_example' # str | The id of the device
    tag = iot_api_client.Tag() # Tag | 

    try:
        # upsert devices_v2_tags
        api_instance.devices_v2_tags_upsert(id, tag)
    except Exception as e:
        print("Exception when calling DevicesV2TagsApi->devices_v2_tags_upsert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **tag** | [**Tag**](Tag.md)|  | 

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


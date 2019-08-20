# iot_api_client.DevicesV2MetadataApi

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_metadata_delete**](DevicesV2MetadataApi.md#devices_v2_metadata_delete) | **DELETE** /iot/v2/devices/{id}/metadata/{key} | delete devices_v2_metadata
[**devices_v2_metadata_list**](DevicesV2MetadataApi.md#devices_v2_metadata_list) | **GET** /iot/v2/devices/{id}/metadata | list devices_v2_metadata
[**devices_v2_metadata_set**](DevicesV2MetadataApi.md#devices_v2_metadata_set) | **PUT** /iot/v2/devices/{id}/metadata | set devices_v2_metadata


# **devices_v2_metadata_delete**
> devices_v2_metadata_delete(id, key)

delete devices_v2_metadata

Removes the a metadata key of the device.

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
api_instance = iot_api_client.DevicesV2MetadataApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
key = 'key_example' # str | 

try:
    # delete devices_v2_metadata
    api_instance.devices_v2_metadata_delete(id, key)
except ApiException as e:
    print("Exception when calling DevicesV2MetadataApi->devices_v2_metadata_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **key** | **str**|  | 

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

# **devices_v2_metadata_list**
> devices_v2_metadata_list(id)

list devices_v2_metadata

Returns metadata of a device

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
api_instance = iot_api_client.DevicesV2MetadataApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device

try:
    # list devices_v2_metadata
    api_instance.devices_v2_metadata_list(id)
except ApiException as e:
    print("Exception when calling DevicesV2MetadataApi->devices_v2_metadata_list: %s\n" % e)
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

# **devices_v2_metadata_set**
> devices_v2_metadata_set(id, request_body)

set devices_v2_metadata

Sets metadata of a device

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
api_instance = iot_api_client.DevicesV2MetadataApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
request_body = None # dict(str, object) | 

try:
    # set devices_v2_metadata
    api_instance.devices_v2_metadata_set(id, request_body)
except ApiException as e:
    print("Exception when calling DevicesV2MetadataApi->devices_v2_metadata_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **request_body** | [**dict(str, object)**](object.md)|  | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


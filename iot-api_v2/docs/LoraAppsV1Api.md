# iot_api_client.LoraAppsV1Api

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lora_apps_v1_list**](LoraAppsV1Api.md#lora_apps_v1_list) | **GET** /iot/v1/lora-apps/ | list lora_apps_v1
[**lora_apps_v1_update**](LoraAppsV1Api.md#lora_apps_v1_update) | **POST** /iot/v1/lora-apps/ | update lora_apps_v1


# **lora_apps_v1_list**
> lora_apps_v1_list(user_id)

list lora_apps_v1

List the available apps for the given user

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
api_instance = iot_api_client.LoraAppsV1Api(iot_api_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id. Could be a uuid, or the string 'me'

try:
    # list lora_apps_v1
    api_instance.lora_apps_v1_list(user_id)
except ApiException as e:
    print("Exception when calling LoraAppsV1Api->lora_apps_v1_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id. Could be a uuid, or the string &#39;me&#39; | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lora_apps_v1_update**
> lora_apps_v1_update(user_id, update_lora_apps_v1_payload)

update lora_apps_v1

Update the available apps for the given user

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
api_instance = iot_api_client.LoraAppsV1Api(iot_api_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id. Could be a uuid, or the string 'me'
update_lora_apps_v1_payload = iot_api_client.UpdateLoraAppsV1Payload() # UpdateLoraAppsV1Payload | 

try:
    # update lora_apps_v1
    api_instance.lora_apps_v1_update(user_id, update_lora_apps_v1_payload)
except ApiException as e:
    print("Exception when calling LoraAppsV1Api->lora_apps_v1_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id. Could be a uuid, or the string &#39;me&#39; | 
 **update_lora_apps_v1_payload** | [**UpdateLoraAppsV1Payload**](UpdateLoraAppsV1Payload.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# iot_api_client.DevicesV2WebhooksApi

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_webhooks_create**](DevicesV2WebhooksApi.md#devices_v2_webhooks_create) | **PUT** /iot/v2/devices/{id}/webhooks | create devices_v2_webhooks
[**devices_v2_webhooks_delete**](DevicesV2WebhooksApi.md#devices_v2_webhooks_delete) | **DELETE** /iot/v2/devices/{id}/webhooks/{wid} | delete devices_v2_webhooks
[**devices_v2_webhooks_test**](DevicesV2WebhooksApi.md#devices_v2_webhooks_test) | **POST** /iot/v2/devices/{id}/webhooks/test | test devices_v2_webhooks


# **devices_v2_webhooks_create**
> ArduinoDevicev2Webhook devices_v2_webhooks_create(id, arduino_devicev2_webhook)

create devices_v2_webhooks

Creates a new webhook associated to a device

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
api_instance = iot_api_client.DevicesV2WebhooksApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
arduino_devicev2_webhook = iot_api_client.ArduinoDevicev2Webhook() # ArduinoDevicev2Webhook | 

try:
    # create devices_v2_webhooks
    api_response = api_instance.devices_v2_webhooks_create(id, arduino_devicev2_webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2WebhooksApi->devices_v2_webhooks_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **arduino_devicev2_webhook** | [**ArduinoDevicev2Webhook**](ArduinoDevicev2Webhook.md)|  | 

### Return type

[**ArduinoDevicev2Webhook**](ArduinoDevicev2Webhook.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.devicev2.webhook+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_webhooks_delete**
> devices_v2_webhooks_delete(id, wid)

delete devices_v2_webhooks

Removes a webhook associated to a device

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
api_instance = iot_api_client.DevicesV2WebhooksApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
wid = 'wid_example' # str | The id of the webhook

try:
    # delete devices_v2_webhooks
    api_instance.devices_v2_webhooks_delete(id, wid)
except ApiException as e:
    print("Exception when calling DevicesV2WebhooksApi->devices_v2_webhooks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **wid** | **str**| The id of the webhook | 

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

# **devices_v2_webhooks_test**
> devices_v2_webhooks_test(id, arduino_devicev2_webhook, wid=wid)

test devices_v2_webhooks

Tests a webhook

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
api_instance = iot_api_client.DevicesV2WebhooksApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
arduino_devicev2_webhook = iot_api_client.ArduinoDevicev2Webhook() # ArduinoDevicev2Webhook | 
wid = 'wid_example' # str | The id of the webhook (optional)

try:
    # test devices_v2_webhooks
    api_instance.devices_v2_webhooks_test(id, arduino_devicev2_webhook, wid=wid)
except ApiException as e:
    print("Exception when calling DevicesV2WebhooksApi->devices_v2_webhooks_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **arduino_devicev2_webhook** | [**ArduinoDevicev2Webhook**](ArduinoDevicev2Webhook.md)|  | 
 **wid** | **str**| The id of the webhook | [optional] 

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


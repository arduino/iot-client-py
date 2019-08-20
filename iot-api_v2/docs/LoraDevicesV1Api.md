# iot_api_client.LoraDevicesV1Api

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lora_devices_v1_create**](LoraDevicesV1Api.md#lora_devices_v1_create) | **PUT** /iot/v1/lora-devices/ | create lora_devices_v1


# **lora_devices_v1_create**
> ArduinoLoradevicev1 lora_devices_v1_create(create_lora_devices_v1_payload)

create lora_devices_v1

Create a new lora device. Its info are saved on our database, and on the a2a network. Creates a device_v2 automatically

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
api_instance = iot_api_client.LoraDevicesV1Api(iot_api_client.ApiClient(configuration))
create_lora_devices_v1_payload = iot_api_client.CreateLoraDevicesV1Payload() # CreateLoraDevicesV1Payload | 

try:
    # create lora_devices_v1
    api_response = api_instance.lora_devices_v1_create(create_lora_devices_v1_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoraDevicesV1Api->lora_devices_v1_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_lora_devices_v1_payload** | [**CreateLoraDevicesV1Payload**](CreateLoraDevicesV1Payload.md)|  | 

### Return type

[**ArduinoLoradevicev1**](ArduinoLoradevicev1.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.loradevicev1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


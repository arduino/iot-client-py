# iot_api_client.LoraDevicesV1Api

All URIs are relative to *https://api2.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lora_devices_v1_create**](LoraDevicesV1Api.md#lora_devices_v1_create) | **PUT** /iot/v1/lora-devices/ | create lora_devices_v1


# **lora_devices_v1_create**
> ArduinoLoradevicev1 lora_devices_v1_create(create_lora_devices_v1_payload, x_organization=x_organization)

create lora_devices_v1

Create a new lora device. Its info are saved on our database, and on the lora provider network. Creates a device_v2 automatically

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_loradevicev1 import ArduinoLoradevicev1
from iot_api_client.models.create_lora_devices_v1_payload import CreateLoraDevicesV1Payload
from iot_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api2.arduino.cc
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.LoraDevicesV1Api(api_client)
    create_lora_devices_v1_payload = iot_api_client.CreateLoraDevicesV1Payload() # CreateLoraDevicesV1Payload | 
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # create lora_devices_v1
        api_response = api_instance.lora_devices_v1_create(create_lora_devices_v1_payload, x_organization=x_organization)
        print("The response of LoraDevicesV1Api->lora_devices_v1_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoraDevicesV1Api->lora_devices_v1_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_lora_devices_v1_payload** | [**CreateLoraDevicesV1Payload**](CreateLoraDevicesV1Payload.md)|  | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

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


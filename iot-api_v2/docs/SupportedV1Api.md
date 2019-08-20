# iot_api_client.SupportedV1Api

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**supported_v1_devices**](SupportedV1Api.md#supported_v1_devices) | **GET** /iot/v1/supported/devices | devices supported_v1


# **supported_v1_devices**
> list[ArduinoSupporteddevicev1] supported_v1_devices()

devices supported_v1

Returns a list of the supported devices

### Example

```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iot_api_client.SupportedV1Api()

try:
    # devices supported_v1
    api_response = api_instance.supported_v1_devices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportedV1Api->supported_v1_devices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ArduinoSupporteddevicev1]**](ArduinoSupporteddevicev1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.supporteddevicev1+json; type=collection

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# iot_api_client.LoraFreqPlanV1Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lora_freq_plan_v1_list**](LoraFreqPlanV1Api.md#lora_freq_plan_v1_list) | **GET** /v1/lora-freq-plans/ | list lora_freq_plan_v1


# **lora_freq_plan_v1_list**
> ArduinoLorafreqplansv1 lora_freq_plan_v1_list()

list lora_freq_plan_v1

List the lora frequency plans supported

### Example

```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)


# Enter a context with an instance of the API client
with iot_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.LoraFreqPlanV1Api(api_client)
    
    try:
        # list lora_freq_plan_v1
        api_response = api_instance.lora_freq_plan_v1_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoraFreqPlanV1Api->lora_freq_plan_v1_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArduinoLorafreqplansv1**](ArduinoLorafreqplansv1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


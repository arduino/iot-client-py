<a name="__pageTop"></a>
# iot_api_client.apis.tags.lora_freq_plan_v1_api.LoraFreqPlanV1Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lora_freq_plan_v1_list**](#lora_freq_plan_v1_list) | **get** /v1/lora-freq-plans/ | list lora_freq_plan_v1

# **lora_freq_plan_v1_list**
<a name="lora_freq_plan_v1_list"></a>
> ArduinoLorafreqplansv1 lora_freq_plan_v1_list()

list lora_freq_plan_v1

List the lora frequency plans supported

### Example

```python
import iot_api_client
from iot_api_client.apis.tags import lora_freq_plan_v1_api
from iot_api_client.model.arduino_lorafreqplansv1 import ArduinoLorafreqplansv1
from iot_api_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lora_freq_plan_v1_api.LoraFreqPlanV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # list lora_freq_plan_v1
        api_response = api_instance.lora_freq_plan_v1_list()
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling LoraFreqPlanV1Api->lora_freq_plan_v1_list: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#lora_freq_plan_v1_list.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#lora_freq_plan_v1_list.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#lora_freq_plan_v1_list.ApiResponseFor500) | Internal Server Error

#### lora_freq_plan_v1_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoLorafreqplansv1**](../../models/ArduinoLorafreqplansv1.md) |  | 


#### lora_freq_plan_v1_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### lora_freq_plan_v1_list.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


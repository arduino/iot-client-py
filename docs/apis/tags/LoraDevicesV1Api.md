<a name="__pageTop"></a>
# iot_api_client.apis.tags.lora_devices_v1_api.LoraDevicesV1Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lora_devices_v1_create**](#lora_devices_v1_create) | **put** /v1/lora-devices/ | create lora_devices_v1

# **lora_devices_v1_create**
<a name="lora_devices_v1_create"></a>
> ArduinoLoradevicev1 lora_devices_v1_create(create_lora_devices_v1_payload)

create lora_devices_v1

Create a new lora device. Its info are saved on our database, and on the lora provider network. Creates a device_v2 automatically

### Example

```python
import iot_api_client
from iot_api_client.apis.tags import lora_devices_v1_api
from iot_api_client.model.arduino_loradevicev1 import ArduinoLoradevicev1
from iot_api_client.model.create_lora_devices_v1_payload import CreateLoraDevicesV1Payload
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lora_devices_v1_api.LoraDevicesV1Api(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = CreateLoraDevicesV1Payload(
        app="app_example",
        app_eui="w8q6zgckec0l3o4g",
        app_key="w8q6zgckec0l3o4g",
        eui="w8q6zgckec0l3o4g",
        frequency_plan="EU_863_870_TTN",
        name="name_example",
        serial="serial_example",
        type="lora-device",
        user_id="user_id_example",
    )
    try:
        # create lora_devices_v1
        api_response = api_instance.lora_devices_v1_create(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling LoraDevicesV1Api->lora_devices_v1_create: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = CreateLoraDevicesV1Payload(
        app="app_example",
        app_eui="w8q6zgckec0l3o4g",
        app_key="w8q6zgckec0l3o4g",
        eui="w8q6zgckec0l3o4g",
        frequency_plan="EU_863_870_TTN",
        name="name_example",
        serial="serial_example",
        type="lora-device",
        user_id="user_id_example",
    )
    try:
        # create lora_devices_v1
        api_response = api_instance.lora_devices_v1_create(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling LoraDevicesV1Api->lora_devices_v1_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.loradevicev1+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateLoraDevicesV1Payload**](../../models/CreateLoraDevicesV1Payload.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateLoraDevicesV1Payload**](../../models/CreateLoraDevicesV1Payload.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#lora_devices_v1_create.ApiResponseFor201) | Created

#### lora_devices_v1_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndArduinoLoradevicev1json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationVndArduinoLoradevicev1json
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoLoradevicev1**](../../models/ArduinoLoradevicev1.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


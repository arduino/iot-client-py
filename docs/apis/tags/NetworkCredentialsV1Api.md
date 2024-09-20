<a name="__pageTop"></a>
# iot_api_client.apis.tags.network_credentials_v1_api.NetworkCredentialsV1Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_credentials_v1_show**](#network_credentials_v1_show) | **get** /v1/network_credentials/{type} | show network_credentials_v1
[**network_credentials_v1_show_by_device**](#network_credentials_v1_show_by_device) | **get** /v1/network_credentials/{type}/connections | showByDevice network_credentials_v1

# **network_credentials_v1_show**
<a name="network_credentials_v1_show"></a>
> ArduinoCredentialsv1Collection network_credentials_v1_show(type)

show network_credentials_v1

Show required network credentials depending on device type

### Example

```python
import iot_api_client
from iot_api_client.apis.tags import network_credentials_v1_api
from iot_api_client.model.arduino_credentialsv1_collection import ArduinoCredentialsv1Collection
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
    api_instance = network_credentials_v1_api.NetworkCredentialsV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'type': "mkrwifi1010",
    }
    query_params = {
    }
    try:
        # show network_credentials_v1
        api_response = api_instance.network_credentials_v1_show(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling NetworkCredentialsV1Api->network_credentials_v1_show: %s\n" % e)

    # example passing only optional values
    path_params = {
        'type': "mkrwifi1010",
    }
    query_params = {
        'connection': "wifi",
    }
    try:
        # show network_credentials_v1
        api_response = api_instance.network_credentials_v1_show(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling NetworkCredentialsV1Api->network_credentials_v1_show: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.credentialsv1+json; type&#x3D;collection', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
connection | ConnectionSchema | | optional


# ConnectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["wifi", "eth", "wifiandsecret", "gsm", "nb", "lora", "catm1", "cellular", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | 

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["mkrwifi1010", "mkr1000", "nano_33_iot", "mkrgsm1400", "mkrwan1310", "mkrwan1300", "mkrnb1500", "lora-device", "login_and_secretkey_wifi", "envie_m7", "nanorp2040connect", "nicla_vision", "opta", "giga", "portenta_c33", "unor4wifi", "nano_nora", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#network_credentials_v1_show.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#network_credentials_v1_show.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#network_credentials_v1_show.ApiResponseFor404) | Not Found

#### network_credentials_v1_show.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoCredentialsv1jsonTypecollection, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoCredentialsv1jsonTypecollection
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoCredentialsv1Collection**](../../models/ArduinoCredentialsv1Collection.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoCredentialsv1Collection**](../../models/ArduinoCredentialsv1Collection.md) |  | 


#### network_credentials_v1_show.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoCredentialsv1jsonTypecollection, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoCredentialsv1jsonTypecollection
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### network_credentials_v1_show.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **network_credentials_v1_show_by_device**
<a name="network_credentials_v1_show_by_device"></a>
> network_credentials_v1_show_by_device(type)

showByDevice network_credentials_v1

Show available connection types depending on device type

### Example

```python
import iot_api_client
from iot_api_client.apis.tags import network_credentials_v1_api
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
    api_instance = network_credentials_v1_api.NetworkCredentialsV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'type': "mkrwifi1010",
    }
    try:
        # showByDevice network_credentials_v1
        api_response = api_instance.network_credentials_v1_show_by_device(
            path_params=path_params,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling NetworkCredentialsV1Api->network_credentials_v1_show_by_device: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | 

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["mkrwifi1010", "mkr1000", "nano_33_iot", "mkrgsm1400", "mkrwan1310", "mkrwan1300", "mkrnb1500", "lora-device", "login_and_secretkey_wifi", "envie_m7", "nanorp2040connect", "nicla_vision", "opta", "giga", "portenta_c33", "unor4wifi", "nano_nora", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#network_credentials_v1_show_by_device.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#network_credentials_v1_show_by_device.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#network_credentials_v1_show_by_device.ApiResponseFor404) | Not Found

#### network_credentials_v1_show_by_device.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### network_credentials_v1_show_by_device.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### network_credentials_v1_show_by_device.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


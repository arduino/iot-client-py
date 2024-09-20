<a name="__pageTop"></a>
# iot_api_client.apis.tags.devices_v2_ota_api.DevicesV2OtaApi

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_ota_send**](#devices_v2_ota_send) | **put** /v2/devices/{id}/ota | send devices_v2_ota
[**devices_v2_ota_upload**](#devices_v2_ota_upload) | **post** /v2/devices/{id}/ota | upload devices_v2_ota
[**devices_v2_ota_url**](#devices_v2_ota_url) | **post** /v2/devices/{id}/ota/url | url devices_v2_ota

# **devices_v2_ota_send**
<a name="devices_v2_ota_send"></a>
> devices_v2_ota_send(iddevicev2_otabinaryurl)

send devices_v2_ota

Send a binary url to a device

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_ota_api
from iot_api_client.model.devicev2_otabinaryurl import Devicev2Otabinaryurl
from iot_api_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_ota_api.DevicesV2OtaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = Devicev2Otabinaryurl(
        _async=True,
        binary_key="ota/z/AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJysota",
        expire_in_mins=10,
    )
    try:
        # send devices_v2_ota
        api_response = api_instance.devices_v2_ota_send(
            path_params=path_params,
            body=body,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2OtaApi->devices_v2_ota_send: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.goa.error+json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Devicev2Otabinaryurl**](../../models/Devicev2Otabinaryurl.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**Devicev2Otabinaryurl**](../../models/Devicev2Otabinaryurl.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_ota_send.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#devices_v2_ota_send.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#devices_v2_ota_send.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#devices_v2_ota_send.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#devices_v2_ota_send.ApiResponseFor404) | Not Found
410 | [ApiResponseFor410](#devices_v2_ota_send.ApiResponseFor410) | Gone
412 | [ApiResponseFor412](#devices_v2_ota_send.ApiResponseFor412) | Precondition Failed
500 | [ApiResponseFor500](#devices_v2_ota_send.ApiResponseFor500) | Internal Server Error

#### devices_v2_ota_send.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_ota_send.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_ota_send.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndGoaErrorjson, SchemaFor400ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_send.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndGoaErrorjson, SchemaFor401ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_send.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationVndGoaErrorjson, SchemaFor404ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor404ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_send.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor410ResponseBodyApplicationVndGoaErrorjson, SchemaFor410ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor410ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor410ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_send.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor412ResponseBodyApplicationVndGoaErrorjson, SchemaFor412ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor412ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor412ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_send.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndGoaErrorjson, SchemaFor500ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_ota_upload**
<a name="devices_v2_ota_upload"></a>
> ArduinoDevicev2Otaupload devices_v2_ota_upload(id)

upload devices_v2_ota

Upload a binary and send it to a device

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_ota_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_devicev2_otaupload import ArduinoDevicev2Otaupload
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_ota_api.DevicesV2OtaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # upload devices_v2_ota
        api_response = api_instance.devices_v2_ota_upload(
            path_params=path_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2OtaApi->devices_v2_ota_upload: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    body = dict(
        _async=True,
        expire_in_mins=10,
        ota_file=open('/path/to/file', 'rb'),
    )
    try:
        # upload devices_v2_ota
        api_response = api_instance.devices_v2_ota_upload(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2OtaApi->devices_v2_ota_upload: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.devicev2.otaupload+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ota_file** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | OTA file | 
**async** | bool,  | BoolClass,  | If false, wait for the full OTA process, until it gets a result from the device | [optional] if omitted the server will use the default value of True
**expire_in_mins** | decimal.Decimal, int,  | decimal.Decimal,  | Binary expire time in minutes, default 10 mins | [optional] if omitted the server will use the default value of 10
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_ota_upload.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#devices_v2_ota_upload.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#devices_v2_ota_upload.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#devices_v2_ota_upload.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#devices_v2_ota_upload.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#devices_v2_ota_upload.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#devices_v2_ota_upload.ApiResponseFor409) | Conflict
410 | [ApiResponseFor410](#devices_v2_ota_upload.ApiResponseFor410) | Gone
412 | [ApiResponseFor412](#devices_v2_ota_upload.ApiResponseFor412) | Precondition Failed
500 | [ApiResponseFor500](#devices_v2_ota_upload.ApiResponseFor500) | Internal Server Error

#### devices_v2_ota_upload.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoDevicev2Otauploadjson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoDevicev2Otauploadjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2Otaupload**](../../models/ArduinoDevicev2Otaupload.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2Otaupload**](../../models/ArduinoDevicev2Otaupload.md) |  | 


#### devices_v2_ota_upload.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationVndArduinoDevicev2Otauploadjson, SchemaFor202ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationVndArduinoDevicev2Otauploadjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2Otaupload**](../../models/ArduinoDevicev2Otaupload.md) |  | 


# SchemaFor202ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2Otaupload**](../../models/ArduinoDevicev2Otaupload.md) |  | 


#### devices_v2_ota_upload.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndArduinoDevicev2Otauploadjson, SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndArduinoDevicev2Otauploadjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_upload.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoDevicev2Otauploadjson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoDevicev2Otauploadjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_upload.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationVndArduinoDevicev2Otauploadjson, SchemaFor403ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationVndArduinoDevicev2Otauploadjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor403ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_upload.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationVndArduinoDevicev2Otauploadjson, SchemaFor404ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationVndArduinoDevicev2Otauploadjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor404ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_upload.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_ota_upload.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor410ResponseBodyApplicationVndArduinoDevicev2Otauploadjson, SchemaFor410ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor410ResponseBodyApplicationVndArduinoDevicev2Otauploadjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor410ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_upload.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor412ResponseBodyApplicationVndArduinoDevicev2Otauploadjson, SchemaFor412ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor412ResponseBodyApplicationVndArduinoDevicev2Otauploadjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor412ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_upload.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoDevicev2Otauploadjson, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoDevicev2Otauploadjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_ota_url**
<a name="devices_v2_ota_url"></a>
> devices_v2_ota_url(iddevicev2_otaurlpyalod)

url devices_v2_ota

Generate a url for downloading a binary

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_ota_api
from iot_api_client.model.error import Error
from iot_api_client.model.devicev2_otaurlpyalod import Devicev2Otaurlpyalod
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_ota_api.DevicesV2OtaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = Devicev2Otaurlpyalod(
        binary_key="ota/z/AMDTMv2D2ylmgd10Z3UB6UkJSISSB512iz2DiJysota",
        sha256="62ECB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea",
        user_id="user_id_example",
    )
    try:
        # url devices_v2_ota
        api_response = api_instance.devices_v2_ota_url(
            path_params=path_params,
            body=body,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2OtaApi->devices_v2_ota_url: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.goa.error+json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Devicev2Otaurlpyalod**](../../models/Devicev2Otaurlpyalod.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**Devicev2Otaurlpyalod**](../../models/Devicev2Otaurlpyalod.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_ota_url.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#devices_v2_ota_url.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#devices_v2_ota_url.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#devices_v2_ota_url.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#devices_v2_ota_url.ApiResponseFor404) | Not Found
410 | [ApiResponseFor410](#devices_v2_ota_url.ApiResponseFor410) | Gone
412 | [ApiResponseFor412](#devices_v2_ota_url.ApiResponseFor412) | Precondition Failed
500 | [ApiResponseFor500](#devices_v2_ota_url.ApiResponseFor500) | Internal Server Error

#### devices_v2_ota_url.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_ota_url.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_ota_url.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndGoaErrorjson, SchemaFor400ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_url.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndGoaErrorjson, SchemaFor401ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_url.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationVndGoaErrorjson, SchemaFor404ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor404ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_url.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor410ResponseBodyApplicationVndGoaErrorjson, SchemaFor410ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor410ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor410ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_url.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor412ResponseBodyApplicationVndGoaErrorjson, SchemaFor412ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor412ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor412ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_ota_url.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndGoaErrorjson, SchemaFor500ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


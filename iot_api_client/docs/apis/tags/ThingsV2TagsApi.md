<a name="__pageTop"></a>
# iot_api_client.apis.tags.things_v2_tags_api.ThingsV2TagsApi

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**things_v2_tags_delete**](#things_v2_tags_delete) | **delete** /v2/things/{id}/tags/{key} | delete things_v2_tags
[**things_v2_tags_list**](#things_v2_tags_list) | **get** /v2/things/{id}/tags | list things_v2_tags
[**things_v2_tags_upsert**](#things_v2_tags_upsert) | **put** /v2/things/{id}/tags | upsert things_v2_tags

# **things_v2_tags_delete**
<a name="things_v2_tags_delete"></a>
> things_v2_tags_delete(idkey)

delete things_v2_tags

Delete a tag associated to the thing given its key.

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import things_v2_tags_api
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
    api_instance = things_v2_tags_api.ThingsV2TagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'key': "key_example",
    }
    try:
        # delete things_v2_tags
        api_response = api_instance.things_v2_tags_delete(
            path_params=path_params,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2TagsApi->things_v2_tags_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
key | KeySchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# KeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#things_v2_tags_delete.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#things_v2_tags_delete.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#things_v2_tags_delete.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#things_v2_tags_delete.ApiResponseFor500) | Internal Server Error

#### things_v2_tags_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_tags_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_tags_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_tags_delete.ApiResponseFor500
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

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **things_v2_tags_list**
<a name="things_v2_tags_list"></a>
> ArduinoTags things_v2_tags_list(id)

list things_v2_tags

List tags associated to the thing.

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import things_v2_tags_api
from iot_api_client.model.arduino_tags import ArduinoTags
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
    api_instance = things_v2_tags_api.ThingsV2TagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # list things_v2_tags
        api_response = api_instance.things_v2_tags_list(
            path_params=path_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2TagsApi->things_v2_tags_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

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
200 | [ApiResponseFor200](#things_v2_tags_list.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#things_v2_tags_list.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#things_v2_tags_list.ApiResponseFor500) | Internal Server Error

#### things_v2_tags_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoTags**](../../models/ArduinoTags.md) |  | 


#### things_v2_tags_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_tags_list.ApiResponseFor500
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

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **things_v2_tags_upsert**
<a name="things_v2_tags_upsert"></a>
> things_v2_tags_upsert(idtag)

upsert things_v2_tags

Creates or updates a tag associated to the thing.

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import things_v2_tags_api
from iot_api_client.model.error import Error
from iot_api_client.model.tag import Tag
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
    api_instance = things_v2_tags_api.ThingsV2TagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = Tag(
        key="0",
        value="0",
    )
    try:
        # upsert things_v2_tags
        api_response = api_instance.things_v2_tags_upsert(
            path_params=path_params,
            body=body,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2TagsApi->things_v2_tags_upsert: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Tag**](../../models/Tag.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**Tag**](../../models/Tag.md) |  | 


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
200 | [ApiResponseFor200](#things_v2_tags_upsert.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#things_v2_tags_upsert.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#things_v2_tags_upsert.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#things_v2_tags_upsert.ApiResponseFor500) | Internal Server Error

#### things_v2_tags_upsert.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_tags_upsert.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_tags_upsert.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_tags_upsert.ApiResponseFor500
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

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


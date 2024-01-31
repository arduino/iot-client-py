<a name="__pageTop"></a>
# iot_api_client.apis.tags.properties_v2_api.PropertiesV2Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**properties_v2_create**](#properties_v2_create) | **put** /v2/things/{id}/properties | create properties_v2
[**properties_v2_delete**](#properties_v2_delete) | **delete** /v2/things/{id}/properties/{pid} | delete properties_v2
[**properties_v2_list**](#properties_v2_list) | **get** /v2/things/{id}/properties | list properties_v2
[**properties_v2_publish**](#properties_v2_publish) | **put** /v2/things/{id}/properties/{pid}/publish | publish properties_v2
[**properties_v2_show**](#properties_v2_show) | **get** /v2/things/{id}/properties/{pid} | show properties_v2
[**properties_v2_timeseries**](#properties_v2_timeseries) | **get** /v2/things/{id}/properties/{pid}/timeseries | timeseries properties_v2
[**properties_v2_update**](#properties_v2_update) | **post** /v2/things/{id}/properties/{pid} | update properties_v2

# **properties_v2_create**
<a name="properties_v2_create"></a>
> ArduinoProperty properties_v2_create(idmodel_property)

create properties_v2

Creates a new property associated to a thing

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import properties_v2_api
from iot_api_client.model.arduino_property import ArduinoProperty
from iot_api_client.model.error import Error
from iot_api_client.model.model_property import ModelProperty
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
    api_instance = properties_v2_api.PropertiesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    body = ModelProperty(
        max_value=3.14,
        min_value=3.14,
        name="name_example",
        permission="READ_ONLY",
        persist=True,
        tag=1,
        type="ANALOG",
        update_parameter=3.14,
        update_strategy="ON_CHANGE",
        variable_name="MqXzyCBw3_uufVPIPFhB9JcGRYnua",
    )
    try:
        # create properties_v2
        api_response = api_instance.properties_v2_create(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_create: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = ModelProperty(
        max_value=3.14,
        min_value=3.14,
        name="name_example",
        permission="READ_ONLY",
        persist=True,
        tag=1,
        type="ANALOG",
        update_parameter=3.14,
        update_strategy="ON_CHANGE",
        variable_name="MqXzyCBw3_uufVPIPFhB9JcGRYnua",
    )
    try:
        # create properties_v2
        api_response = api_instance.properties_v2_create(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.property+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelProperty**](../../models/ModelProperty.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelProperty**](../../models/ModelProperty.md) |  | 


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
201 | [ApiResponseFor201](#properties_v2_create.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#properties_v2_create.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#properties_v2_create.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#properties_v2_create.ApiResponseFor404) | Not Found
412 | [ApiResponseFor412](#properties_v2_create.ApiResponseFor412) | Precondition Failed
500 | [ApiResponseFor500](#properties_v2_create.ApiResponseFor500) | Internal Server Error

#### properties_v2_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor201ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationVndArduinoPropertyjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoProperty**](../../models/ArduinoProperty.md) |  | 


# SchemaFor201ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoProperty**](../../models/ArduinoProperty.md) |  | 


#### properties_v2_create.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndArduinoPropertyjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### properties_v2_create.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoPropertyjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### properties_v2_create.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### properties_v2_create.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor412ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor412ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor412ResponseBodyApplicationVndArduinoPropertyjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor412ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### properties_v2_create.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoPropertyjson
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

# **properties_v2_delete**
<a name="properties_v2_delete"></a>
> properties_v2_delete(idpid)

delete properties_v2

Removes a property associated to a thing

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import properties_v2_api
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
    api_instance = properties_v2_api.PropertiesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # delete properties_v2
        api_response = api_instance.properties_v2_delete(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    query_params = {
        'force': False,
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # delete properties_v2
        api_response = api_instance.properties_v2_delete(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.goa.error+json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
force | ForceSchema | | optional


# ForceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
pid | PidSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#properties_v2_delete.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#properties_v2_delete.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#properties_v2_delete.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#properties_v2_delete.ApiResponseFor500) | Internal Server Error

#### properties_v2_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### properties_v2_delete.ApiResponseFor401
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


#### properties_v2_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### properties_v2_delete.ApiResponseFor500
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

# **properties_v2_list**
<a name="properties_v2_list"></a>
> ArduinoPropertyCollection properties_v2_list(id)

list properties_v2

Returns the list of properties associated to the thing

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import properties_v2_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_property_collection import ArduinoPropertyCollection
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
    api_instance = properties_v2_api.PropertiesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # list properties_v2
        api_response = api_instance.properties_v2_list(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'show_deleted': False,
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # list properties_v2
        api_response = api_instance.properties_v2_list(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.property+json; type&#x3D;collection', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
show_deleted | ShowDeletedSchema | | optional


# ShowDeletedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

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
200 | [ApiResponseFor200](#properties_v2_list.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#properties_v2_list.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#properties_v2_list.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#properties_v2_list.ApiResponseFor500) | Internal Server Error

#### properties_v2_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoPropertyjsonTypecollection, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoPropertyjsonTypecollection
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoPropertyCollection**](../../models/ArduinoPropertyCollection.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoPropertyCollection**](../../models/ArduinoPropertyCollection.md) |  | 


#### properties_v2_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoPropertyjsonTypecollection, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoPropertyjsonTypecollection
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### properties_v2_list.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationVndArduinoPropertyjsonTypecollection, SchemaFor404ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationVndArduinoPropertyjsonTypecollection
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor404ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### properties_v2_list.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoPropertyjsonTypecollection, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoPropertyjsonTypecollection
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

# **properties_v2_publish**
<a name="properties_v2_publish"></a>
> properties_v2_publish(idpidproperty_value)

publish properties_v2

Publish a property value to MQTT

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import properties_v2_api
from iot_api_client.model.property_value import PropertyValue
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
    api_instance = properties_v2_api.PropertiesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    header_params = {
    }
    body = PropertyValue(
        device_id="device_id_example",
        value=None,
    )
    try:
        # publish properties_v2
        api_response = api_instance.properties_v2_publish(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_publish: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = PropertyValue(
        device_id="device_id_example",
        value=None,
    )
    try:
        # publish properties_v2
        api_response = api_instance.properties_v2_publish(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_publish: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
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
[**PropertyValue**](../../models/PropertyValue.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertyValue**](../../models/PropertyValue.md) |  | 


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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
pid | PidSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#properties_v2_publish.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#properties_v2_publish.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#properties_v2_publish.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#properties_v2_publish.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#properties_v2_publish.ApiResponseFor500) | Internal Server Error

#### properties_v2_publish.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### properties_v2_publish.ApiResponseFor400
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


#### properties_v2_publish.ApiResponseFor401
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


#### properties_v2_publish.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### properties_v2_publish.ApiResponseFor500
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

# **properties_v2_show**
<a name="properties_v2_show"></a>
> ArduinoProperty properties_v2_show(idpid)

show properties_v2

Returns the property requested by the user

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import properties_v2_api
from iot_api_client.model.arduino_property import ArduinoProperty
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
    api_instance = properties_v2_api.PropertiesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # show properties_v2
        api_response = api_instance.properties_v2_show(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_show: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    query_params = {
        'show_deleted': False,
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # show properties_v2
        api_response = api_instance.properties_v2_show(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_show: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.property+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
show_deleted | ShowDeletedSchema | | optional


# ShowDeletedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
pid | PidSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#properties_v2_show.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#properties_v2_show.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#properties_v2_show.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#properties_v2_show.ApiResponseFor500) | Internal Server Error

#### properties_v2_show.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoPropertyjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoProperty**](../../models/ArduinoProperty.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoProperty**](../../models/ArduinoProperty.md) |  | 


#### properties_v2_show.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoPropertyjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### properties_v2_show.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor404ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationVndArduinoPropertyjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor404ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### properties_v2_show.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoPropertyjson
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

# **properties_v2_timeseries**
<a name="properties_v2_timeseries"></a>
> ArduinoTimeseriesmedia properties_v2_timeseries(idpid)

timeseries properties_v2

Get numerical property's historic data binned on a specified time interval (note: the total number of data points should NOT be greater than 1000 otherwise the result will be truncated)

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import properties_v2_api
from iot_api_client.model.arduino_timeseriesmedia import ArduinoTimeseriesmedia
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
    api_instance = properties_v2_api.PropertiesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # timeseries properties_v2
        api_response = api_instance.properties_v2_timeseries(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_timeseries: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    query_params = {
        'aggregation': "AVG",
        'desc': False,
        'from': "from_example",
        'interval': 1,
        'to': "to_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # timeseries properties_v2
        api_response = api_instance.properties_v2_timeseries(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_timeseries: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.timeseriesmedia+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
aggregation | AggregationSchema | | optional
desc | DescSchema | | optional
from | ModelFromSchema | | optional
interval | IntervalSchema | | optional
to | ToSchema | | optional


# AggregationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["AVG", "MIN", "MAX", "SUM", "COUNT", "PCT_99", "PCT_95", "PCT_90", "PCT_75", "PCT_50", "PCT_15", "PCT_5", ] 

# DescSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# ModelFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IntervalSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ToSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
pid | PidSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#properties_v2_timeseries.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#properties_v2_timeseries.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#properties_v2_timeseries.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#properties_v2_timeseries.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#properties_v2_timeseries.ApiResponseFor500) | Internal Server Error

#### properties_v2_timeseries.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoTimeseriesmediajson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoTimeseriesmediajson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoTimeseriesmedia**](../../models/ArduinoTimeseriesmedia.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoTimeseriesmedia**](../../models/ArduinoTimeseriesmedia.md) |  | 


#### properties_v2_timeseries.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndArduinoTimeseriesmediajson, SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndArduinoTimeseriesmediajson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### properties_v2_timeseries.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### properties_v2_timeseries.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### properties_v2_timeseries.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoTimeseriesmediajson, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoTimeseriesmediajson
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

# **properties_v2_update**
<a name="properties_v2_update"></a>
> ArduinoProperty properties_v2_update(idpidmodel_property)

update properties_v2

Updates a property associated to a thing

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import properties_v2_api
from iot_api_client.model.arduino_property import ArduinoProperty
from iot_api_client.model.error import Error
from iot_api_client.model.model_property import ModelProperty
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
    api_instance = properties_v2_api.PropertiesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    header_params = {
    }
    body = ModelProperty(
        max_value=3.14,
        min_value=3.14,
        name="name_example",
        permission="READ_ONLY",
        persist=True,
        tag=1,
        type="ANALOG",
        update_parameter=3.14,
        update_strategy="ON_CHANGE",
        variable_name="MqXzyCBw3_uufVPIPFhB9JcGRYnua",
    )
    try:
        # update properties_v2
        api_response = api_instance.properties_v2_update(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_update: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = ModelProperty(
        max_value=3.14,
        min_value=3.14,
        name="name_example",
        permission="READ_ONLY",
        persist=True,
        tag=1,
        type="ANALOG",
        update_parameter=3.14,
        update_strategy="ON_CHANGE",
        variable_name="MqXzyCBw3_uufVPIPFhB9JcGRYnua",
    )
    try:
        # update properties_v2
        api_response = api_instance.properties_v2_update(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertiesV2Api->properties_v2_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.property+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelProperty**](../../models/ModelProperty.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelProperty**](../../models/ModelProperty.md) |  | 


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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
pid | PidSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#properties_v2_update.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#properties_v2_update.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#properties_v2_update.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#properties_v2_update.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#properties_v2_update.ApiResponseFor500) | Internal Server Error

#### properties_v2_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoPropertyjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoProperty**](../../models/ArduinoProperty.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoProperty**](../../models/ArduinoProperty.md) |  | 


#### properties_v2_update.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndArduinoPropertyjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### properties_v2_update.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoPropertyjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### properties_v2_update.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor404ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationVndArduinoPropertyjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor404ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### properties_v2_update.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoPropertyjson, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoPropertyjson
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


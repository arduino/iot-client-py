<a name="__pageTop"></a>
# iot_api_client.apis.tags.things_v2_api.ThingsV2Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**things_v2_create**](#things_v2_create) | **put** /v2/things | create things_v2
[**things_v2_create_sketch**](#things_v2_create_sketch) | **put** /v2/things/{id}/sketch | createSketch things_v2
[**things_v2_delete**](#things_v2_delete) | **delete** /v2/things/{id} | delete things_v2
[**things_v2_delete_sketch**](#things_v2_delete_sketch) | **delete** /v2/things/{id}/sketch | deleteSketch things_v2
[**things_v2_list**](#things_v2_list) | **get** /v2/things | list things_v2
[**things_v2_show**](#things_v2_show) | **get** /v2/things/{id} | show things_v2
[**things_v2_update**](#things_v2_update) | **post** /v2/things/{id} | update things_v2
[**things_v2_update_sketch**](#things_v2_update_sketch) | **put** /v2/things/{id}/sketch/{sketchId} | updateSketch things_v2

# **things_v2_create**
<a name="things_v2_create"></a>
> ArduinoThing things_v2_create(thing_create)

create things_v2

Creates a new thing associated to the user

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import things_v2_api
from iot_api_client.model.error import Error
from iot_api_client.model.thing_create import ThingCreate
from iot_api_client.model.arduino_thing import ArduinoThing
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
    api_instance = things_v2_api.ThingsV2Api(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    header_params = {
    }
    body = ThingCreate(
        device_id="device_id_example",
        id="id_example",
        name="A",
        properties=[
            ModelProperty(
                max_value=3.14,
                min_value=3.14,
                name="name_example",
                permission="READ_ONLY",
                persist=True,
                tag=3.14,
                type="ANALOG",
                update_parameter=3.14,
                update_strategy="ON_CHANGE",
                variable_name="MqXzyCBw3_uufVPIPFhB9JcGRYnua",
            )
        ],
        timezone="America/New_York",
        webhook_active=True,
        webhook_uri="webhook_uri_example",
    )
    try:
        # create things_v2
        api_response = api_instance.things_v2_create(
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_create: %s\n" % e)

    # example passing only optional values
    query_params = {
        'force': False,
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = ThingCreate(
        device_id="device_id_example",
        id="id_example",
        name="A",
        properties=[
            ModelProperty(
                max_value=3.14,
                min_value=3.14,
                name="name_example",
                permission="READ_ONLY",
                persist=True,
                tag=3.14,
                type="ANALOG",
                update_parameter=3.14,
                update_strategy="ON_CHANGE",
                variable_name="MqXzyCBw3_uufVPIPFhB9JcGRYnua",
            )
        ],
        timezone="America/New_York",
        webhook_active=True,
        webhook_uri="webhook_uri_example",
    )
    try:
        # create things_v2
        api_response = api_instance.things_v2_create(
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ThingCreate**](../../models/ThingCreate.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ThingCreate**](../../models/ThingCreate.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#things_v2_create.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#things_v2_create.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#things_v2_create.ApiResponseFor401) | Unauthorized
409 | [ApiResponseFor409](#things_v2_create.ApiResponseFor409) | Conflict
412 | [ApiResponseFor412](#things_v2_create.ApiResponseFor412) | Precondition Failed
500 | [ApiResponseFor500](#things_v2_create.ApiResponseFor500) | Internal Server Error

#### things_v2_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoThing**](../../models/ArduinoThing.md) |  | 


#### things_v2_create.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_create.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_create.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_create.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor412ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor412ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_create.ApiResponseFor500
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

# **things_v2_create_sketch**
<a name="things_v2_create_sketch"></a>
> ArduinoThing things_v2_create_sketch(idthing_sketch)

createSketch things_v2

Creates a new sketch thing associated to the thing

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import things_v2_api
from iot_api_client.model.error import Error
from iot_api_client.model.thing_sketch import ThingSketch
from iot_api_client.model.arduino_thing import ArduinoThing
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
    api_instance = things_v2_api.ThingsV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    body = ThingSketch(
        sketch_version="v1",
    )
    try:
        # createSketch things_v2
        api_response = api_instance.things_v2_create_sketch(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_create_sketch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = ThingSketch(
        sketch_version="v1",
    )
    try:
        # createSketch things_v2
        api_response = api_instance.things_v2_create_sketch(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_create_sketch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
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
[**ThingSketch**](../../models/ThingSketch.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ThingSketch**](../../models/ThingSketch.md) |  | 


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
201 | [ApiResponseFor201](#things_v2_create_sketch.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#things_v2_create_sketch.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#things_v2_create_sketch.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#things_v2_create_sketch.ApiResponseFor404) | Not Found
412 | [ApiResponseFor412](#things_v2_create_sketch.ApiResponseFor412) | Precondition Failed
500 | [ApiResponseFor500](#things_v2_create_sketch.ApiResponseFor500) | Internal Server Error

#### things_v2_create_sketch.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoThing**](../../models/ArduinoThing.md) |  | 


#### things_v2_create_sketch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_create_sketch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_create_sketch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_create_sketch.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor412ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor412ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_create_sketch.ApiResponseFor500
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

# **things_v2_delete**
<a name="things_v2_delete"></a>
> things_v2_delete(id)

delete things_v2

Removes a thing associated to the user

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import things_v2_api
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
    api_instance = things_v2_api.ThingsV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # delete things_v2
        api_response = api_instance.things_v2_delete(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'force': False,
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # delete things_v2
        api_response = api_instance.things_v2_delete(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#things_v2_delete.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#things_v2_delete.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#things_v2_delete.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#things_v2_delete.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#things_v2_delete.ApiResponseFor500) | Internal Server Error

#### things_v2_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_delete.ApiResponseFor500
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

# **things_v2_delete_sketch**
<a name="things_v2_delete_sketch"></a>
> ArduinoThing things_v2_delete_sketch(id)

deleteSketch things_v2

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import things_v2_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_thing import ArduinoThing
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
    api_instance = things_v2_api.ThingsV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    try:
        # deleteSketch things_v2
        api_response = api_instance.things_v2_delete_sketch(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_delete_sketch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # deleteSketch things_v2
        api_response = api_instance.things_v2_delete_sketch(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_delete_sketch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

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
200 | [ApiResponseFor200](#things_v2_delete_sketch.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#things_v2_delete_sketch.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#things_v2_delete_sketch.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#things_v2_delete_sketch.ApiResponseFor500) | Internal Server Error

#### things_v2_delete_sketch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoThing**](../../models/ArduinoThing.md) |  | 


#### things_v2_delete_sketch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_delete_sketch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_delete_sketch.ApiResponseFor500
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

# **things_v2_list**
<a name="things_v2_list"></a>
> ArduinoThingCollection things_v2_list()

list things_v2

Returns the list of things associated to the user

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import things_v2_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_thing_collection import ArduinoThingCollection
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
    api_instance = things_v2_api.ThingsV2Api(api_client)

    # example passing only optional values
    query_params = {
        'across_user_ids': False,
        'device_id': "device_id_example",
        'ids': [
        "ids_example"
    ],
        'show_deleted': False,
        'show_properties': False,
        'tags': [
        "0:@9JLe6iL71-aa-.Ctq@dcsc.3-8@1gAa8Xa6u61"
    ],
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # list things_v2
        api_response = api_instance.things_v2_list(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
across_user_ids | AcrossUserIdsSchema | | optional
device_id | DeviceIdSchema | | optional
ids | IdsSchema | | optional
show_deleted | ShowDeletedSchema | | optional
show_properties | ShowPropertiesSchema | | optional
tags | TagsSchema | | optional


# AcrossUserIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# DeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ShowDeletedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# ShowPropertiesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# TagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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
200 | [ApiResponseFor200](#things_v2_list.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#things_v2_list.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#things_v2_list.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#things_v2_list.ApiResponseFor500) | Internal Server Error

#### things_v2_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoThingCollection**](../../models/ArduinoThingCollection.md) |  | 


#### things_v2_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_list.ApiResponseFor500
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

# **things_v2_show**
<a name="things_v2_show"></a>
> ArduinoThing things_v2_show(id)

show things_v2

Returns the thing requested by the user

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import things_v2_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_thing import ArduinoThing
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
    api_instance = things_v2_api.ThingsV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # show things_v2
        api_response = api_instance.things_v2_show(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_show: %s\n" % e)

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
        # show things_v2
        api_response = api_instance.things_v2_show(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_show: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
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
200 | [ApiResponseFor200](#things_v2_show.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#things_v2_show.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#things_v2_show.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#things_v2_show.ApiResponseFor500) | Internal Server Error

#### things_v2_show.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoThing**](../../models/ArduinoThing.md) |  | 


#### things_v2_show.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_show.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_show.ApiResponseFor500
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

# **things_v2_update**
<a name="things_v2_update"></a>
> ArduinoThing things_v2_update(idthing_update)

update things_v2

Updates a thing associated to the user

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import things_v2_api
from iot_api_client.model.thing_update import ThingUpdate
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_thing import ArduinoThing
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
    api_instance = things_v2_api.ThingsV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    header_params = {
    }
    body = ThingUpdate(
        device_id="device_id_example",
        id="id_example",
        name="A",
        properties=[
            ModelProperty(
                max_value=3.14,
                min_value=3.14,
                name="name_example",
                permission="READ_ONLY",
                persist=True,
                tag=3.14,
                type="ANALOG",
                update_parameter=3.14,
                update_strategy="ON_CHANGE",
                variable_name="MqXzyCBw3_uufVPIPFhB9JcGRYnua",
            )
        ],
        timezone="timezone_example",
        webhook_active=True,
        webhook_uri="webhook_uri_example",
    )
    try:
        # update things_v2
        api_response = api_instance.things_v2_update(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_update: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'force': False,
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = ThingUpdate(
        device_id="device_id_example",
        id="id_example",
        name="A",
        properties=[
            ModelProperty(
                max_value=3.14,
                min_value=3.14,
                name="name_example",
                permission="READ_ONLY",
                persist=True,
                tag=3.14,
                type="ANALOG",
                update_parameter=3.14,
                update_strategy="ON_CHANGE",
                variable_name="MqXzyCBw3_uufVPIPFhB9JcGRYnua",
            )
        ],
        timezone="timezone_example",
        webhook_active=True,
        webhook_uri="webhook_uri_example",
    )
    try:
        # update things_v2
        api_response = api_instance.things_v2_update(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
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
[**ThingUpdate**](../../models/ThingUpdate.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ThingUpdate**](../../models/ThingUpdate.md) |  | 


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

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#things_v2_update.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#things_v2_update.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#things_v2_update.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#things_v2_update.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#things_v2_update.ApiResponseFor409) | Conflict
412 | [ApiResponseFor412](#things_v2_update.ApiResponseFor412) | Precondition Failed
500 | [ApiResponseFor500](#things_v2_update.ApiResponseFor500) | Internal Server Error

#### things_v2_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoThing**](../../models/ArduinoThing.md) |  | 


#### things_v2_update.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_update.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_update.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_update.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_update.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor412ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor412ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_update.ApiResponseFor500
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

# **things_v2_update_sketch**
<a name="things_v2_update_sketch"></a>
> ArduinoThing things_v2_update_sketch(idsketch_id)

updateSketch things_v2

Update an existing thing sketch

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import things_v2_api
from iot_api_client.model.update_sketch import UpdateSketch
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_thing import ArduinoThing
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
    api_instance = things_v2_api.ThingsV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'sketchId': "sketchId_example",
    }
    header_params = {
    }
    try:
        # updateSketch things_v2
        api_response = api_instance.things_v2_update_sketch(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_update_sketch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
        'sketchId': "sketchId_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = UpdateSketch(
        sketch_version="v1",
    )
    try:
        # updateSketch things_v2
        api_response = api_instance.things_v2_update_sketch(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_update_sketch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
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
[**UpdateSketch**](../../models/UpdateSketch.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateSketch**](../../models/UpdateSketch.md) |  | 


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
sketchId | SketchIdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SketchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#things_v2_update_sketch.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#things_v2_update_sketch.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#things_v2_update_sketch.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#things_v2_update_sketch.ApiResponseFor404) | Not Found
412 | [ApiResponseFor412](#things_v2_update_sketch.ApiResponseFor412) | Precondition Failed
500 | [ApiResponseFor500](#things_v2_update_sketch.ApiResponseFor500) | Internal Server Error

#### things_v2_update_sketch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoThing**](../../models/ArduinoThing.md) |  | 


#### things_v2_update_sketch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_update_sketch.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### things_v2_update_sketch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_update_sketch.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor412ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor412ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### things_v2_update_sketch.ApiResponseFor500
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


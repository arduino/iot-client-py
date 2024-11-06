# iot_api_client.ThingsV2Api

All URIs are relative to *https://api2.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**things_v2_clone**](ThingsV2Api.md#things_v2_clone) | **PUT** /iot/v2/things/{id}/clone | clone things_v2
[**things_v2_create**](ThingsV2Api.md#things_v2_create) | **PUT** /iot/v2/things | create things_v2
[**things_v2_create_sketch**](ThingsV2Api.md#things_v2_create_sketch) | **PUT** /iot/v2/things/{id}/sketch | createSketch things_v2
[**things_v2_delete**](ThingsV2Api.md#things_v2_delete) | **DELETE** /iot/v2/things/{id} | delete things_v2
[**things_v2_delete_sketch**](ThingsV2Api.md#things_v2_delete_sketch) | **DELETE** /iot/v2/things/{id}/sketch | deleteSketch things_v2
[**things_v2_list**](ThingsV2Api.md#things_v2_list) | **GET** /iot/v2/things | list things_v2
[**things_v2_show**](ThingsV2Api.md#things_v2_show) | **GET** /iot/v2/things/{id} | show things_v2
[**things_v2_template**](ThingsV2Api.md#things_v2_template) | **GET** /iot/v2/things/{id}/template | template things_v2
[**things_v2_update**](ThingsV2Api.md#things_v2_update) | **POST** /iot/v2/things/{id} | update things_v2
[**things_v2_update_sketch**](ThingsV2Api.md#things_v2_update_sketch) | **PUT** /iot/v2/things/{id}/sketch/{sketchId} | updateSketch things_v2


# **things_v2_clone**
> ArduinoThing things_v2_clone(id, thing_clone, x_organization=x_organization)

clone things_v2

Clone a given thing

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_thing import ArduinoThing
from iot_api_client.models.thing_clone import ThingClone
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    thing_clone = iot_api_client.ThingClone() # ThingClone | Payload to clone a new thing from an existing one
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # clone things_v2
        api_response = api_instance.things_v2_clone(id, thing_clone, x_organization=x_organization)
        print("The response of ThingsV2Api->things_v2_clone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingsV2Api->things_v2_clone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **thing_clone** | [**ThingClone**](ThingClone.md)| Payload to clone a new thing from an existing one | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.thing+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_create**
> ArduinoThing things_v2_create(thing_create, force=force, x_organization=x_organization)

create things_v2

Creates a new thing associated to the user

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_thing import ArduinoThing
from iot_api_client.models.thing_create import ThingCreate
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    thing_create = iot_api_client.ThingCreate() # ThingCreate | Payload to create a new thing
    force = False # bool | If true, detach device from the other thing, and attach to this thing (optional) (default to False)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # create things_v2
        api_response = api_instance.things_v2_create(thing_create, force=force, x_organization=x_organization)
        print("The response of ThingsV2Api->things_v2_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingsV2Api->things_v2_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_create** | [**ThingCreate**](ThingCreate.md)| Payload to create a new thing | 
 **force** | **bool**| If true, detach device from the other thing, and attach to this thing | [optional] [default to False]
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.thing+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_create_sketch**
> ArduinoThing things_v2_create_sketch(id, thing_sketch, x_organization=x_organization)

createSketch things_v2

Creates a new sketch thing associated to the thing

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_thing import ArduinoThing
from iot_api_client.models.thing_sketch import ThingSketch
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    thing_sketch = iot_api_client.ThingSketch() # ThingSketch | ThingSketchPayload describes a sketch of a thing
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # createSketch things_v2
        api_response = api_instance.things_v2_create_sketch(id, thing_sketch, x_organization=x_organization)
        print("The response of ThingsV2Api->things_v2_create_sketch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingsV2Api->things_v2_create_sketch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **thing_sketch** | [**ThingSketch**](ThingSketch.md)| ThingSketchPayload describes a sketch of a thing | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.thing+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_delete**
> things_v2_delete(id, force=force, x_organization=x_organization)

delete things_v2

Removes a thing associated to the user

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    force = False # bool | If true, hard delete the thing (optional) (default to False)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # delete things_v2
        api_instance.things_v2_delete(id, force=force, x_organization=x_organization)
    except Exception as e:
        print("Exception when calling ThingsV2Api->things_v2_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **force** | **bool**| If true, hard delete the thing | [optional] [default to False]
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.goa.error+json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_delete_sketch**
> ArduinoThing things_v2_delete_sketch(id, x_organization=x_organization)

deleteSketch things_v2

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_thing import ArduinoThing
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # deleteSketch things_v2
        api_response = api_instance.things_v2_delete_sketch(id, x_organization=x_organization)
        print("The response of ThingsV2Api->things_v2_delete_sketch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingsV2Api->things_v2_delete_sketch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.thing+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_list**
> List[ArduinoThing] things_v2_list(across_user_ids=across_user_ids, device_id=device_id, ids=ids, show_deleted=show_deleted, show_properties=show_properties, tags=tags, x_organization=x_organization)

list things_v2

Returns the list of things associated to the user

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_thing import ArduinoThing
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    across_user_ids = False # bool | If true, returns all the things (optional) (default to False)
    device_id = 'device_id_example' # str | The id of the device you want to filter (optional)
    ids = ['ids_example'] # List[str] | Filter only the desired things (optional)
    show_deleted = False # bool | If true, shows the soft deleted things (optional) (default to False)
    show_properties = False # bool | If true, returns things with their properties, and last values (optional) (default to False)
    tags = ['tags_example'] # List[str] | Filter by tags (optional)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # list things_v2
        api_response = api_instance.things_v2_list(across_user_ids=across_user_ids, device_id=device_id, ids=ids, show_deleted=show_deleted, show_properties=show_properties, tags=tags, x_organization=x_organization)
        print("The response of ThingsV2Api->things_v2_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingsV2Api->things_v2_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **across_user_ids** | **bool**| If true, returns all the things | [optional] [default to False]
 **device_id** | **str**| The id of the device you want to filter | [optional] 
 **ids** | [**List[str]**](str.md)| Filter only the desired things | [optional] 
 **show_deleted** | **bool**| If true, shows the soft deleted things | [optional] [default to False]
 **show_properties** | **bool**| If true, returns things with their properties, and last values | [optional] [default to False]
 **tags** | [**List[str]**](str.md)| Filter by tags | [optional] 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**List[ArduinoThing]**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.thing+json; type=collection, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_show**
> ArduinoThing things_v2_show(id, show_deleted=show_deleted, x_organization=x_organization)

show things_v2

Returns the thing requested by the user

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_thing import ArduinoThing
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    show_deleted = False # bool | If true, shows the soft deleted thing (optional) (default to False)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # show things_v2
        api_response = api_instance.things_v2_show(id, show_deleted=show_deleted, x_organization=x_organization)
        print("The response of ThingsV2Api->things_v2_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingsV2Api->things_v2_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **show_deleted** | **bool**| If true, shows the soft deleted thing | [optional] [default to False]
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.thing+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_template**
> ArduinoThingtemplate things_v2_template(id, x_organization=x_organization)

template things_v2

Extract template from the given thing

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_thingtemplate import ArduinoThingtemplate
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # template things_v2
        api_response = api_instance.things_v2_template(id, x_organization=x_organization)
        print("The response of ThingsV2Api->things_v2_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingsV2Api->things_v2_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoThingtemplate**](ArduinoThingtemplate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.thingtemplate+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_update**
> ArduinoThing things_v2_update(id, thing_update, force=force, x_organization=x_organization)

update things_v2

Updates a thing associated to the user

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_thing import ArduinoThing
from iot_api_client.models.thing_update import ThingUpdate
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    thing_update = iot_api_client.ThingUpdate() # ThingUpdate | Payload to update an existing thing
    force = False # bool | If true, detach device from the other thing, and attach to this thing (optional) (default to False)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # update things_v2
        api_response = api_instance.things_v2_update(id, thing_update, force=force, x_organization=x_organization)
        print("The response of ThingsV2Api->things_v2_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingsV2Api->things_v2_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **thing_update** | [**ThingUpdate**](ThingUpdate.md)| Payload to update an existing thing | 
 **force** | **bool**| If true, detach device from the other thing, and attach to this thing | [optional] [default to False]
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.thing+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_update_sketch**
> ArduinoThing things_v2_update_sketch(id, sketch_id, x_organization=x_organization, update_sketch=update_sketch)

updateSketch things_v2

Update an existing thing sketch

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_thing import ArduinoThing
from iot_api_client.models.update_sketch import UpdateSketch
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    sketch_id = 'sketch_id_example' # str | The id of the sketch
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)
    update_sketch = iot_api_client.UpdateSketch() # UpdateSketch |  (optional)

    try:
        # updateSketch things_v2
        api_response = api_instance.things_v2_update_sketch(id, sketch_id, x_organization=x_organization, update_sketch=update_sketch)
        print("The response of ThingsV2Api->things_v2_update_sketch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingsV2Api->things_v2_update_sketch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **sketch_id** | **str**| The id of the sketch | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 
 **update_sketch** | [**UpdateSketch**](UpdateSketch.md)|  | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.thing+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


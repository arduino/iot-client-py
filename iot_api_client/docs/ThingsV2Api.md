# iot_api_client.ThingsV2Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**things_v2_create**](ThingsV2Api.md#things_v2_create) | **PUT** /v2/things | create things_v2
[**things_v2_create_sketch**](ThingsV2Api.md#things_v2_create_sketch) | **PUT** /v2/things/{id}/sketch | createSketch things_v2
[**things_v2_delete**](ThingsV2Api.md#things_v2_delete) | **DELETE** /v2/things/{id} | delete things_v2
[**things_v2_delete_sketch**](ThingsV2Api.md#things_v2_delete_sketch) | **DELETE** /v2/things/{id}/sketch | deleteSketch things_v2
[**things_v2_list**](ThingsV2Api.md#things_v2_list) | **GET** /v2/things | list things_v2
[**things_v2_show**](ThingsV2Api.md#things_v2_show) | **GET** /v2/things/{id} | show things_v2
[**things_v2_update**](ThingsV2Api.md#things_v2_update) | **POST** /v2/things/{id} | update things_v2
[**things_v2_update_sketch**](ThingsV2Api.md#things_v2_update_sketch) | **PUT** /v2/things/{id}/sketch/{sketchId} | updateSketch things_v2


# **things_v2_create**
> ArduinoThing things_v2_create(thing_create, force=force, x_organization=x_organization)

create things_v2

Creates a new thing associated to the user

### Example

* OAuth Authentication (oauth2):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    thing_create = iot_api_client.ThingCreate() # ThingCreate | Payload to create a new thing
force = False # bool | If true, detach device from the other thing, and attach to this thing (optional) (default to False)
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # create things_v2
        api_response = api_instance.things_v2_create(thing_create, force=force, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thing_create** | [**ThingCreate**](ThingCreate.md)| Payload to create a new thing | 
 **force** | **bool**| If true, detach device from the other thing, and attach to this thing | [optional] [default to False]
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**409** | Conflict |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_create_sketch**
> ArduinoThing things_v2_create_sketch(id, thing_sketch, x_organization=x_organization)

createSketch things_v2

Creates a new sketch thing associated to the thing

### Example

* OAuth Authentication (oauth2):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
thing_sketch = iot_api_client.ThingSketch() # ThingSketch | ThingSketchPayload describes a sketch of a thing
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # createSketch things_v2
        api_response = api_instance.things_v2_create_sketch(id, thing_sketch, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_create_sketch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **thing_sketch** | [**ThingSketch**](ThingSketch.md)| ThingSketchPayload describes a sketch of a thing | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_delete**
> things_v2_delete(id, force=force, x_organization=x_organization)

delete things_v2

Removes a thing associated to the user

### Example

* OAuth Authentication (oauth2):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
force = False # bool | If true, hard delete the thing (optional) (default to False)
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # delete things_v2
        api_instance.things_v2_delete(id, force=force, x_organization=x_organization)
    except ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **force** | **bool**| If true, hard delete the thing | [optional] [default to False]
 **x_organization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_delete_sketch**
> ArduinoThing things_v2_delete_sketch(id, x_organization=x_organization)

deleteSketch things_v2

### Example

* OAuth Authentication (oauth2):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # deleteSketch things_v2
        api_response = api_instance.things_v2_delete_sketch(id, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_delete_sketch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_list**
> list[ArduinoThing] things_v2_list(across_user_ids=across_user_ids, device_id=device_id, ids=ids, show_deleted=show_deleted, show_properties=show_properties, tags=tags, x_organization=x_organization)

list things_v2

Returns the list of things associated to the user

### Example

* OAuth Authentication (oauth2):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    across_user_ids = False # bool | If true, returns all the things (optional) (default to False)
device_id = 'device_id_example' # str | The id of the device you want to filter (optional)
ids = ['ids_example'] # list[str] | Filter only the desired things (optional)
show_deleted = False # bool | If true, shows the soft deleted things (optional) (default to False)
show_properties = False # bool | If true, returns things with their properties, and last values (optional) (default to False)
tags = ['tags_example'] # list[str] | Filter by tags (optional)
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # list things_v2
        api_response = api_instance.things_v2_list(across_user_ids=across_user_ids, device_id=device_id, ids=ids, show_deleted=show_deleted, show_properties=show_properties, tags=tags, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **across_user_ids** | **bool**| If true, returns all the things | [optional] [default to False]
 **device_id** | **str**| The id of the device you want to filter | [optional] 
 **ids** | [**list[str]**](str.md)| Filter only the desired things | [optional] 
 **show_deleted** | **bool**| If true, shows the soft deleted things | [optional] [default to False]
 **show_properties** | **bool**| If true, returns things with their properties, and last values | [optional] [default to False]
 **tags** | [**list[str]**](str.md)| Filter by tags | [optional] 
 **x_organization** | **str**|  | [optional] 

### Return type

[**list[ArduinoThing]**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_show**
> ArduinoThing things_v2_show(id, show_deleted=show_deleted, x_organization=x_organization)

show things_v2

Returns the thing requested by the user

### Example

* OAuth Authentication (oauth2):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
show_deleted = False # bool | If true, shows the soft deleted thing (optional) (default to False)
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # show things_v2
        api_response = api_instance.things_v2_show(id, show_deleted=show_deleted, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **show_deleted** | **bool**| If true, shows the soft deleted thing | [optional] [default to False]
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_update**
> ArduinoThing things_v2_update(id, thing_update, force=force, x_organization=x_organization)

update things_v2

Updates a thing associated to the user

### Example

* OAuth Authentication (oauth2):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
thing_update = iot_api_client.ThingUpdate() # ThingUpdate | Payload to update an existing thing
force = False # bool | If true, detach device from the other thing, and attach to this thing (optional) (default to False)
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # update things_v2
        api_response = api_instance.things_v2_update(id, thing_update, force=force, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **thing_update** | [**ThingUpdate**](ThingUpdate.md)| Payload to update an existing thing | 
 **force** | **bool**| If true, detach device from the other thing, and attach to this thing | [optional] [default to False]
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
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

* OAuth Authentication (oauth2):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2Api(api_client)
    id = 'id_example' # str | The id of the thing
sketch_id = 'sketch_id_example' # str | The id of the sketch
x_organization = 'x_organization_example' # str |  (optional)
update_sketch = iot_api_client.UpdateSketch() # UpdateSketch |  (optional)

    try:
        # updateSketch things_v2
        api_response = api_instance.things_v2_update_sketch(id, sketch_id, x_organization=x_organization, update_sketch=update_sketch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ThingsV2Api->things_v2_update_sketch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **sketch_id** | **str**| The id of the sketch | 
 **x_organization** | **str**|  | [optional] 
 **update_sketch** | [**UpdateSketch**](UpdateSketch.md)|  | [optional] 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


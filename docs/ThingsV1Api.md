# iot_api_client.ThingsV1Api

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**things_v1_create**](ThingsV1Api.md#things_v1_create) | **PUT** /v1/things | create things_v1
[**things_v1_create_sketch**](ThingsV1Api.md#things_v1_create_sketch) | **PUT** /v1/things/{id}/sketch | createSketch things_v1
[**things_v1_delete**](ThingsV1Api.md#things_v1_delete) | **DELETE** /v1/things/{id} | delete things_v1
[**things_v1_delete_sketch**](ThingsV1Api.md#things_v1_delete_sketch) | **DELETE** /v1/things/{id}/sketch | deleteSketch things_v1
[**things_v1_layout**](ThingsV1Api.md#things_v1_layout) | **GET** /v1/things/{id}/layout | layout things_v1
[**things_v1_list**](ThingsV1Api.md#things_v1_list) | **GET** /v1/things | list things_v1
[**things_v1_show**](ThingsV1Api.md#things_v1_show) | **GET** /v1/things/{id} | show things_v1
[**things_v1_update**](ThingsV1Api.md#things_v1_update) | **POST** /v1/things/{id} | update things_v1
[**things_v1_update_sketch**](ThingsV1Api.md#things_v1_update_sketch) | **PUT** /v1/things/{id}/sketch/{sketchId} | updateSketch things_v1


# **things_v1_create**
> ArduinoThing things_v1_create(create_things_v1_payload, force=force)

create things_v1

Creates a new thing associated to the user

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.ThingsV1Api(iot_api_client.ApiClient(configuration))
create_things_v1_payload = iot_api_client.CreateThingsV1Payload() # CreateThingsV1Payload | ThingPayload describes a thing
force = False # bool | If true, detach device from the other thing, and attach to this thing (optional) (default to False)

try:
    # create things_v1
    api_response = api_instance.things_v1_create(create_things_v1_payload, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingsV1Api->things_v1_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_things_v1_payload** | [**CreateThingsV1Payload**](CreateThingsV1Payload.md)| ThingPayload describes a thing | 
 **force** | **bool**| If true, detach device from the other thing, and attach to this thing | [optional] [default to False]

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
**401** | Unauthorized |  -  |
**409** | Conflict |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v1_create_sketch**
> ArduinoThing things_v1_create_sketch(id, thing_sketch)

createSketch things_v1

Creates a new sketch thing associated to the thing

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.ThingsV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
thing_sketch = iot_api_client.ThingSketch() # ThingSketch | ThingSketchPayload describes a sketch of a thing

try:
    # createSketch things_v1
    api_response = api_instance.things_v1_create_sketch(id, thing_sketch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingsV1Api->things_v1_create_sketch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **thing_sketch** | [**ThingSketch**](ThingSketch.md)| ThingSketchPayload describes a sketch of a thing | 

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
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v1_delete**
> things_v1_delete(id, force=force)

delete things_v1

Removes a thing associated to the user

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.ThingsV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
force = False # bool | If true, hard delete the thing (optional) (default to False)

try:
    # delete things_v1
    api_instance.things_v1_delete(id, force=force)
except ApiException as e:
    print("Exception when calling ThingsV1Api->things_v1_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **force** | **bool**| If true, hard delete the thing | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v1_delete_sketch**
> ArduinoThing things_v1_delete_sketch(id)

deleteSketch things_v1

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.ThingsV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing

try:
    # deleteSketch things_v1
    api_response = api_instance.things_v1_delete_sketch(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingsV1Api->things_v1_delete_sketch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 

### Return type

[**ArduinoThing**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.thing+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v1_layout**
> ArduinoThinglayout things_v1_layout(id, show_deleted=show_deleted)

layout things_v1

Returns the thing requested by the user, without last values data

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.ThingsV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
show_deleted = False # bool | If true, shows the soft deleted thing (optional) (default to False)

try:
    # layout things_v1
    api_response = api_instance.things_v1_layout(id, show_deleted=show_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingsV1Api->things_v1_layout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **show_deleted** | **bool**| If true, shows the soft deleted thing | [optional] [default to False]

### Return type

[**ArduinoThinglayout**](ArduinoThinglayout.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.thinglayout+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v1_list**
> list[ArduinoThing] things_v1_list(across_user_ids=across_user_ids, device_id=device_id, show_deleted=show_deleted)

list things_v1

Returns the list of things associated to the user

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.ThingsV1Api(iot_api_client.ApiClient(configuration))
across_user_ids = False # bool | If true, returns all the things (optional) (default to False)
device_id = 'device_id_example' # str | The id of the device you want to filter (optional)
show_deleted = False # bool | If true, shows the soft deleted things (optional) (default to False)

try:
    # list things_v1
    api_response = api_instance.things_v1_list(across_user_ids=across_user_ids, device_id=device_id, show_deleted=show_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingsV1Api->things_v1_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **across_user_ids** | **bool**| If true, returns all the things | [optional] [default to False]
 **device_id** | **str**| The id of the device you want to filter | [optional] 
 **show_deleted** | **bool**| If true, shows the soft deleted things | [optional] [default to False]

### Return type

[**list[ArduinoThing]**](ArduinoThing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.thing+json; type=collection

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v1_show**
> ArduinoThing things_v1_show(id, show_deleted=show_deleted)

show things_v1

Returns the thing requested by the user

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.ThingsV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
show_deleted = False # bool | If true, shows the soft deleted thing (optional) (default to False)

try:
    # show things_v1
    api_response = api_instance.things_v1_show(id, show_deleted=show_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingsV1Api->things_v1_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **show_deleted** | **bool**| If true, shows the soft deleted thing | [optional] [default to False]

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v1_update**
> ArduinoThing things_v1_update(id, thing, force=force)

update things_v1

Updates a thing associated to the user

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.ThingsV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
thing = iot_api_client.Thing() # Thing | ThingPayload describes a thing
force = False # bool | If true, detach device from the other thing, and attach to this thing (optional) (default to False)

try:
    # update things_v1
    api_response = api_instance.things_v1_update(id, thing, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingsV1Api->things_v1_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **thing** | [**Thing**](Thing.md)| ThingPayload describes a thing | 
 **force** | **bool**| If true, detach device from the other thing, and attach to this thing | [optional] [default to False]

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
**404** | Not Found |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v1_update_sketch**
> ArduinoThing things_v1_update_sketch(id, sketch_id)

updateSketch things_v1

Update an existing thing sketch

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.ThingsV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
sketch_id = 'sketch_id_example' # str | The id of the sketch

try:
    # updateSketch things_v1
    api_response = api_instance.things_v1_update_sketch(id, sketch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThingsV1Api->things_v1_update_sketch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **sketch_id** | **str**| The id of the sketch | 

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
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# iot_api_client.DevicesV2Api

All URIs are relative to *https://api2.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_create**](DevicesV2Api.md#devices_v2_create) | **PUT** /iot/v2/devices | create devices_v2
[**devices_v2_delete**](DevicesV2Api.md#devices_v2_delete) | **DELETE** /iot/v2/devices/{id} | delete devices_v2
[**devices_v2_get_events**](DevicesV2Api.md#devices_v2_get_events) | **GET** /iot/v2/devices/{id}/events | getEvents devices_v2
[**devices_v2_get_properties**](DevicesV2Api.md#devices_v2_get_properties) | **GET** /iot/v2/devices/{id}/properties | getProperties devices_v2
[**devices_v2_get_status_events**](DevicesV2Api.md#devices_v2_get_status_events) | **GET** /iot/v2/devices/{id}/status | GetStatusEvents devices_v2
[**devices_v2_list**](DevicesV2Api.md#devices_v2_list) | **GET** /iot/v2/devices | list devices_v2
[**devices_v2_show**](DevicesV2Api.md#devices_v2_show) | **GET** /iot/v2/devices/{id} | show devices_v2
[**devices_v2_timeseries**](DevicesV2Api.md#devices_v2_timeseries) | **GET** /iot/v2/devices/{id}/properties/{pid} | timeseries devices_v2
[**devices_v2_update**](DevicesV2Api.md#devices_v2_update) | **POST** /iot/v2/devices/{id} | update devices_v2
[**devices_v2_update_properties**](DevicesV2Api.md#devices_v2_update_properties) | **PUT** /iot/v2/devices/{id}/properties | updateProperties devices_v2


# **devices_v2_create**
> ArduinoDevicev2 devices_v2_create(create_devices_v2_payload, x_organization=x_organization)

create devices_v2

Creates a new device associated to the user.

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_devicev2 import ArduinoDevicev2
from iot_api_client.models.create_devices_v2_payload import CreateDevicesV2Payload
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2Api(api_client)
    create_devices_v2_payload = iot_api_client.CreateDevicesV2Payload() # CreateDevicesV2Payload | DeviceV2 describes a device.
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # create devices_v2
        api_response = api_instance.devices_v2_create(create_devices_v2_payload, x_organization=x_organization)
        print("The response of DevicesV2Api->devices_v2_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2Api->devices_v2_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_devices_v2_payload** | [**CreateDevicesV2Payload**](CreateDevicesV2Payload.md)| DeviceV2 describes a device. | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDevicev2**](ArduinoDevicev2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.devicev2+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_delete**
> devices_v2_delete(id, force=force, x_organization=x_organization)

delete devices_v2

Removes a device associated to the user

### Example

* OAuth Authentication (oauth2):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
    force = False # bool | If true, hard delete the device (optional) (default to False)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # delete devices_v2
        api_instance.devices_v2_delete(id, force=force, x_organization=x_organization)
    except Exception as e:
        print("Exception when calling DevicesV2Api->devices_v2_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **force** | **bool**| If true, hard delete the device | [optional] [default to False]
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_get_events**
> ArduinoDevicev2EventProperties devices_v2_get_events(id, limit=limit, start=start, x_organization=x_organization)

getEvents devices_v2

GET device events

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_devicev2_event_properties import ArduinoDevicev2EventProperties
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
    limit = 56 # int | The number of events to select (optional)
    start = 'start_example' # str | The time at which to start selecting events (optional)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # getEvents devices_v2
        api_response = api_instance.devices_v2_get_events(id, limit=limit, start=start, x_organization=x_organization)
        print("The response of DevicesV2Api->devices_v2_get_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2Api->devices_v2_get_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **limit** | **int**| The number of events to select | [optional] 
 **start** | **str**| The time at which to start selecting events | [optional] 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDevicev2EventProperties**](ArduinoDevicev2EventProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2.event.properties+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_get_properties**
> ArduinoDevicev2properties devices_v2_get_properties(id, show_deleted=show_deleted, x_organization=x_organization)

getProperties devices_v2

GET device properties

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_devicev2properties import ArduinoDevicev2properties
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
    show_deleted = False # bool | If true, shows the soft deleted properties (optional) (default to False)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # getProperties devices_v2
        api_response = api_instance.devices_v2_get_properties(id, show_deleted=show_deleted, x_organization=x_organization)
        print("The response of DevicesV2Api->devices_v2_get_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2Api->devices_v2_get_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **show_deleted** | **bool**| If true, shows the soft deleted properties | [optional] [default to False]
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDevicev2properties**](ArduinoDevicev2properties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2properties+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_get_status_events**
> ArduinoDevicev2StatusEvents devices_v2_get_status_events(id, limit=limit, start=start, x_organization=x_organization)

GetStatusEvents devices_v2

GET connection status events

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_devicev2_status_events import ArduinoDevicev2StatusEvents
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
    limit = 30 # int | The number of events to select (optional) (default to 30)
    start = 'start_example' # str | The time at which to start selecting events (optional)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # GetStatusEvents devices_v2
        api_response = api_instance.devices_v2_get_status_events(id, limit=limit, start=start, x_organization=x_organization)
        print("The response of DevicesV2Api->devices_v2_get_status_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2Api->devices_v2_get_status_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **limit** | **int**| The number of events to select | [optional] [default to 30]
 **start** | **str**| The time at which to start selecting events | [optional] 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDevicev2StatusEvents**](ArduinoDevicev2StatusEvents.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2.status.events+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_list**
> List[ArduinoDevicev2] devices_v2_list(across_user_ids=across_user_ids, serial=serial, show_deleted=show_deleted, tags=tags, x_organization=x_organization)

list devices_v2

Returns the list of devices associated to the user

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_devicev2 import ArduinoDevicev2
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2Api(api_client)
    across_user_ids = False # bool | If true, returns all the devices (optional) (default to False)
    serial = 'serial_example' # str | Filter by device serial number (optional)
    show_deleted = False # bool | If true, shows the soft deleted devices (optional) (default to False)
    tags = ['tags_example'] # List[str] | Filter by tags (optional)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # list devices_v2
        api_response = api_instance.devices_v2_list(across_user_ids=across_user_ids, serial=serial, show_deleted=show_deleted, tags=tags, x_organization=x_organization)
        print("The response of DevicesV2Api->devices_v2_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2Api->devices_v2_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **across_user_ids** | **bool**| If true, returns all the devices | [optional] [default to False]
 **serial** | **str**| Filter by device serial number | [optional] 
 **show_deleted** | **bool**| If true, shows the soft deleted devices | [optional] [default to False]
 **tags** | [**List[str]**](str.md)| Filter by tags | [optional] 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**List[ArduinoDevicev2]**](ArduinoDevicev2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2+json; type=collection, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_show**
> ArduinoDevicev2 devices_v2_show(id, x_organization=x_organization)

show devices_v2

Returns the device requested by the user

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_devicev2 import ArduinoDevicev2
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # show devices_v2
        api_response = api_instance.devices_v2_show(id, x_organization=x_organization)
        print("The response of DevicesV2Api->devices_v2_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2Api->devices_v2_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDevicev2**](ArduinoDevicev2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_timeseries**
> ArduinoDevicev2propertyvalues devices_v2_timeseries(id, pid, limit=limit, start=start, x_organization=x_organization)

timeseries devices_v2

GET device properties values in a range of time

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_devicev2propertyvalues import ArduinoDevicev2propertyvalues
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
    pid = 'pid_example' # str | The id of the property
    limit = 56 # int | The number of properties to select (optional)
    start = 'start_example' # str | The time at which to start selecting properties (optional)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # timeseries devices_v2
        api_response = api_instance.devices_v2_timeseries(id, pid, limit=limit, start=start, x_organization=x_organization)
        print("The response of DevicesV2Api->devices_v2_timeseries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2Api->devices_v2_timeseries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **pid** | **str**| The id of the property | 
 **limit** | **int**| The number of properties to select | [optional] 
 **start** | **str**| The time at which to start selecting properties | [optional] 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDevicev2propertyvalues**](ArduinoDevicev2propertyvalues.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2propertyvalues+json, application/vnd.goa.error+json

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

# **devices_v2_update**
> ArduinoDevicev2 devices_v2_update(id, devicev2, x_organization=x_organization)

update devices_v2

Updates a device associated to the user

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_devicev2 import ArduinoDevicev2
from iot_api_client.models.devicev2 import Devicev2
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
    devicev2 = iot_api_client.Devicev2() # Devicev2 | DeviceV2 describes a device.
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # update devices_v2
        api_response = api_instance.devices_v2_update(id, devicev2, x_organization=x_organization)
        print("The response of DevicesV2Api->devices_v2_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2Api->devices_v2_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **devicev2** | [**Devicev2**](Devicev2.md)| DeviceV2 describes a device. | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDevicev2**](ArduinoDevicev2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.devicev2+json, application/vnd.goa.error+json

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

# **devices_v2_update_properties**
> devices_v2_update_properties(id, properties_values, x_organization=x_organization)

updateProperties devices_v2

Update device properties last values

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.properties_values import PropertiesValues
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
    properties_values = iot_api_client.PropertiesValues() # PropertiesValues | 
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # updateProperties devices_v2
        api_instance.devices_v2_update_properties(id, properties_values, x_organization=x_organization)
    except Exception as e:
        print("Exception when calling DevicesV2Api->devices_v2_update_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **properties_values** | [**PropertiesValues**](PropertiesValues.md)|  | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.goa.error+json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


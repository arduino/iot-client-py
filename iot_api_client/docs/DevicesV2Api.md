# iot_api_client.DevicesV2Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_create**](DevicesV2Api.md#devices_v2_create) | **PUT** /v2/devices | create devices_v2
[**devices_v2_delete**](DevicesV2Api.md#devices_v2_delete) | **DELETE** /v2/devices/{id} | delete devices_v2
[**devices_v2_get_events**](DevicesV2Api.md#devices_v2_get_events) | **GET** /v2/devices/{id}/events | getEvents devices_v2
[**devices_v2_get_properties**](DevicesV2Api.md#devices_v2_get_properties) | **GET** /v2/devices/{id}/properties | getProperties devices_v2
[**devices_v2_list**](DevicesV2Api.md#devices_v2_list) | **GET** /v2/devices | list devices_v2
[**devices_v2_show**](DevicesV2Api.md#devices_v2_show) | **GET** /v2/devices/{id} | show devices_v2
[**devices_v2_timeseries**](DevicesV2Api.md#devices_v2_timeseries) | **GET** /v2/devices/{id}/properties/{pid} | timeseries devices_v2
[**devices_v2_update**](DevicesV2Api.md#devices_v2_update) | **POST** /v2/devices/{id} | update devices_v2
[**devices_v2_update_properties**](DevicesV2Api.md#devices_v2_update_properties) | **PUT** /v2/devices/{id}/properties | updateProperties devices_v2


# **devices_v2_create**
> ArduinoDevicev2 devices_v2_create(create_devices_v2_payload, x_organization=x_organization)

create devices_v2

Creates a new device associated to the user.

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
    api_instance = iot_api_client.DevicesV2Api(api_client)
    create_devices_v2_payload = iot_api_client.CreateDevicesV2Payload() # CreateDevicesV2Payload | DeviceV2 describes a device.
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # create devices_v2
        api_response = api_instance.devices_v2_create(create_devices_v2_payload, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_devices_v2_payload** | [**CreateDevicesV2Payload**](CreateDevicesV2Payload.md)| DeviceV2 describes a device. | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDevicev2**](ArduinoDevicev2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_delete**
> devices_v2_delete(id, x_organization=x_organization)

delete devices_v2

Removes a device associated to the user

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
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # delete devices_v2
        api_instance.devices_v2_delete(id, x_organization=x_organization)
    except ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
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
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_get_events**
> ArduinoDevicev2EventProperties devices_v2_get_events(id, limit=limit, start=start, x_organization=x_organization)

getEvents devices_v2

GET device events

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
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
limit = 56 # int | The number of events to select (optional)
start = 'start_example' # str | The time at which to start selecting events (optional)
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # getEvents devices_v2
        api_response = api_instance.devices_v2_get_events(id, limit=limit, start=start, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **limit** | **int**| The number of events to select | [optional] 
 **start** | **str**| The time at which to start selecting events | [optional] 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDevicev2EventProperties**](ArduinoDevicev2EventProperties.md)

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
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
show_deleted = False # bool | If true, shows the soft deleted properties (optional) (default to False)
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # getProperties devices_v2
        api_response = api_instance.devices_v2_get_properties(id, show_deleted=show_deleted, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_get_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **show_deleted** | **bool**| If true, shows the soft deleted properties | [optional] [default to False]
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDevicev2properties**](ArduinoDevicev2properties.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_list**
> list[ArduinoDevicev2] devices_v2_list(across_user_ids=across_user_ids, serial=serial, tags=tags, x_organization=x_organization)

list devices_v2

Returns the list of devices associated to the user

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
    api_instance = iot_api_client.DevicesV2Api(api_client)
    across_user_ids = False # bool | If true, returns all the devices (optional) (default to False)
serial = 'serial_example' # str | Filter by device serial number (optional)
tags = ['tags_example'] # list[str] | Filter by tags (optional)
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # list devices_v2
        api_response = api_instance.devices_v2_list(across_user_ids=across_user_ids, serial=serial, tags=tags, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **across_user_ids** | **bool**| If true, returns all the devices | [optional] [default to False]
 **serial** | **str**| Filter by device serial number | [optional] 
 **tags** | [**list[str]**](str.md)| Filter by tags | [optional] 
 **x_organization** | **str**|  | [optional] 

### Return type

[**list[ArduinoDevicev2]**](ArduinoDevicev2.md)

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

# **devices_v2_show**
> ArduinoDevicev2 devices_v2_show(id, x_organization=x_organization)

show devices_v2

Returns the device requested by the user

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
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # show devices_v2
        api_response = api_instance.devices_v2_show(id, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDevicev2**](ArduinoDevicev2.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_timeseries**
> ArduinoDevicev2propertyvalues devices_v2_timeseries(id, pid, limit=limit, start=start, x_organization=x_organization)

timeseries devices_v2

GET device properties values in a range of time

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
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
pid = 'pid_example' # str | The id of the property
limit = 56 # int | The number of properties to select (optional)
start = 'start_example' # str | The time at which to start selecting properties (optional)
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # timeseries devices_v2
        api_response = api_instance.devices_v2_timeseries(id, pid, limit=limit, start=start, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_timeseries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **pid** | **str**| The id of the property | 
 **limit** | **int**| The number of properties to select | [optional] 
 **start** | **str**| The time at which to start selecting properties | [optional] 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDevicev2propertyvalues**](ArduinoDevicev2propertyvalues.md)

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

# **devices_v2_update**
> ArduinoDevicev2 devices_v2_update(id, devicev2, x_organization=x_organization)

update devices_v2

Updates a device associated to the user

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
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
devicev2 = iot_api_client.Devicev2() # Devicev2 | DeviceV2 describes a device.
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # update devices_v2
        api_response = api_instance.devices_v2_update(id, devicev2, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **devicev2** | [**Devicev2**](Devicev2.md)| DeviceV2 describes a device. | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDevicev2**](ArduinoDevicev2.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_update_properties**
> devices_v2_update_properties(id, properties_values, x_organization=x_organization)

updateProperties devices_v2

Update device properties last values

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
    api_instance = iot_api_client.DevicesV2Api(api_client)
    id = 'id_example' # str | The id of the device
properties_values = iot_api_client.PropertiesValues() # PropertiesValues | 
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # updateProperties devices_v2
        api_instance.devices_v2_update_properties(id, properties_values, x_organization=x_organization)
    except ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_update_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **properties_values** | [**PropertiesValues**](PropertiesValues.md)|  | 
 **x_organization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


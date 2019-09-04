# iot_api_client.DevicesV2Api

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_create**](DevicesV2Api.md#devices_v2_create) | **PUT** /v2/devices | create devices_v2
[**devices_v2_delete**](DevicesV2Api.md#devices_v2_delete) | **DELETE** /v2/devices/{id} | delete devices_v2
[**devices_v2_get_properties**](DevicesV2Api.md#devices_v2_get_properties) | **GET** /v2/devices/{id}/properties | getProperties devices_v2
[**devices_v2_list**](DevicesV2Api.md#devices_v2_list) | **GET** /v2/devices | list devices_v2
[**devices_v2_show**](DevicesV2Api.md#devices_v2_show) | **GET** /v2/devices/{id} | show devices_v2
[**devices_v2_timeseries**](DevicesV2Api.md#devices_v2_timeseries) | **GET** /v2/devices/{id}/properties/{pid} | timeseries devices_v2
[**devices_v2_update**](DevicesV2Api.md#devices_v2_update) | **POST** /v2/devices/{id} | update devices_v2
[**devices_v2_update_properties**](DevicesV2Api.md#devices_v2_update_properties) | **PUT** /v2/devices/{id}/properties | updateProperties devices_v2


# **devices_v2_create**
> ArduinoDevicev2 devices_v2_create(create_devices_v2_payload)

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
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2Api(iot_api_client.ApiClient(configuration))
create_devices_v2_payload = iot_api_client.CreateDevicesV2Payload() # CreateDevicesV2Payload | DeviceV2 describes a device.

try:
    # create devices_v2
    api_response = api_instance.devices_v2_create(create_devices_v2_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_devices_v2_payload** | [**CreateDevicesV2Payload**](CreateDevicesV2Payload.md)| DeviceV2 describes a device. | 

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
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_delete**
> devices_v2_delete(id)

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
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device

try:
    # delete devices_v2
    api_instance.devices_v2_delete(id)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_get_properties**
> ArduinoDevicev2properties devices_v2_get_properties(id, show_deleted=show_deleted)

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
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
show_deleted = False # bool | If true, shows the soft deleted properties (optional) (default to False)

try:
    # getProperties devices_v2
    api_response = api_instance.devices_v2_get_properties(id, show_deleted=show_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_get_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **show_deleted** | **bool**| If true, shows the soft deleted properties | [optional] [default to False]

### Return type

[**ArduinoDevicev2properties**](ArduinoDevicev2properties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2properties+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_list**
> list[ArduinoDevicev2] devices_v2_list(across_user_ids=across_user_ids)

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
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2Api(iot_api_client.ApiClient(configuration))
across_user_ids = False # bool | If true, returns all the devices (optional) (default to False)

try:
    # list devices_v2
    api_response = api_instance.devices_v2_list(across_user_ids=across_user_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **across_user_ids** | **bool**| If true, returns all the devices | [optional] [default to False]

### Return type

[**list[ArduinoDevicev2]**](ArduinoDevicev2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2+json; type=collection

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_show**
> ArduinoDevicev2 devices_v2_show(id)

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
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device

try:
    # show devices_v2
    api_response = api_instance.devices_v2_show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 

### Return type

[**ArduinoDevicev2**](ArduinoDevicev2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_timeseries**
> ArduinoDevicev2propertyvalues devices_v2_timeseries(id, pid, limit=limit, start=start)

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
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
pid = 'pid_example' # str | The id of the property
limit = 56 # int | The number of properties to select (optional)
start = 'start_example' # str | The time at which to start selecting properties (optional)

try:
    # timeseries devices_v2
    api_response = api_instance.devices_v2_timeseries(id, pid, limit=limit, start=start)
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

### Return type

[**ArduinoDevicev2propertyvalues**](ArduinoDevicev2propertyvalues.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2propertyvalues+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_update**
> ArduinoDevicev2 devices_v2_update(id, devicev2)

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
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
devicev2 = iot_api_client.Devicev2() # Devicev2 | DeviceV2 describes a device.

try:
    # update devices_v2
    api_response = api_instance.devices_v2_update(id, devicev2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **devicev2** | [**Devicev2**](Devicev2.md)| DeviceV2 describes a device. | 

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
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_update_properties**
> devices_v2_update_properties(id, properties_values)

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
configuration = iot_api_client.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api-dev.arduino.cc
configuration.host = "http://api-dev.arduino.cc"
# Create an instance of the API class
api_instance = iot_api_client.DevicesV2Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
properties_values = iot_api_client.PropertiesValues() # PropertiesValues | 

try:
    # updateProperties devices_v2
    api_instance.devices_v2_update_properties(id, properties_values)
except ApiException as e:
    print("Exception when calling DevicesV2Api->devices_v2_update_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **properties_values** | [**PropertiesValues**](PropertiesValues.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


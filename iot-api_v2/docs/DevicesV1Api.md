# iot_api_client.DevicesV1Api

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v1_connect**](DevicesV1Api.md#devices_v1_connect) | **POST** /iot/v1/devices/connect | connect devices_v1
[**devices_v1_create**](DevicesV1Api.md#devices_v1_create) | **PUT** /iot/v1/devices | create devices_v1
[**devices_v1_delete**](DevicesV1Api.md#devices_v1_delete) | **DELETE** /iot/v1/devices/{id} | delete devices_v1
[**devices_v1_image**](DevicesV1Api.md#devices_v1_image) | **POST** /iot/v1/devices/{id}/image | image devices_v1
[**devices_v1_list**](DevicesV1Api.md#devices_v1_list) | **GET** /iot/v1/devices | list devices_v1
[**devices_v1_show**](DevicesV1Api.md#devices_v1_show) | **GET** /iot/v1/devices/{id} | show devices_v1
[**devices_v1_update**](DevicesV1Api.md#devices_v1_update) | **POST** /iot/v1/devices/{id} | update devices_v1


# **devices_v1_connect**
> ArduinoMqttv1 devices_v1_connect()

connect devices_v1

Returns a signed websocket url to use for a connection

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
api_instance = iot_api_client.DevicesV1Api(iot_api_client.ApiClient(configuration))

try:
    # connect devices_v1
    api_response = api_instance.devices_v1_connect()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV1Api->devices_v1_connect: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArduinoMqttv1**](ArduinoMqttv1.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.mqttv1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v1_create**
> ArduinoDevicev1 devices_v1_create(arduino_devicev1)

create devices_v1

Creates a new device associated to the user. By default it creates a device with no name and no certificates attached. If you provide a name or a certificate request it will set them up.

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
api_instance = iot_api_client.DevicesV1Api(iot_api_client.ApiClient(configuration))
arduino_devicev1 = iot_api_client.ArduinoDevicev1() # ArduinoDevicev1 | DevicePayload describes a device. No field is mandatory

try:
    # create devices_v1
    api_response = api_instance.devices_v1_create(arduino_devicev1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV1Api->devices_v1_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arduino_devicev1** | [**ArduinoDevicev1**](ArduinoDevicev1.md)| DevicePayload describes a device. No field is mandatory | 

### Return type

[**ArduinoDevicev1**](ArduinoDevicev1.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.devicev1+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v1_delete**
> devices_v1_delete(id)

delete devices_v1

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
api_instance = iot_api_client.DevicesV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the resource

try:
    # delete devices_v1
    api_instance.devices_v1_delete(id)
except ApiException as e:
    print("Exception when calling DevicesV1Api->devices_v1_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the resource | 

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

# **devices_v1_image**
> devices_v1_image(id, configv1)

image devices_v1

Returns an iso image to be burned into a usb key

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
api_instance = iot_api_client.DevicesV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the resource
configv1 = [iot_api_client.Configv1()] # list[Configv1] | 

try:
    # image devices_v1
    api_instance.devices_v1_image(id, configv1)
except ApiException as e:
    print("Exception when calling DevicesV1Api->devices_v1_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the resource | 
 **configv1** | [**list[Configv1]**](Configv1.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v1_list**
> list[ArduinoDevicev1] devices_v1_list()

list devices_v1

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
api_instance = iot_api_client.DevicesV1Api(iot_api_client.ApiClient(configuration))

try:
    # list devices_v1
    api_response = api_instance.devices_v1_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV1Api->devices_v1_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ArduinoDevicev1]**](ArduinoDevicev1.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev1+json; type=collection

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v1_show**
> ArduinoDevicev1 devices_v1_show(id)

show devices_v1

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
api_instance = iot_api_client.DevicesV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the resource

try:
    # show devices_v1
    api_response = api_instance.devices_v1_show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV1Api->devices_v1_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the resource | 

### Return type

[**ArduinoDevicev1**](ArduinoDevicev1.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v1_update**
> ArduinoDevicev1 devices_v1_update(id, arduino_devicev1)

update devices_v1

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
api_instance = iot_api_client.DevicesV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the resource
arduino_devicev1 = iot_api_client.ArduinoDevicev1() # ArduinoDevicev1 | DevicePayload describes a device. No field is mandatory

try:
    # update devices_v1
    api_response = api_instance.devices_v1_update(id, arduino_devicev1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV1Api->devices_v1_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the resource | 
 **arduino_devicev1** | [**ArduinoDevicev1**](ArduinoDevicev1.md)| DevicePayload describes a device. No field is mandatory | 

### Return type

[**ArduinoDevicev1**](ArduinoDevicev1.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.devicev1+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


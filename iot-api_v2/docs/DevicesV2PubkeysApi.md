# iot_api_client.DevicesV2PubkeysApi

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_pubkeys_create**](DevicesV2PubkeysApi.md#devices_v2_pubkeys_create) | **PUT** /iot/v2/devices/{id}/pubkeys | create devices_v2_pubkeys
[**devices_v2_pubkeys_delete**](DevicesV2PubkeysApi.md#devices_v2_pubkeys_delete) | **DELETE** /iot/v2/devices/{id}/pubkeys/{pid} | delete devices_v2_pubkeys
[**devices_v2_pubkeys_list**](DevicesV2PubkeysApi.md#devices_v2_pubkeys_list) | **GET** /iot/v2/devices/{id}/pubkeys | list devices_v2_pubkeys
[**devices_v2_pubkeys_show**](DevicesV2PubkeysApi.md#devices_v2_pubkeys_show) | **GET** /iot/v2/devices/{id}/pubkeys/{pid} | show devices_v2_pubkeys
[**devices_v2_pubkeys_update**](DevicesV2PubkeysApi.md#devices_v2_pubkeys_update) | **POST** /iot/v2/devices/{id}/pubkeys/{pid} | update devices_v2_pubkeys


# **devices_v2_pubkeys_create**
> ArduinoDevicev2Pubkey devices_v2_pubkeys_create(id, create_devices_v2_pubkeys_payload)

create devices_v2_pubkeys

Creates a new pubkey associated to a device

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
api_instance = iot_api_client.DevicesV2PubkeysApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
create_devices_v2_pubkeys_payload = iot_api_client.CreateDevicesV2PubkeysPayload() # CreateDevicesV2PubkeysPayload | 

try:
    # create devices_v2_pubkeys
    api_response = api_instance.devices_v2_pubkeys_create(id, create_devices_v2_pubkeys_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2PubkeysApi->devices_v2_pubkeys_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **create_devices_v2_pubkeys_payload** | [**CreateDevicesV2PubkeysPayload**](CreateDevicesV2PubkeysPayload.md)|  | 

### Return type

[**ArduinoDevicev2Pubkey**](ArduinoDevicev2Pubkey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.devicev2.pubkey+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_pubkeys_delete**
> devices_v2_pubkeys_delete(id, pid)

delete devices_v2_pubkeys

Removes a pubkey associated to a device

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
api_instance = iot_api_client.DevicesV2PubkeysApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
pid = 'pid_example' # str | The id of the pubkey

try:
    # delete devices_v2_pubkeys
    api_instance.devices_v2_pubkeys_delete(id, pid)
except ApiException as e:
    print("Exception when calling DevicesV2PubkeysApi->devices_v2_pubkeys_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **pid** | **str**| The id of the pubkey | 

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

# **devices_v2_pubkeys_list**
> list[ArduinoDevicev2Pubkey] devices_v2_pubkeys_list(id)

list devices_v2_pubkeys

Returns the list of pubkeys associated to the device

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
api_instance = iot_api_client.DevicesV2PubkeysApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device

try:
    # list devices_v2_pubkeys
    api_response = api_instance.devices_v2_pubkeys_list(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2PubkeysApi->devices_v2_pubkeys_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 

### Return type

[**list[ArduinoDevicev2Pubkey]**](ArduinoDevicev2Pubkey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2.pubkey+json; type=collection

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_pubkeys_show**
> ArduinoDevicev2Pubkey devices_v2_pubkeys_show(id, pid)

show devices_v2_pubkeys

Returns the pubkey requested by the user

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
api_instance = iot_api_client.DevicesV2PubkeysApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
pid = 'pid_example' # str | The id of the pubkey

try:
    # show devices_v2_pubkeys
    api_response = api_instance.devices_v2_pubkeys_show(id, pid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2PubkeysApi->devices_v2_pubkeys_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **pid** | **str**| The id of the pubkey | 

### Return type

[**ArduinoDevicev2Pubkey**](ArduinoDevicev2Pubkey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2.pubkey+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_pubkeys_update**
> ArduinoDevicev2Pubkey devices_v2_pubkeys_update(id, pid, devicev2_pubkey)

update devices_v2_pubkeys

Updates a pubkey associated to a device

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
api_instance = iot_api_client.DevicesV2PubkeysApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
pid = 'pid_example' # str | The id of the pubkey
devicev2_pubkey = iot_api_client.Devicev2Pubkey() # Devicev2Pubkey | 

try:
    # update devices_v2_pubkeys
    api_response = api_instance.devices_v2_pubkeys_update(id, pid, devicev2_pubkey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2PubkeysApi->devices_v2_pubkeys_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **pid** | **str**| The id of the pubkey | 
 **devicev2_pubkey** | [**Devicev2Pubkey**](Devicev2Pubkey.md)|  | 

### Return type

[**ArduinoDevicev2Pubkey**](ArduinoDevicev2Pubkey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.devicev2.pubkey+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


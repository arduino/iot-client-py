# iot_api_client.DevicesV2CertsApi

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_certs_create**](DevicesV2CertsApi.md#devices_v2_certs_create) | **PUT** /iot/v2/devices/{id}/certs | create devices_v2_certs
[**devices_v2_certs_delete**](DevicesV2CertsApi.md#devices_v2_certs_delete) | **DELETE** /iot/v2/devices/{id}/certs/{cid} | delete devices_v2_certs
[**devices_v2_certs_list**](DevicesV2CertsApi.md#devices_v2_certs_list) | **GET** /iot/v2/devices/{id}/certs | list devices_v2_certs
[**devices_v2_certs_show**](DevicesV2CertsApi.md#devices_v2_certs_show) | **GET** /iot/v2/devices/{id}/certs/{cid} | show devices_v2_certs
[**devices_v2_certs_update**](DevicesV2CertsApi.md#devices_v2_certs_update) | **POST** /iot/v2/devices/{id}/certs/{cid} | update devices_v2_certs


# **devices_v2_certs_create**
> ArduinoDevicev2Cert devices_v2_certs_create(id, create_devices_v2_certs_payload)

create devices_v2_certs

Creates a new cert associated to a device. The csr is signed and saved in database. The CommonName will be replaced with the device id.

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
api_instance = iot_api_client.DevicesV2CertsApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device
create_devices_v2_certs_payload = iot_api_client.CreateDevicesV2CertsPayload() # CreateDevicesV2CertsPayload | 

try:
    # create devices_v2_certs
    api_response = api_instance.devices_v2_certs_create(id, create_devices_v2_certs_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2CertsApi->devices_v2_certs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **create_devices_v2_certs_payload** | [**CreateDevicesV2CertsPayload**](CreateDevicesV2CertsPayload.md)|  | 

### Return type

[**ArduinoDevicev2Cert**](ArduinoDevicev2Cert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.devicev2.cert+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_certs_delete**
> devices_v2_certs_delete(cid, id)

delete devices_v2_certs

Removes a cert associated to a device

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
api_instance = iot_api_client.DevicesV2CertsApi(iot_api_client.ApiClient(configuration))
cid = 'cid_example' # str | The id of the cert
id = 'id_example' # str | The id of the device

try:
    # delete devices_v2_certs
    api_instance.devices_v2_certs_delete(cid, id)
except ApiException as e:
    print("Exception when calling DevicesV2CertsApi->devices_v2_certs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| The id of the cert | 
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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_certs_list**
> list[ArduinoDevicev2Cert] devices_v2_certs_list(id)

list devices_v2_certs

Returns the list of certs associated to the device

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
api_instance = iot_api_client.DevicesV2CertsApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the device

try:
    # list devices_v2_certs
    api_response = api_instance.devices_v2_certs_list(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2CertsApi->devices_v2_certs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 

### Return type

[**list[ArduinoDevicev2Cert]**](ArduinoDevicev2Cert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2.cert+json; type=collection

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_certs_show**
> ArduinoDevicev2Cert devices_v2_certs_show(cid, id)

show devices_v2_certs

Returns the cert requested by the user

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
api_instance = iot_api_client.DevicesV2CertsApi(iot_api_client.ApiClient(configuration))
cid = 'cid_example' # str | The id of the cert
id = 'id_example' # str | The id of the device

try:
    # show devices_v2_certs
    api_response = api_instance.devices_v2_certs_show(cid, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2CertsApi->devices_v2_certs_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| The id of the cert | 
 **id** | **str**| The id of the device | 

### Return type

[**ArduinoDevicev2Cert**](ArduinoDevicev2Cert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2.cert+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_certs_update**
> ArduinoDevicev2Cert devices_v2_certs_update(cid, id, devicev2_cert)

update devices_v2_certs

Updates a cert associated to a device. The csr is signed and saved in database. The CommonName will be replaced with the device id.

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
api_instance = iot_api_client.DevicesV2CertsApi(iot_api_client.ApiClient(configuration))
cid = 'cid_example' # str | The id of the cert
id = 'id_example' # str | The id of the device
devicev2_cert = iot_api_client.Devicev2Cert() # Devicev2Cert | 

try:
    # update devices_v2_certs
    api_response = api_instance.devices_v2_certs_update(cid, id, devicev2_cert)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesV2CertsApi->devices_v2_certs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**| The id of the cert | 
 **id** | **str**| The id of the device | 
 **devicev2_cert** | [**Devicev2Cert**](Devicev2Cert.md)|  | 

### Return type

[**ArduinoDevicev2Cert**](ArduinoDevicev2Cert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.devicev2.cert+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


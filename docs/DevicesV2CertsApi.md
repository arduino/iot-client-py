# iot_api_client.DevicesV2CertsApi

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_certs_create**](DevicesV2CertsApi.md#devices_v2_certs_create) | **PUT** /v2/devices/{id}/certs | create devices_v2_certs
[**devices_v2_certs_delete**](DevicesV2CertsApi.md#devices_v2_certs_delete) | **DELETE** /v2/devices/{id}/certs/{cid} | delete devices_v2_certs
[**devices_v2_certs_list**](DevicesV2CertsApi.md#devices_v2_certs_list) | **GET** /v2/devices/{id}/certs | list devices_v2_certs
[**devices_v2_certs_show**](DevicesV2CertsApi.md#devices_v2_certs_show) | **GET** /v2/devices/{id}/certs/{cid} | show devices_v2_certs
[**devices_v2_certs_update**](DevicesV2CertsApi.md#devices_v2_certs_update) | **POST** /v2/devices/{id}/certs/{cid} | update devices_v2_certs


# **devices_v2_certs_create**
> ArduinoDevicev2Cert devices_v2_certs_create(id, create_devices_v2_certs_payload)

create devices_v2_certs

Creates a new cert associated to a device. The csr is signed and saved in database. The CommonName will be replaced with the device id.

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import iot_api_client
from iot_api_client.models.arduino_devicev2_cert import ArduinoDevicev2Cert
from iot_api_client.models.create_devices_v2_certs_payload import CreateDevicesV2CertsPayload
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2CertsApi(api_client)
    id = 'id_example' # str | The id of the device
    create_devices_v2_certs_payload = iot_api_client.CreateDevicesV2CertsPayload() # CreateDevicesV2CertsPayload | 

    try:
        # create devices_v2_certs
        api_response = api_instance.devices_v2_certs_create(id, create_devices_v2_certs_payload)
        print("The response of DevicesV2CertsApi->devices_v2_certs_create:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.arduino.devicev2.cert+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_certs_delete**
> devices_v2_certs_delete(cid, id)

delete devices_v2_certs

Removes a cert associated to a device

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2CertsApi(api_client)
    cid = 'cid_example' # str | The id of the cert
    id = 'id_example' # str | The id of the device

    try:
        # delete devices_v2_certs
        api_instance.devices_v2_certs_delete(cid, id)
    except Exception as e:
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
 - **Accept**: application/vnd.goa.error+json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_certs_list**
> List[ArduinoDevicev2Cert] devices_v2_certs_list(id)

list devices_v2_certs

Returns the list of certs associated to the device

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import iot_api_client
from iot_api_client.models.arduino_devicev2_cert import ArduinoDevicev2Cert
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2CertsApi(api_client)
    id = 'id_example' # str | The id of the device

    try:
        # list devices_v2_certs
        api_response = api_instance.devices_v2_certs_list(id)
        print("The response of DevicesV2CertsApi->devices_v2_certs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2CertsApi->devices_v2_certs_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 

### Return type

[**List[ArduinoDevicev2Cert]**](ArduinoDevicev2Cert.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.devicev2.cert+json; type=collection, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_certs_show**
> ArduinoDevicev2Cert devices_v2_certs_show(cid, id)

show devices_v2_certs

Returns the cert requested by the user

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import iot_api_client
from iot_api_client.models.arduino_devicev2_cert import ArduinoDevicev2Cert
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2CertsApi(api_client)
    cid = 'cid_example' # str | The id of the cert
    id = 'id_example' # str | The id of the device

    try:
        # show devices_v2_certs
        api_response = api_instance.devices_v2_certs_show(cid, id)
        print("The response of DevicesV2CertsApi->devices_v2_certs_show:\n")
        pprint(api_response)
    except Exception as e:
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
 - **Accept**: application/vnd.arduino.devicev2.cert+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_certs_update**
> ArduinoDevicev2Cert devices_v2_certs_update(cid, id, devicev2_cert)

update devices_v2_certs

Updates a cert associated to a device. The csr is signed and saved in database. The CommonName will be replaced with the device id.

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import iot_api_client
from iot_api_client.models.arduino_devicev2_cert import ArduinoDevicev2Cert
from iot_api_client.models.devicev2_cert import Devicev2Cert
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DevicesV2CertsApi(api_client)
    cid = 'cid_example' # str | The id of the cert
    id = 'id_example' # str | The id of the device
    devicev2_cert = iot_api_client.Devicev2Cert() # Devicev2Cert | 

    try:
        # update devices_v2_certs
        api_response = api_instance.devices_v2_certs_update(cid, id, devicev2_cert)
        print("The response of DevicesV2CertsApi->devices_v2_certs_update:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.arduino.devicev2.cert+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# iot_api_client.ClientsV1Api

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clients_v1_create**](ClientsV1Api.md#clients_v1_create) | **PUT** /iot/v1/clients | create clients_v1
[**clients_v1_delete**](ClientsV1Api.md#clients_v1_delete) | **DELETE** /iot/v1/clients/{id} | delete clients_v1
[**clients_v1_list**](ClientsV1Api.md#clients_v1_list) | **GET** /iot/v1/clients | list clients_v1
[**clients_v1_show**](ClientsV1Api.md#clients_v1_show) | **GET** /iot/v1/clients/{id} | show clients_v1


# **clients_v1_create**
> ArduinoClient clients_v1_create(client)

create clients_v1

Creates a new client associated to the user

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
api_instance = iot_api_client.ClientsV1Api(iot_api_client.ApiClient(configuration))
client = iot_api_client.Client() # Client | ClientPayload describes an oauth client

try:
    # create clients_v1
    api_response = api_instance.clients_v1_create(client)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsV1Api->clients_v1_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | [**Client**](Client.md)| ClientPayload describes an oauth client | 

### Return type

[**ArduinoClient**](ArduinoClient.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.client+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_v1_delete**
> clients_v1_delete(id)

delete clients_v1

Removes a client associated to the user

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
api_instance = iot_api_client.ClientsV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the client

try:
    # delete clients_v1
    api_instance.clients_v1_delete(id)
except ApiException as e:
    print("Exception when calling ClientsV1Api->clients_v1_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the client | 

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

# **clients_v1_list**
> list[ArduinoClient] clients_v1_list()

list clients_v1

Returns the list of oauth clients of the user

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
api_instance = iot_api_client.ClientsV1Api(iot_api_client.ApiClient(configuration))

try:
    # list clients_v1
    api_response = api_instance.clients_v1_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsV1Api->clients_v1_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ArduinoClient]**](ArduinoClient.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.client+json; type=collection, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_v1_show**
> ArduinoClient clients_v1_show(id)

show clients_v1

Returns the client requested by the user

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
api_instance = iot_api_client.ClientsV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing

try:
    # show clients_v1
    api_response = api_instance.clients_v1_show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsV1Api->clients_v1_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 

### Return type

[**ArduinoClient**](ArduinoClient.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.client+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


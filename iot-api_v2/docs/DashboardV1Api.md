# iot_api_client.DashboardV1Api

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_v1_create**](DashboardV1Api.md#dashboard_v1_create) | **POST** /iot/v1/dashboards | create dashboard_v1
[**dashboard_v1_list**](DashboardV1Api.md#dashboard_v1_list) | **GET** /iot/v1/dashboards | list dashboard_v1
[**dashboard_v1_show**](DashboardV1Api.md#dashboard_v1_show) | **GET** /iot/v1/dashboards/{id}/types/{type} | show dashboard_v1
[**dashboard_v1_update**](DashboardV1Api.md#dashboard_v1_update) | **PUT** /iot/v1/dashboards/{id} | update dashboard_v1


# **dashboard_v1_create**
> ArduinoDashboard dashboard_v1_create()

create dashboard_v1

Create a dashboard    Http body example:       {    \"name\": \"Dashboard name\",    \"type\": \"THING|SPACE|PROPERTIES\",    \"configuration\": {     \"description\": \"The configuration key is a general json field where the front end will store all the information that are useful to visualize the dashboard\"    }   }     

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
api_instance = iot_api_client.DashboardV1Api(iot_api_client.ApiClient(configuration))

try:
    # create dashboard_v1
    api_response = api_instance.dashboard_v1_create()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardV1Api->dashboard_v1_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArduinoDashboard**](ArduinoDashboard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.dashboard+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_v1_list**
> ArduinoDashboardlist dashboard_v1_list()

list dashboard_v1

Returns the list of dashboards

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
api_instance = iot_api_client.DashboardV1Api(iot_api_client.ApiClient(configuration))

try:
    # list dashboard_v1
    api_response = api_instance.dashboard_v1_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardV1Api->dashboard_v1_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArduinoDashboardlist**](ArduinoDashboardlist.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.dashboardlist+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_v1_show**
> ArduinoDashboard dashboard_v1_show(id, type)

show dashboard_v1

Returns the dashboard requested by the user

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
api_instance = iot_api_client.DashboardV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the dashboard
type = 'type_example' # str | The dashboard type

try:
    # show dashboard_v1
    api_response = api_instance.dashboard_v1_show(id, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardV1Api->dashboard_v1_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **type** | **str**| The dashboard type | 

### Return type

[**ArduinoDashboard**](ArduinoDashboard.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.dashboard+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_v1_update**
> dashboard_v1_update(id)

update dashboard_v1

Creates or update a dashboard.    Http body example:     {     \"id\": \"a860f4ba-f346-4782-8595-748396b36f5d\",     \"name\": \"Dashboard name\",     \"type\": \"THING|SPACE|PROPERTIES\",     \"configuration\": {    \"description\": \"The configuration key is a general json field where the front end will store all the information that are useful to visualize the dashboard\"     }   }

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
api_instance = iot_api_client.DashboardV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the dashboard

try:
    # update dashboard_v1
    api_instance.dashboard_v1_update(id)
except ApiException as e:
    print("Exception when calling DashboardV1Api->dashboard_v1_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


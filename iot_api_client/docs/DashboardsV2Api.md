# iot_api_client.DashboardsV2Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboards_v2_create**](DashboardsV2Api.md#dashboards_v2_create) | **POST** /v2/dashboards | create dashboards_v2
[**dashboards_v2_delete**](DashboardsV2Api.md#dashboards_v2_delete) | **DELETE** /v2/dashboards/{id} | delete dashboards_v2
[**dashboards_v2_delete_share**](DashboardsV2Api.md#dashboards_v2_delete_share) | **DELETE** /v2/dashboards/{id}/shares/{user_id} | deleteShare dashboards_v2
[**dashboards_v2_link**](DashboardsV2Api.md#dashboards_v2_link) | **PUT** /v2/dashboards/{id}/widgets/{widgetId}/variables | link dashboards_v2
[**dashboards_v2_list**](DashboardsV2Api.md#dashboards_v2_list) | **GET** /v2/dashboards | list dashboards_v2
[**dashboards_v2_list_shares**](DashboardsV2Api.md#dashboards_v2_list_shares) | **GET** /v2/dashboards/{id}/shares | listShares dashboards_v2
[**dashboards_v2_request_access**](DashboardsV2Api.md#dashboards_v2_request_access) | **PUT** /v2/dashboards/{id}/share_request | requestAccess dashboards_v2
[**dashboards_v2_share**](DashboardsV2Api.md#dashboards_v2_share) | **PUT** /v2/dashboards/{id}/shares | share dashboards_v2
[**dashboards_v2_show**](DashboardsV2Api.md#dashboards_v2_show) | **GET** /v2/dashboards/{id} | show dashboards_v2
[**dashboards_v2_update**](DashboardsV2Api.md#dashboards_v2_update) | **PUT** /v2/dashboards/{id} | update dashboards_v2


# **dashboards_v2_create**
> ArduinoDashboardv2 dashboards_v2_create(dashboardv2, x_organization=x_organization)

create dashboards_v2

Create a new dashboard

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
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    dashboardv2 = iot_api_client.Dashboardv2() # Dashboardv2 | DashboardV2Payload describes a dashboard
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # create dashboards_v2
        api_response = api_instance.dashboards_v2_create(dashboardv2, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboardv2** | [**Dashboardv2**](Dashboardv2.md)| DashboardV2Payload describes a dashboard | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDashboardv2**](ArduinoDashboardv2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_delete**
> dashboards_v2_delete(id, x_organization=x_organization)

delete dashboards_v2

Delete a dashboard

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
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # delete dashboards_v2
        api_instance.dashboards_v2_delete(id, x_organization=x_organization)
    except ApiException as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_delete_share**
> dashboards_v2_delete_share(id, user_id, x_organization=x_organization)

deleteShare dashboards_v2

Delete a user the dashboard has been shared with

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
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
user_id = 'user_id_example' # str | The id of the user
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # deleteShare dashboards_v2
        api_instance.dashboards_v2_delete_share(id, user_id, x_organization=x_organization)
    except ApiException as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_delete_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **user_id** | **str**| The id of the user | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_link**
> ArduinoVariableslinks dashboards_v2_link(id, widget_id, widgetlink, x_organization=x_organization)

link dashboards_v2

Link or detach widget variables

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
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
widget_id = 'widget_id_example' # str | The id of the widget
widgetlink = iot_api_client.Widgetlink() # Widgetlink | 
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # link dashboards_v2
        api_response = api_instance.dashboards_v2_link(id, widget_id, widgetlink, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **widget_id** | **str**| The id of the widget | 
 **widgetlink** | [**Widgetlink**](Widgetlink.md)|  | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoVariableslinks**](ArduinoVariableslinks.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_list**
> list[ArduinoDashboardv2] dashboards_v2_list(name=name, user_id=user_id, x_organization=x_organization)

list dashboards_v2

Returns the list of dashboards

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
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    name = 'name_example' # str | The name of the dashboard (optional)
user_id = 'user_id_example' # str | The user_id of the dashboard's owner (optional)
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # list dashboards_v2
        api_response = api_instance.dashboards_v2_list(name=name, user_id=user_id, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the dashboard | [optional] 
 **user_id** | **str**| The user_id of the dashboard&#39;s owner | [optional] 
 **x_organization** | **str**|  | [optional] 

### Return type

[**list[ArduinoDashboardv2]**](ArduinoDashboardv2.md)

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

# **dashboards_v2_list_shares**
> list[ArduinoDashboardshare] dashboards_v2_list_shares(id, x_organization=x_organization)

listShares dashboards_v2

List of users the dashboard has been shared with

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
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # listShares dashboards_v2
        api_response = api_instance.dashboards_v2_list_shares(id, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_list_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**list[ArduinoDashboardshare]**](ArduinoDashboardshare.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_request_access**
> dashboards_v2_request_access(id, sharerequest, x_organization=x_organization)

requestAccess dashboards_v2

Request access to a dashboard

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
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
sharerequest = iot_api_client.Sharerequest() # Sharerequest | 
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # requestAccess dashboards_v2
        api_instance.dashboards_v2_request_access(id, sharerequest, x_organization=x_organization)
    except ApiException as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_request_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **sharerequest** | [**Sharerequest**](Sharerequest.md)|  | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_share**
> dashboards_v2_share(id, dashboardshare, x_organization=x_organization)

share dashboards_v2

Share a dashboard

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
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
dashboardshare = iot_api_client.Dashboardshare() # Dashboardshare | 
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # share dashboards_v2
        api_instance.dashboards_v2_share(id, dashboardshare, x_organization=x_organization)
    except ApiException as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **dashboardshare** | [**Dashboardshare**](Dashboardshare.md)|  | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_show**
> ArduinoDashboardv2 dashboards_v2_show(id, x_organization=x_organization)

show dashboards_v2

Show a dashboard

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
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # show dashboards_v2
        api_response = api_instance.dashboards_v2_show(id, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDashboardv2**](ArduinoDashboardv2.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_update**
> ArduinoDashboardv2 dashboards_v2_update(id, dashboardv2, x_organization=x_organization)

update dashboards_v2

Updates an existing dashboard

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
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
dashboardv2 = iot_api_client.Dashboardv2() # Dashboardv2 | DashboardV2Payload describes a dashboard
x_organization = 'x_organization_example' # str |  (optional)

    try:
        # update dashboards_v2
        api_response = api_instance.dashboards_v2_update(id, dashboardv2, x_organization=x_organization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **dashboardv2** | [**Dashboardv2**](Dashboardv2.md)| DashboardV2Payload describes a dashboard | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDashboardv2**](ArduinoDashboardv2.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


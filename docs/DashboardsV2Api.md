# iot_api_client.DashboardsV2Api

All URIs are relative to *https://api2.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboards_v2_clone**](DashboardsV2Api.md#dashboards_v2_clone) | **PUT** /iot/v2/dashboards/{id}/clone | clone dashboards_v2
[**dashboards_v2_create**](DashboardsV2Api.md#dashboards_v2_create) | **POST** /iot/v2/dashboards | create dashboards_v2
[**dashboards_v2_delete**](DashboardsV2Api.md#dashboards_v2_delete) | **DELETE** /iot/v2/dashboards/{id} | delete dashboards_v2
[**dashboards_v2_delete_share**](DashboardsV2Api.md#dashboards_v2_delete_share) | **DELETE** /iot/v2/dashboards/{id}/shares/{user_id} | deleteShare dashboards_v2
[**dashboards_v2_link**](DashboardsV2Api.md#dashboards_v2_link) | **PUT** /iot/v2/dashboards/{id}/widgets/{widgetId}/variables | link dashboards_v2
[**dashboards_v2_list**](DashboardsV2Api.md#dashboards_v2_list) | **GET** /iot/v2/dashboards | list dashboards_v2
[**dashboards_v2_list_shares**](DashboardsV2Api.md#dashboards_v2_list_shares) | **GET** /iot/v2/dashboards/{id}/shares | listShares dashboards_v2
[**dashboards_v2_patch**](DashboardsV2Api.md#dashboards_v2_patch) | **PATCH** /iot/v2/dashboards/{id} | patch dashboards_v2
[**dashboards_v2_request_access**](DashboardsV2Api.md#dashboards_v2_request_access) | **PUT** /iot/v2/dashboards/{id}/share_request | requestAccess dashboards_v2
[**dashboards_v2_share**](DashboardsV2Api.md#dashboards_v2_share) | **PUT** /iot/v2/dashboards/{id}/shares | share dashboards_v2
[**dashboards_v2_show**](DashboardsV2Api.md#dashboards_v2_show) | **GET** /iot/v2/dashboards/{id} | show dashboards_v2
[**dashboards_v2_template**](DashboardsV2Api.md#dashboards_v2_template) | **GET** /iot/v2/dashboards/{id}/template | template dashboards_v2
[**dashboards_v2_update**](DashboardsV2Api.md#dashboards_v2_update) | **PUT** /iot/v2/dashboards/{id} | update dashboards_v2


# **dashboards_v2_clone**
> ArduinoDashboardv2 dashboards_v2_clone(id, clone, x_organization=x_organization)

clone dashboards_v2

Clone an existing dashboard

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv2 import ArduinoDashboardv2
from iot_api_client.models.clone import Clone
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    clone = iot_api_client.Clone() # Clone | Add overrides used when performing a clone of a dashboard
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # clone dashboards_v2
        api_response = api_instance.dashboards_v2_clone(id, clone, x_organization=x_organization)
        print("The response of DashboardsV2Api->dashboards_v2_clone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_clone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **clone** | [**Clone**](Clone.md)| Add overrides used when performing a clone of a dashboard | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDashboardv2**](ArduinoDashboardv2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.dashboardv2+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_create**
> ArduinoDashboardv2 dashboards_v2_create(dashboardv2, x_organization=x_organization)

create dashboards_v2

Create a new dashboard

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv2 import ArduinoDashboardv2
from iot_api_client.models.dashboardv2 import Dashboardv2
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    dashboardv2 = iot_api_client.Dashboardv2() # Dashboardv2 | Describes a dashboard
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # create dashboards_v2
        api_response = api_instance.dashboards_v2_create(dashboardv2, x_organization=x_organization)
        print("The response of DashboardsV2Api->dashboards_v2_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboardv2** | [**Dashboardv2**](Dashboardv2.md)| Describes a dashboard | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDashboardv2**](ArduinoDashboardv2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.dashboardv2+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_delete**
> dashboards_v2_delete(id, force=force, x_organization=x_organization)

delete dashboards_v2

Delete a dashboard

### Example

* Bearer Authentication (oauth2):

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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    force = False # bool | If true, hard delete the thing (optional) (default to False)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # delete dashboards_v2
        api_instance.dashboards_v2_delete(id, force=force, x_organization=x_organization)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **force** | **bool**| If true, hard delete the thing | [optional] [default to False]
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_delete_share**
> dashboards_v2_delete_share(id, user_id, x_organization=x_organization)

deleteShare dashboards_v2

Delete a user the dashboard has been shared with

### Example

* Bearer Authentication (oauth2):

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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    user_id = 'user_id_example' # str | The id of the user
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # deleteShare dashboards_v2
        api_instance.dashboards_v2_delete_share(id, user_id, x_organization=x_organization)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_delete_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **user_id** | **str**| The id of the user | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_link**
> ArduinoVariableslinks dashboards_v2_link(id, widget_id, widgetlink, x_organization=x_organization)

link dashboards_v2

Link or detach widget variables

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_variableslinks import ArduinoVariableslinks
from iot_api_client.models.widgetlink import Widgetlink
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    widget_id = 'widget_id_example' # str | The id of the widget
    widgetlink = iot_api_client.Widgetlink() # Widgetlink | 
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # link dashboards_v2
        api_response = api_instance.dashboards_v2_link(id, widget_id, widgetlink, x_organization=x_organization)
        print("The response of DashboardsV2Api->dashboards_v2_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **widget_id** | **str**| The id of the widget | 
 **widgetlink** | [**Widgetlink**](Widgetlink.md)|  | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoVariableslinks**](ArduinoVariableslinks.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.variableslinks+json, application/vnd.goa.error+json

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

# **dashboards_v2_list**
> List[ArduinoDashboardv2] dashboards_v2_list(name=name, user_id=user_id, x_organization=x_organization)

list dashboards_v2

Returns the list of dashboards

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv2 import ArduinoDashboardv2
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    name = 'name_example' # str | Filter by name of the dashboard. It support like matching. (optional)
    user_id = 'user_id_example' # str | Filter by user_id of the dashboard's owner (optional)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # list dashboards_v2
        api_response = api_instance.dashboards_v2_list(name=name, user_id=user_id, x_organization=x_organization)
        print("The response of DashboardsV2Api->dashboards_v2_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by name of the dashboard. It support like matching. | [optional] 
 **user_id** | **str**| Filter by user_id of the dashboard&#39;s owner | [optional] 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**List[ArduinoDashboardv2]**](ArduinoDashboardv2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.dashboardv2+json; type=collection, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_list_shares**
> List[ArduinoDashboardshare] dashboards_v2_list_shares(id, x_organization=x_organization)

listShares dashboards_v2

List of users the dashboard has been shared with

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardshare import ArduinoDashboardshare
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # listShares dashboards_v2
        api_response = api_instance.dashboards_v2_list_shares(id, x_organization=x_organization)
        print("The response of DashboardsV2Api->dashboards_v2_list_shares:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_list_shares: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**List[ArduinoDashboardshare]**](ArduinoDashboardshare.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.dashboardshare+json; type=collection, application/vnd.goa.error+json

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

# **dashboards_v2_patch**
> ArduinoDashboardv2 dashboards_v2_patch(id, dashboardv2, x_organization=x_organization)

patch dashboards_v2

Updates an existing dashboard field without overwriting the existing data

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv2 import ArduinoDashboardv2
from iot_api_client.models.dashboardv2 import Dashboardv2
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    dashboardv2 = iot_api_client.Dashboardv2() # Dashboardv2 | Describes a dashboard
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # patch dashboards_v2
        api_response = api_instance.dashboards_v2_patch(id, dashboardv2, x_organization=x_organization)
        print("The response of DashboardsV2Api->dashboards_v2_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **dashboardv2** | [**Dashboardv2**](Dashboardv2.md)| Describes a dashboard | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDashboardv2**](ArduinoDashboardv2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.dashboardv2+json, application/vnd.goa.error+json

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

# **dashboards_v2_request_access**
> dashboards_v2_request_access(id, sharerequest, x_organization=x_organization)

requestAccess dashboards_v2

Request access to a dashboard

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.sharerequest import Sharerequest
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    sharerequest = iot_api_client.Sharerequest() # Sharerequest | 
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # requestAccess dashboards_v2
        api_instance.dashboards_v2_request_access(id, sharerequest, x_organization=x_organization)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_request_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **sharerequest** | [**Sharerequest**](Sharerequest.md)|  | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_share**
> dashboards_v2_share(id, dashboardshare, x_organization=x_organization)

share dashboards_v2

Share a dashboard

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.dashboardshare import Dashboardshare
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    dashboardshare = iot_api_client.Dashboardshare() # Dashboardshare | 
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # share dashboards_v2
        api_instance.dashboards_v2_share(id, dashboardshare, x_organization=x_organization)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **dashboardshare** | [**Dashboardshare**](Dashboardshare.md)|  | 
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_show**
> ArduinoDashboardv2 dashboards_v2_show(id, x_organization=x_organization)

show dashboards_v2

Show a dashboard by id

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv2 import ArduinoDashboardv2
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # show dashboards_v2
        api_response = api_instance.dashboards_v2_show(id, x_organization=x_organization)
        print("The response of DashboardsV2Api->dashboards_v2_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDashboardv2**](ArduinoDashboardv2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.dashboardv2+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v2_template**
> ArduinoDashboardv2template dashboards_v2_template(id, x_organization=x_organization)

template dashboards_v2

Get a template of the dashboard

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv2template import ArduinoDashboardv2template
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # template dashboards_v2
        api_response = api_instance.dashboards_v2_template(id, x_organization=x_organization)
        print("The response of DashboardsV2Api->dashboards_v2_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDashboardv2template**](ArduinoDashboardv2template.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.dashboardv2template+json, application/vnd.goa.error+json

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

# **dashboards_v2_update**
> ArduinoDashboardv2 dashboards_v2_update(id, dashboardv2, x_organization=x_organization)

update dashboards_v2

Updates an existing dashboard

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv2 import ArduinoDashboardv2
from iot_api_client.models.dashboardv2 import Dashboardv2
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

# Configure Bearer authorization: oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV2Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    dashboardv2 = iot_api_client.Dashboardv2() # Dashboardv2 | Describes a dashboard
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # update dashboards_v2
        api_response = api_instance.dashboards_v2_update(id, dashboardv2, x_organization=x_organization)
        print("The response of DashboardsV2Api->dashboards_v2_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV2Api->dashboards_v2_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **dashboardv2** | [**Dashboardv2**](Dashboardv2.md)| Describes a dashboard | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoDashboardv2**](ArduinoDashboardv2.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.dashboardv2+json, application/vnd.goa.error+json

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


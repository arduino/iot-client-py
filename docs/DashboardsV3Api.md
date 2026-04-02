# iot_api_client.DashboardsV3Api

All URIs are relative to *https://api2.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboards_v3_clone**](DashboardsV3Api.md#dashboards_v3_clone) | **PUT** /iot/v3/dashboards/{id}/clone | clone dashboards_v3
[**dashboards_v3_create**](DashboardsV3Api.md#dashboards_v3_create) | **POST** /iot/v3/dashboards | create dashboards_v3
[**dashboards_v3_list**](DashboardsV3Api.md#dashboards_v3_list) | **GET** /iot/v3/dashboards | list dashboards_v3
[**dashboards_v3_patch**](DashboardsV3Api.md#dashboards_v3_patch) | **PATCH** /iot/v3/dashboards/{id} | patch dashboards_v3
[**dashboards_v3_show**](DashboardsV3Api.md#dashboards_v3_show) | **GET** /iot/v3/dashboards/{id} | show dashboards_v3
[**dashboards_v3_template**](DashboardsV3Api.md#dashboards_v3_template) | **GET** /iot/v3/dashboards/{id}/template | template dashboards_v3
[**dashboards_v3_update**](DashboardsV3Api.md#dashboards_v3_update) | **PUT** /iot/v3/dashboards/{id} | update dashboards_v3


# **dashboards_v3_clone**
> ArduinoDashboardv3 dashboards_v3_clone(id, clone, x_organization=x_organization)

clone dashboards_v3

Clone an existing dashboard

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv3 import ArduinoDashboardv3
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV3Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    clone = iot_api_client.Clone() # Clone | 
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # clone dashboards_v3
        api_response = api_instance.dashboards_v3_clone(id, clone, x_organization=x_organization)
        print("The response of DashboardsV3Api->dashboards_v3_clone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV3Api->dashboards_v3_clone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **clone** | [**Clone**](Clone.md)|  | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDashboardv3**](ArduinoDashboardv3.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.dashboardv3+json, application/vnd.goa.error+json

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

# **dashboards_v3_create**
> ArduinoDashboardv3 dashboards_v3_create(dashboardv3, x_organization=x_organization)

create dashboards_v3

Create a new dashboard

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv3 import ArduinoDashboardv3
from iot_api_client.models.dashboardv3 import Dashboardv3
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV3Api(api_client)
    dashboardv3 = iot_api_client.Dashboardv3() # Dashboardv3 | DashboardV3Payload describes a dashboard
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # create dashboards_v3
        api_response = api_instance.dashboards_v3_create(dashboardv3, x_organization=x_organization)
        print("The response of DashboardsV3Api->dashboards_v3_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV3Api->dashboards_v3_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboardv3** | [**Dashboardv3**](Dashboardv3.md)| DashboardV3Payload describes a dashboard | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDashboardv3**](ArduinoDashboardv3.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.dashboardv3+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v3_list**
> List[ArduinoDashboardv3] dashboards_v3_list(name=name, thing_id=thing_id, user_id=user_id, x_organization=x_organization)

list dashboards_v3

Returns the list of dashboards

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv3 import ArduinoDashboardv3
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV3Api(api_client)
    name = 'name_example' # str | The name of the dashboard (optional)
    thing_id = 'thing_id_example' # str | The thing_id of the dashboard's properties (optional)
    user_id = 'user_id_example' # str | The user_id of the dashboard's owner (optional)
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # list dashboards_v3
        api_response = api_instance.dashboards_v3_list(name=name, thing_id=thing_id, user_id=user_id, x_organization=x_organization)
        print("The response of DashboardsV3Api->dashboards_v3_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV3Api->dashboards_v3_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the dashboard | [optional] 
 **thing_id** | **str**| The thing_id of the dashboard&#39;s properties | [optional] 
 **user_id** | **str**| The user_id of the dashboard&#39;s owner | [optional] 
 **x_organization** | **str**|  | [optional] 

### Return type

[**List[ArduinoDashboardv3]**](ArduinoDashboardv3.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.dashboardv3+json; type=collection, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v3_patch**
> ArduinoDashboardv3 dashboards_v3_patch(id, dashboardv3, x_organization=x_organization)

patch dashboards_v3

Updates an existing dashboard field without overwriting the existing data

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv3 import ArduinoDashboardv3
from iot_api_client.models.dashboardv3 import Dashboardv3
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV3Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    dashboardv3 = iot_api_client.Dashboardv3() # Dashboardv3 | DashboardV3Payload describes a dashboard
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # patch dashboards_v3
        api_response = api_instance.dashboards_v3_patch(id, dashboardv3, x_organization=x_organization)
        print("The response of DashboardsV3Api->dashboards_v3_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV3Api->dashboards_v3_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **dashboardv3** | [**Dashboardv3**](Dashboardv3.md)| DashboardV3Payload describes a dashboard | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDashboardv3**](ArduinoDashboardv3.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.dashboardv3+json, application/vnd.goa.error+json

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

# **dashboards_v3_show**
> ArduinoDashboardv3 dashboards_v3_show(id, x_organization=x_organization)

show dashboards_v3

Show a dashboard

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv3 import ArduinoDashboardv3
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV3Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # show dashboards_v3
        api_response = api_instance.dashboards_v3_show(id, x_organization=x_organization)
        print("The response of DashboardsV3Api->dashboards_v3_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV3Api->dashboards_v3_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDashboardv3**](ArduinoDashboardv3.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.dashboardv3+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboards_v3_template**
> ArduinoDashboardv3template dashboards_v3_template(id, x_organization=x_organization)

template dashboards_v3

Get a template of the dashboard

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv3template import ArduinoDashboardv3template
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV3Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # template dashboards_v3
        api_response = api_instance.dashboards_v3_template(id, x_organization=x_organization)
        print("The response of DashboardsV3Api->dashboards_v3_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV3Api->dashboards_v3_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDashboardv3template**](ArduinoDashboardv3template.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.dashboardv3template+json, application/vnd.goa.error+json

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

# **dashboards_v3_update**
> ArduinoDashboardv3 dashboards_v3_update(id, dashboardv3, x_organization=x_organization)

update dashboards_v3

Updates an existing dashboard

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_dashboardv3 import ArduinoDashboardv3
from iot_api_client.models.dashboardv3 import Dashboardv3
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.DashboardsV3Api(api_client)
    id = 'id_example' # str | The id of the dashboard
    dashboardv3 = iot_api_client.Dashboardv3() # Dashboardv3 | DashboardV3Payload describes a dashboard
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # update dashboards_v3
        api_response = api_instance.dashboards_v3_update(id, dashboardv3, x_organization=x_organization)
        print("The response of DashboardsV3Api->dashboards_v3_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsV3Api->dashboards_v3_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the dashboard | 
 **dashboardv3** | [**Dashboardv3**](Dashboardv3.md)| DashboardV3Payload describes a dashboard | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoDashboardv3**](ArduinoDashboardv3.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.dashboardv3+json, application/vnd.goa.error+json

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


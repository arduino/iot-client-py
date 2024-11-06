# iot_api_client.PropertiesV2Api

All URIs are relative to *https://api2.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**properties_v2_create**](PropertiesV2Api.md#properties_v2_create) | **PUT** /iot/v2/things/{id}/properties | create properties_v2
[**properties_v2_delete**](PropertiesV2Api.md#properties_v2_delete) | **DELETE** /iot/v2/things/{id}/properties/{pid} | delete properties_v2
[**properties_v2_list**](PropertiesV2Api.md#properties_v2_list) | **GET** /iot/v2/things/{id}/properties | list properties_v2
[**properties_v2_publish**](PropertiesV2Api.md#properties_v2_publish) | **PUT** /iot/v2/things/{id}/properties/{pid}/publish | publish properties_v2
[**properties_v2_show**](PropertiesV2Api.md#properties_v2_show) | **GET** /iot/v2/things/{id}/properties/{pid} | show properties_v2
[**properties_v2_timeseries**](PropertiesV2Api.md#properties_v2_timeseries) | **GET** /iot/v2/things/{id}/properties/{pid}/timeseries | timeseries properties_v2
[**properties_v2_update**](PropertiesV2Api.md#properties_v2_update) | **POST** /iot/v2/things/{id}/properties/{pid} | update properties_v2


# **properties_v2_create**
> ArduinoProperty properties_v2_create(id, model_property, x_organization=x_organization)

create properties_v2

Creates a new property associated to a thing

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_property import ArduinoProperty
from iot_api_client.models.model_property import ModelProperty
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
    api_instance = iot_api_client.PropertiesV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    model_property = iot_api_client.ModelProperty() # ModelProperty | PropertyPayload describes a property of a thing. No field is mandatory
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # create properties_v2
        api_response = api_instance.properties_v2_create(id, model_property, x_organization=x_organization)
        print("The response of PropertiesV2Api->properties_v2_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertiesV2Api->properties_v2_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **model_property** | [**ModelProperty**](ModelProperty.md)| PropertyPayload describes a property of a thing. No field is mandatory | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoProperty**](ArduinoProperty.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.property+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_v2_delete**
> properties_v2_delete(id, pid, force=force, x_organization=x_organization)

delete properties_v2

Removes a property associated to a thing

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
    api_instance = iot_api_client.PropertiesV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    pid = 'pid_example' # str | The id of the property
    force = False # bool | If true, hard delete the property (optional) (default to False)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # delete properties_v2
        api_instance.properties_v2_delete(id, pid, force=force, x_organization=x_organization)
    except Exception as e:
        print("Exception when calling PropertiesV2Api->properties_v2_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **pid** | **str**| The id of the property | 
 **force** | **bool**| If true, hard delete the property | [optional] [default to False]
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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_v2_list**
> List[ArduinoProperty] properties_v2_list(id, show_deleted=show_deleted, x_organization=x_organization)

list properties_v2

Returns the list of properties associated to the thing

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_property import ArduinoProperty
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
    api_instance = iot_api_client.PropertiesV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    show_deleted = False # bool | If true, shows the soft deleted properties (optional) (default to False)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # list properties_v2
        api_response = api_instance.properties_v2_list(id, show_deleted=show_deleted, x_organization=x_organization)
        print("The response of PropertiesV2Api->properties_v2_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertiesV2Api->properties_v2_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **show_deleted** | **bool**| If true, shows the soft deleted properties | [optional] [default to False]
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**List[ArduinoProperty]**](ArduinoProperty.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.property+json; type=collection, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_v2_publish**
> properties_v2_publish(id, pid, property_value, x_organization=x_organization)

publish properties_v2

Publish a property value to MQTT

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.property_value import PropertyValue
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
    api_instance = iot_api_client.PropertiesV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    pid = 'pid_example' # str | The id of the property
    property_value = iot_api_client.PropertyValue() # PropertyValue | PropertyValuePayload describes a property value
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # publish properties_v2
        api_instance.properties_v2_publish(id, pid, property_value, x_organization=x_organization)
    except Exception as e:
        print("Exception when calling PropertiesV2Api->properties_v2_publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **pid** | **str**| The id of the property | 
 **property_value** | [**PropertyValue**](PropertyValue.md)| PropertyValuePayload describes a property value | 
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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_v2_show**
> ArduinoProperty properties_v2_show(id, pid, show_deleted=show_deleted, x_organization=x_organization)

show properties_v2

Returns the property requested by the user

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_property import ArduinoProperty
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
    api_instance = iot_api_client.PropertiesV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    pid = 'pid_example' # str | The id of the property
    show_deleted = False # bool | If true, shows the soft deleted properties (optional) (default to False)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # show properties_v2
        api_response = api_instance.properties_v2_show(id, pid, show_deleted=show_deleted, x_organization=x_organization)
        print("The response of PropertiesV2Api->properties_v2_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertiesV2Api->properties_v2_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **pid** | **str**| The id of the property | 
 **show_deleted** | **bool**| If true, shows the soft deleted properties | [optional] [default to False]
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoProperty**](ArduinoProperty.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.property+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_v2_timeseries**
> ArduinoTimeseriesmedia properties_v2_timeseries(id, pid, aggregation=aggregation, desc=desc, var_from=var_from, interval=interval, to=to, x_organization=x_organization)

timeseries properties_v2

Get numerical property's historic data binned on a specified time interval (note: the total number of data points should NOT be greater than 1000 otherwise the result will be truncated)

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_timeseriesmedia import ArduinoTimeseriesmedia
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
    api_instance = iot_api_client.PropertiesV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    pid = 'pid_example' # str | ID of a numerical property
    aggregation = 'aggregation_example' # str | Samples aggregation statistic. Supported aggregations AVG|MAX|MIN|COUNT|SUM|PCT_99|PCT_95|PCT_90|PCT_75|PCT_50|PCT_15|PCT_5 (optional)
    desc = False # bool | Whether data's ordering (by time) should be descending (optional) (default to False)
    var_from = 'var_from_example' # str | Get data with a timestamp >= to this date (default: 2 weeks ago, min: 1842-01-01T00:00:00Z, max: 2242-01-01T00:00:00Z) (optional)
    interval = 56 # int | Binning interval in seconds (defaut: the smallest possible value compatibly with the limit of 1000 data points in the response) (optional)
    to = 'to_example' # str | Get data with a timestamp < to this date (default: now, min: 1842-01-01T00:00:00Z, max: 2242-01-01T00:00:00Z) (optional)
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # timeseries properties_v2
        api_response = api_instance.properties_v2_timeseries(id, pid, aggregation=aggregation, desc=desc, var_from=var_from, interval=interval, to=to, x_organization=x_organization)
        print("The response of PropertiesV2Api->properties_v2_timeseries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertiesV2Api->properties_v2_timeseries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **pid** | **str**| ID of a numerical property | 
 **aggregation** | **str**| Samples aggregation statistic. Supported aggregations AVG|MAX|MIN|COUNT|SUM|PCT_99|PCT_95|PCT_90|PCT_75|PCT_50|PCT_15|PCT_5 | [optional] 
 **desc** | **bool**| Whether data&#39;s ordering (by time) should be descending | [optional] [default to False]
 **var_from** | **str**| Get data with a timestamp &gt;&#x3D; to this date (default: 2 weeks ago, min: 1842-01-01T00:00:00Z, max: 2242-01-01T00:00:00Z) | [optional] 
 **interval** | **int**| Binning interval in seconds (defaut: the smallest possible value compatibly with the limit of 1000 data points in the response) | [optional] 
 **to** | **str**| Get data with a timestamp &lt; to this date (default: now, min: 1842-01-01T00:00:00Z, max: 2242-01-01T00:00:00Z) | [optional] 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoTimeseriesmedia**](ArduinoTimeseriesmedia.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.timeseriesmedia+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_v2_update**
> ArduinoProperty properties_v2_update(id, pid, model_property, x_organization=x_organization)

update properties_v2

Updates a property associated to a thing

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_property import ArduinoProperty
from iot_api_client.models.model_property import ModelProperty
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
    api_instance = iot_api_client.PropertiesV2Api(api_client)
    id = 'id_example' # str | The id of the thing
    pid = 'pid_example' # str | The id of the property
    model_property = iot_api_client.ModelProperty() # ModelProperty | PropertyPayload describes a property of a thing. No field is mandatory
    x_organization = 'x_organization_example' # str | Organization space identifer (optional) (optional)

    try:
        # update properties_v2
        api_response = api_instance.properties_v2_update(id, pid, model_property, x_organization=x_organization)
        print("The response of PropertiesV2Api->properties_v2_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertiesV2Api->properties_v2_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **pid** | **str**| The id of the property | 
 **model_property** | [**ModelProperty**](ModelProperty.md)| PropertyPayload describes a property of a thing. No field is mandatory | 
 **x_organization** | **str**| Organization space identifer (optional) | [optional] 

### Return type

[**ArduinoProperty**](ArduinoProperty.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.property+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


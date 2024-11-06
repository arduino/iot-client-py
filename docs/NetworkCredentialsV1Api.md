# iot_api_client.NetworkCredentialsV1Api

All URIs are relative to *https://api2.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_credentials_v1_show**](NetworkCredentialsV1Api.md#network_credentials_v1_show) | **GET** /iot/v1/network_credentials/{type} | show network_credentials_v1
[**network_credentials_v1_show_by_device**](NetworkCredentialsV1Api.md#network_credentials_v1_show_by_device) | **GET** /iot/v1/network_credentials/{type}/connections | showByDevice network_credentials_v1


# **network_credentials_v1_show**
> List[ArduinoCredentialsv1] network_credentials_v1_show(type, connection=connection)

show network_credentials_v1

Show required network credentials depending on device type

### Example

* Bearer Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_credentialsv1 import ArduinoCredentialsv1
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
    api_instance = iot_api_client.NetworkCredentialsV1Api(api_client)
    type = 'type_example' # str | Device type
    connection = 'connection_example' # str | Connection used by the device (optional)

    try:
        # show network_credentials_v1
        api_response = api_instance.network_credentials_v1_show(type, connection=connection)
        print("The response of NetworkCredentialsV1Api->network_credentials_v1_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkCredentialsV1Api->network_credentials_v1_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Device type | 
 **connection** | **str**| Connection used by the device | [optional] 

### Return type

[**List[ArduinoCredentialsv1]**](ArduinoCredentialsv1.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.credentialsv1+json; type=collection, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_credentials_v1_show_by_device**
> network_credentials_v1_show_by_device(type)

showByDevice network_credentials_v1

Show available connection types depending on device type

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
    api_instance = iot_api_client.NetworkCredentialsV1Api(api_client)
    type = 'type_example' # str | Device type

    try:
        # showByDevice network_credentials_v1
        api_instance.network_credentials_v1_show_by_device(type)
    except Exception as e:
        print("Exception when calling NetworkCredentialsV1Api->network_credentials_v1_show_by_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Device type | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


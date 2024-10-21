# iot_api_client.PropertyTypesV1Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**property_types_v1_list_types**](PropertyTypesV1Api.md#property_types_v1_list_types) | **GET** /v1/property_types | listTypes property_types_v1


# **property_types_v1_list_types**
> List[ArduinoPropertytype] property_types_v1_list_types()

listTypes property_types_v1

Returns the list of available property types

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import iot_api_client
from iot_api_client.models.arduino_propertytype import ArduinoPropertytype
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
    api_instance = iot_api_client.PropertyTypesV1Api(api_client)

    try:
        # listTypes property_types_v1
        api_response = api_instance.property_types_v1_list_types()
        print("The response of PropertyTypesV1Api->property_types_v1_list_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertyTypesV1Api->property_types_v1_list_types: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ArduinoPropertytype]**](ArduinoPropertytype.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.propertytype+json; type=collection, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


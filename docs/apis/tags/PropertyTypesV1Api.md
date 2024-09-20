<a name="__pageTop"></a>
# iot_api_client.apis.tags.property_types_v1_api.PropertyTypesV1Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**property_types_v1_list_types**](#property_types_v1_list_types) | **get** /v1/property_types | listTypes property_types_v1

# **property_types_v1_list_types**
<a name="property_types_v1_list_types"></a>
> ArduinoPropertytypeCollection property_types_v1_list_types()

listTypes property_types_v1

Returns the list of available property types

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import property_types_v1_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_propertytype_collection import ArduinoPropertytypeCollection
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
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = property_types_v1_api.PropertyTypesV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # listTypes property_types_v1
        api_response = api_instance.property_types_v1_list_types()
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling PropertyTypesV1Api->property_types_v1_list_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#property_types_v1_list_types.ApiResponseFor200) | OK
500 | [ApiResponseFor500](#property_types_v1_list_types.ApiResponseFor500) | Internal Server Error

#### property_types_v1_list_types.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoPropertytypejsonTypecollection, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoPropertytypejsonTypecollection
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoPropertytypeCollection**](../../models/ArduinoPropertytypeCollection.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoPropertytypeCollection**](../../models/ArduinoPropertytypeCollection.md) |  | 


#### property_types_v1_list_types.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoPropertytypejsonTypecollection, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoPropertytypejsonTypecollection
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


# iot_api_client.ThingsV2TagsApi

All URIs are relative to *https://api2.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**things_v2_tags_delete**](ThingsV2TagsApi.md#things_v2_tags_delete) | **DELETE** /iot/v2/things/{id}/tags/{key} | delete things_v2_tags
[**things_v2_tags_list**](ThingsV2TagsApi.md#things_v2_tags_list) | **GET** /iot/v2/things/{id}/tags | list things_v2_tags
[**things_v2_tags_upsert**](ThingsV2TagsApi.md#things_v2_tags_upsert) | **PUT** /iot/v2/things/{id}/tags | upsert things_v2_tags


# **things_v2_tags_delete**
> things_v2_tags_delete(id, key)

delete things_v2_tags

Delete a tag associated to the thing given its key.

### Example

* OAuth Authentication (oauth2):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.ThingsV2TagsApi(api_client)
    id = 'id_example' # str | The id of the thing
    key = 'key_example' # str | The key of the tag

    try:
        # delete things_v2_tags
        api_instance.things_v2_tags_delete(id, key)
    except Exception as e:
        print("Exception when calling ThingsV2TagsApi->things_v2_tags_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **key** | **str**| The key of the tag | 

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

# **things_v2_tags_list**
> ArduinoTags things_v2_tags_list(id)

list things_v2_tags

List tags associated to the thing.

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_tags import ArduinoTags
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
    api_instance = iot_api_client.ThingsV2TagsApi(api_client)
    id = 'id_example' # str | The id of the thing

    try:
        # list things_v2_tags
        api_response = api_instance.things_v2_tags_list(id)
        print("The response of ThingsV2TagsApi->things_v2_tags_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThingsV2TagsApi->things_v2_tags_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 

### Return type

[**ArduinoTags**](ArduinoTags.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.tags+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **things_v2_tags_upsert**
> things_v2_tags_upsert(id, tag)

upsert things_v2_tags

Creates or updates a tag associated to the thing.

### Example

* OAuth Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.tag import Tag
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
    api_instance = iot_api_client.ThingsV2TagsApi(api_client)
    id = 'id_example' # str | The id of the thing
    tag = iot_api_client.Tag() # Tag | 

    try:
        # upsert things_v2_tags
        api_instance.things_v2_tags_upsert(id, tag)
    except Exception as e:
        print("Exception when calling ThingsV2TagsApi->things_v2_tags_upsert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **tag** | [**Tag**](Tag.md)|  | 

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


# iot_api_client.ManageApi

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manage_delete_user**](ManageApi.md#manage_delete_user) | **DELETE** /iot/v1/manage/users/{id} | delete_user manage


# **manage_delete_user**
> manage_delete_user(id)

delete_user manage

Deletes the user, all their sketches and libraries

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
api_instance = iot_api_client.ManageApi(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the user. Can be 'me' to access the currently authenticated user

try:
    # delete_user manage
    api_instance.manage_delete_user(id)
except ApiException as e:
    print("Exception when calling ManageApi->manage_delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the user. Can be &#39;me&#39; to access the currently authenticated user | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | NotFound: The requested user doesn&#39;t exist or it&#39;s not visible to the current user. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


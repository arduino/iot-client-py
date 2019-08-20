# iot_api_client.CleanupApi

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cleanup_iot**](CleanupApi.md#cleanup_iot) | **POST** /iot/v1/cleanup | iot cleanup


# **cleanup_iot**
> cleanup_iot()

iot cleanup

Iot removes the things created more than an hour ago and never got reclaimed. It then deletes the certificates that are no longer associated with a thing

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
api_instance = iot_api_client.CleanupApi(iot_api_client.ApiClient(configuration))

try:
    # iot cleanup
    api_instance.cleanup_iot()
except ApiException as e:
    print("Exception when calling CleanupApi->cleanup_iot: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


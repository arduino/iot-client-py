# iot_api_client.DefaultApi

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_iot_docs**](DefaultApi.md#public_iot_docs) | **GET** /iot/docs | Download templates/docs.html
[**public_iot_swagger_json**](DefaultApi.md#public_iot_swagger_json) | **GET** /iot/swagger.json | Download swagger/swagger.json


# **public_iot_docs**
> file public_iot_docs()

Download templates/docs.html

### Example

```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iot_api_client.DefaultApi()

try:
    # Download templates/docs.html
    api_response = api_instance.public_iot_docs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->public_iot_docs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_iot_swagger_json**
> file public_iot_swagger_json()

Download swagger/swagger.json

### Example

```python
from __future__ import print_function
import time
import iot_api_client
from iot_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = iot_api_client.DefaultApi()

try:
    # Download swagger/swagger.json
    api_response = api_instance.public_iot_swagger_json()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->public_iot_swagger_json: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File downloaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


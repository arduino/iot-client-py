# iot_api_client.LoraGwV1Api

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lora_gw_v1_claim**](LoraGwV1Api.md#lora_gw_v1_claim) | **POST** /iot/v1/lora-gw/{id}/claim | claim lora_gw_v1
[**lora_gw_v1_create**](LoraGwV1Api.md#lora_gw_v1_create) | **PUT** /iot/v1/lora-gw/ | create lora_gw_v1
[**lora_gw_v1_delete**](LoraGwV1Api.md#lora_gw_v1_delete) | **DELETE** /iot/v1/lora-gw/{id} | delete lora_gw_v1
[**lora_gw_v1_show**](LoraGwV1Api.md#lora_gw_v1_show) | **GET** /iot/v1/lora-gw/{id} | show lora_gw_v1
[**lora_gw_v1_unclaim**](LoraGwV1Api.md#lora_gw_v1_unclaim) | **POST** /iot/v1/lora-gw/{id}/unclaim | unclaim lora_gw_v1


# **lora_gw_v1_claim**
> ArduinoLoragwv1 lora_gw_v1_claim(id, claim_lora_gw_v1_payload)

claim lora_gw_v1

Assign a lora gateway to a user, create a device_v1 resource, create an a2a user (if not existing), create the device on a2a

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
api_instance = iot_api_client.LoraGwV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The mac/serial_number/device_code of the lora gateway. It is printed on the box, and used to connect to a2a.
claim_lora_gw_v1_payload = iot_api_client.ClaimLoraGwV1Payload() # ClaimLoraGwV1Payload | 

try:
    # claim lora_gw_v1
    api_response = api_instance.lora_gw_v1_claim(id, claim_lora_gw_v1_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoraGwV1Api->lora_gw_v1_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The mac/serial_number/device_code of the lora gateway. It is printed on the box, and used to connect to a2a. | 
 **claim_lora_gw_v1_payload** | [**ClaimLoraGwV1Payload**](ClaimLoraGwV1Payload.md)|  | 

### Return type

[**ArduinoLoragwv1**](ArduinoLoragwv1.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.loragwv1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lora_gw_v1_create**
> ArduinoLoragwv1 lora_gw_v1_create(create_lora_gw_v1_payload)

create lora_gw_v1

Create a new pending lora gateway. Its info are only saved on our database.

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
api_instance = iot_api_client.LoraGwV1Api(iot_api_client.ApiClient(configuration))
create_lora_gw_v1_payload = iot_api_client.CreateLoraGwV1Payload() # CreateLoraGwV1Payload | 

try:
    # create lora_gw_v1
    api_response = api_instance.lora_gw_v1_create(create_lora_gw_v1_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoraGwV1Api->lora_gw_v1_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_lora_gw_v1_payload** | [**CreateLoraGwV1Payload**](CreateLoraGwV1Payload.md)|  | 

### Return type

[**ArduinoLoragwv1**](ArduinoLoragwv1.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.loragwv1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lora_gw_v1_delete**
> lora_gw_v1_delete(id)

delete lora_gw_v1

Removes a lora gateway

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
api_instance = iot_api_client.LoraGwV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the lora gateway. It's calculated from the mac using magic

try:
    # delete lora_gw_v1
    api_instance.lora_gw_v1_delete(id)
except ApiException as e:
    print("Exception when calling LoraGwV1Api->lora_gw_v1_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the lora gateway. It&#39;s calculated from the mac using magic | 

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

# **lora_gw_v1_show**
> ArduinoLoragwv1 lora_gw_v1_show(id)

show lora_gw_v1

Retrieve info about a lora gateway.

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
api_instance = iot_api_client.LoraGwV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the lora gateway. It's calculated from the mac using magic

try:
    # show lora_gw_v1
    api_response = api_instance.lora_gw_v1_show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoraGwV1Api->lora_gw_v1_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the lora gateway. It&#39;s calculated from the mac using magic | 

### Return type

[**ArduinoLoragwv1**](ArduinoLoragwv1.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.loragwv1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lora_gw_v1_unclaim**
> ArduinoLoragwv1 lora_gw_v1_unclaim(id)

unclaim lora_gw_v1

Remove the gateway from a2a, delete the device_v1 resource.

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
api_instance = iot_api_client.LoraGwV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The mac/serial_number/device_code of the lora gateway. It is printed on the box, and used to connect to a2a.

try:
    # unclaim lora_gw_v1
    api_response = api_instance.lora_gw_v1_unclaim(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoraGwV1Api->lora_gw_v1_unclaim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The mac/serial_number/device_code of the lora gateway. It is printed on the box, and used to connect to a2a. | 

### Return type

[**ArduinoLoragwv1**](ArduinoLoragwv1.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.loragwv1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# iot_api_client.PropertiesV1Api

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**properties_v1_create**](PropertiesV1Api.md#properties_v1_create) | **PUT** /v1/things/{id}/properties | create properties_v1
[**properties_v1_delete**](PropertiesV1Api.md#properties_v1_delete) | **DELETE** /v1/things/{id}/properties/{pid} | delete properties_v1
[**properties_v1_list**](PropertiesV1Api.md#properties_v1_list) | **GET** /v1/things/{id}/properties | list properties_v1
[**properties_v1_publish**](PropertiesV1Api.md#properties_v1_publish) | **PUT** /v1/things/{id}/properties/{pid}/publish | publish properties_v1
[**properties_v1_show**](PropertiesV1Api.md#properties_v1_show) | **GET** /v1/things/{id}/properties/{pid} | show properties_v1
[**properties_v1_update**](PropertiesV1Api.md#properties_v1_update) | **POST** /v1/things/{id}/properties/{pid} | update properties_v1


# **properties_v1_create**
> ArduinoProperty properties_v1_create(id, model_property)

create properties_v1

Creates a new property associated to a thing

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
api_instance = iot_api_client.PropertiesV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
model_property = iot_api_client.ModelProperty() # ModelProperty | PropertyPayload describes a property of a thing. No field is mandatory

try:
    # create properties_v1
    api_response = api_instance.properties_v1_create(id, model_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertiesV1Api->properties_v1_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **model_property** | [**ModelProperty**](ModelProperty.md)| PropertyPayload describes a property of a thing. No field is mandatory | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_v1_delete**
> properties_v1_delete(id, pid, force=force)

delete properties_v1

Removes a property associated to a thing

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
api_instance = iot_api_client.PropertiesV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
pid = 'pid_example' # str | The id of the property
force = False # bool | If true, hard delete the property (optional) (default to False)

try:
    # delete properties_v1
    api_instance.properties_v1_delete(id, pid, force=force)
except ApiException as e:
    print("Exception when calling PropertiesV1Api->properties_v1_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **pid** | **str**| The id of the property | 
 **force** | **bool**| If true, hard delete the property | [optional] [default to False]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_v1_list**
> list[ArduinoProperty] properties_v1_list(id, show_deleted=show_deleted)

list properties_v1

Returns the list of properties associated to the thing

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
api_instance = iot_api_client.PropertiesV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
show_deleted = False # bool | If true, shows the soft deleted properties (optional) (default to False)

try:
    # list properties_v1
    api_response = api_instance.properties_v1_list(id, show_deleted=show_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertiesV1Api->properties_v1_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **show_deleted** | **bool**| If true, shows the soft deleted properties | [optional] [default to False]

### Return type

[**list[ArduinoProperty]**](ArduinoProperty.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_v1_publish**
> properties_v1_publish(id, pid, property_value)

publish properties_v1

Publish a property value to MQTT

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
api_instance = iot_api_client.PropertiesV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
pid = 'pid_example' # str | The id of the property
property_value = iot_api_client.PropertyValue() # PropertyValue | PropertyValuePayload describes a property value

try:
    # publish properties_v1
    api_instance.properties_v1_publish(id, pid, property_value)
except ApiException as e:
    print("Exception when calling PropertiesV1Api->properties_v1_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **pid** | **str**| The id of the property | 
 **property_value** | [**PropertyValue**](PropertyValue.md)| PropertyValuePayload describes a property value | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_v1_show**
> ArduinoProperty properties_v1_show(id, pid, show_deleted=show_deleted)

show properties_v1

Returns the property requested by the user

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
api_instance = iot_api_client.PropertiesV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
pid = 'pid_example' # str | The id of the property
show_deleted = False # bool | If true, shows the soft deleted properties (optional) (default to False)

try:
    # show properties_v1
    api_response = api_instance.properties_v1_show(id, pid, show_deleted=show_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertiesV1Api->properties_v1_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **pid** | **str**| The id of the property | 
 **show_deleted** | **bool**| If true, shows the soft deleted properties | [optional] [default to False]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **properties_v1_update**
> ArduinoProperty properties_v1_update(id, pid, model_property)

update properties_v1

Updates a property associated to a thing

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
api_instance = iot_api_client.PropertiesV1Api(iot_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
pid = 'pid_example' # str | The id of the property
model_property = iot_api_client.ModelProperty() # ModelProperty | PropertyPayload describes a property of a thing. No field is mandatory

try:
    # update properties_v1
    api_response = api_instance.properties_v1_update(id, pid, model_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertiesV1Api->properties_v1_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the thing | 
 **pid** | **str**| The id of the property | 
 **model_property** | [**ModelProperty**](ModelProperty.md)| PropertyPayload describes a property of a thing. No field is mandatory | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# arduino_iot_rest.PropertiesV2Api

All URIs are relative to *http://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**properties_v2_create**](PropertiesV2Api.md#properties_v2_create) | **PUT** /v2/things/{id}/properties | create properties_v2
[**properties_v2_delete**](PropertiesV2Api.md#properties_v2_delete) | **DELETE** /v2/things/{id}/properties/{pid} | delete properties_v2
[**properties_v2_list**](PropertiesV2Api.md#properties_v2_list) | **GET** /v2/things/{id}/properties | list properties_v2
[**properties_v2_publish**](PropertiesV2Api.md#properties_v2_publish) | **PUT** /v2/things/{id}/properties/{pid}/publish | publish properties_v2
[**properties_v2_show**](PropertiesV2Api.md#properties_v2_show) | **GET** /v2/things/{id}/properties/{pid} | show properties_v2
[**properties_v2_update**](PropertiesV2Api.md#properties_v2_update) | **POST** /v2/things/{id}/properties/{pid} | update properties_v2


# **properties_v2_create**
> ArduinoProperty properties_v2_create(id, model_property)

create properties_v2

Creates a new property associated to a thing

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import arduino_iot_rest
from arduino_iot_rest.rest import ApiException
from pprint import pprint
configuration = arduino_iot_rest.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api2.arduino.cc/iot
configuration.host = "http://api2.arduino.cc/iot"
# Create an instance of the API class
api_instance = arduino_iot_rest.PropertiesV2Api(arduino_iot_rest.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
model_property = arduino_iot_rest.ModelProperty() # ModelProperty | PropertyPayload describes a property of a thing. No field is mandatory

try:
    # create properties_v2
    api_response = api_instance.properties_v2_create(id, model_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertiesV2Api->properties_v2_create: %s\n" % e)
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

# **properties_v2_delete**
> properties_v2_delete(id, pid, force=force)

delete properties_v2

Removes a property associated to a thing

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import arduino_iot_rest
from arduino_iot_rest.rest import ApiException
from pprint import pprint
configuration = arduino_iot_rest.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api2.arduino.cc/iot
configuration.host = "http://api2.arduino.cc/iot"
# Create an instance of the API class
api_instance = arduino_iot_rest.PropertiesV2Api(arduino_iot_rest.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
pid = 'pid_example' # str | The id of the property
force = False # bool | If true, hard delete the property (optional) (default to False)

try:
    # delete properties_v2
    api_instance.properties_v2_delete(id, pid, force=force)
except ApiException as e:
    print("Exception when calling PropertiesV2Api->properties_v2_delete: %s\n" % e)
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

# **properties_v2_list**
> list[ArduinoProperty] properties_v2_list(id, show_deleted=show_deleted)

list properties_v2

Returns the list of properties associated to the thing

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import arduino_iot_rest
from arduino_iot_rest.rest import ApiException
from pprint import pprint
configuration = arduino_iot_rest.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api2.arduino.cc/iot
configuration.host = "http://api2.arduino.cc/iot"
# Create an instance of the API class
api_instance = arduino_iot_rest.PropertiesV2Api(arduino_iot_rest.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
show_deleted = False # bool | If true, shows the soft deleted properties (optional) (default to False)

try:
    # list properties_v2
    api_response = api_instance.properties_v2_list(id, show_deleted=show_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertiesV2Api->properties_v2_list: %s\n" % e)
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

# **properties_v2_publish**
> properties_v2_publish(id, pid, property_value)

publish properties_v2

Publish a property value to MQTT

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import arduino_iot_rest
from arduino_iot_rest.rest import ApiException
from pprint import pprint
configuration = arduino_iot_rest.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api2.arduino.cc/iot
configuration.host = "http://api2.arduino.cc/iot"
# Create an instance of the API class
api_instance = arduino_iot_rest.PropertiesV2Api(arduino_iot_rest.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
pid = 'pid_example' # str | The id of the property
property_value = arduino_iot_rest.PropertyValue() # PropertyValue | PropertyValuePayload describes a property value

try:
    # publish properties_v2
    api_instance.properties_v2_publish(id, pid, property_value)
except ApiException as e:
    print("Exception when calling PropertiesV2Api->properties_v2_publish: %s\n" % e)
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

# **properties_v2_show**
> ArduinoProperty properties_v2_show(id, pid, show_deleted=show_deleted)

show properties_v2

Returns the property requested by the user

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import arduino_iot_rest
from arduino_iot_rest.rest import ApiException
from pprint import pprint
configuration = arduino_iot_rest.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api2.arduino.cc/iot
configuration.host = "http://api2.arduino.cc/iot"
# Create an instance of the API class
api_instance = arduino_iot_rest.PropertiesV2Api(arduino_iot_rest.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
pid = 'pid_example' # str | The id of the property
show_deleted = False # bool | If true, shows the soft deleted properties (optional) (default to False)

try:
    # show properties_v2
    api_response = api_instance.properties_v2_show(id, pid, show_deleted=show_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertiesV2Api->properties_v2_show: %s\n" % e)
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

# **properties_v2_update**
> ArduinoProperty properties_v2_update(id, pid, model_property)

update properties_v2

Updates a property associated to a thing

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import arduino_iot_rest
from arduino_iot_rest.rest import ApiException
from pprint import pprint
configuration = arduino_iot_rest.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://api2.arduino.cc/iot
configuration.host = "http://api2.arduino.cc/iot"
# Create an instance of the API class
api_instance = arduino_iot_rest.PropertiesV2Api(arduino_iot_rest.ApiClient(configuration))
id = 'id_example' # str | The id of the thing
pid = 'pid_example' # str | The id of the property
model_property = arduino_iot_rest.ModelProperty() # ModelProperty | PropertyPayload describes a property of a thing. No field is mandatory

try:
    # update properties_v2
    api_response = api_instance.properties_v2_update(id, pid, model_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertiesV2Api->properties_v2_update: %s\n" % e)
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


# iot_api_client.TriggersV1Api

All URIs are relative to *https://api2.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actions_v1_create**](TriggersV1Api.md#actions_v1_create) | **POST** /iot/v1/actions | create actions_v1
[**actions_v1_delete**](TriggersV1Api.md#actions_v1_delete) | **DELETE** /iot/v1/actions/{id} | delete actions_v1
[**actions_v1_list**](TriggersV1Api.md#actions_v1_list) | **GET** /iot/v1/actions | list actions_v1
[**actions_v1_show**](TriggersV1Api.md#actions_v1_show) | **GET** /iot/v1/actions/{id} | show actions_v1
[**actions_v1_update**](TriggersV1Api.md#actions_v1_update) | **PUT** /iot/v1/actions/{id} | update actions_v1
[**triggers_v1_create**](TriggersV1Api.md#triggers_v1_create) | **PUT** /iot/v1/triggers | create triggers_v1
[**triggers_v1_delete**](TriggersV1Api.md#triggers_v1_delete) | **DELETE** /iot/v1/triggers/{id} | delete triggers_v1
[**triggers_v1_list**](TriggersV1Api.md#triggers_v1_list) | **GET** /iot/v1/triggers | list triggers_v1
[**triggers_v1_patch**](TriggersV1Api.md#triggers_v1_patch) | **PATCH** /iot/v1/triggers/{id} | patch triggers_v1
[**triggers_v1_show**](TriggersV1Api.md#triggers_v1_show) | **GET** /iot/v1/triggers/{id} | show triggers_v1
[**triggers_v1_template**](TriggersV1Api.md#triggers_v1_template) | **GET** /iot/v1/triggers/{id}/template | template triggers_v1
[**triggers_v1_update**](TriggersV1Api.md#triggers_v1_update) | **POST** /iot/v1/triggers/{id} | update triggers_v1


# **actions_v1_create**
> ArduinoAction actions_v1_create(create_action, x_organization=x_organization)

create actions_v1

Creates a new action

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_action import ArduinoAction
from iot_api_client.models.create_action import CreateAction
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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    create_action = iot_api_client.CreateAction() # CreateAction | 
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # create actions_v1
        api_response = api_instance.actions_v1_create(create_action, x_organization=x_organization)
        print("The response of TriggersV1Api->actions_v1_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersV1Api->actions_v1_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_action** | [**CreateAction**](CreateAction.md)|  | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoAction**](ArduinoAction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.action+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_v1_delete**
> actions_v1_delete(id, x_organization=x_organization)

delete actions_v1

Removes an action

### Example

* Bearer (JWT) Authentication (oauth2):

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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    id = 'id_example' # str | The id of the action
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # delete actions_v1
        api_instance.actions_v1_delete(id, x_organization=x_organization)
    except Exception as e:
        print("Exception when calling TriggersV1Api->actions_v1_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the action | 
 **x_organization** | **str**|  | [optional] 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_v1_list**
> List[ArduinoAction] actions_v1_list(x_organization=x_organization)

list actions_v1

Returns the list of actions

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_action import ArduinoAction
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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # list actions_v1
        api_response = api_instance.actions_v1_list(x_organization=x_organization)
        print("The response of TriggersV1Api->actions_v1_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersV1Api->actions_v1_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_organization** | **str**|  | [optional] 

### Return type

[**List[ArduinoAction]**](ArduinoAction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.action+json; type=collection, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_v1_show**
> ArduinoAction actions_v1_show(id, x_organization=x_organization)

show actions_v1

Returns an action

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_action import ArduinoAction
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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    id = 'id_example' # str | The id of the action
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # show actions_v1
        api_response = api_instance.actions_v1_show(id, x_organization=x_organization)
        print("The response of TriggersV1Api->actions_v1_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersV1Api->actions_v1_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the action | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoAction**](ArduinoAction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.action+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_v1_update**
> ArduinoAction actions_v1_update(id, update_action, x_organization=x_organization)

update actions_v1

Updates an action

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_action import ArduinoAction
from iot_api_client.models.update_action import UpdateAction
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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    id = 'id_example' # str | The id of the action
    update_action = iot_api_client.UpdateAction() # UpdateAction | 
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # update actions_v1
        api_response = api_instance.actions_v1_update(id, update_action, x_organization=x_organization)
        print("The response of TriggersV1Api->actions_v1_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersV1Api->actions_v1_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the action | 
 **update_action** | [**UpdateAction**](UpdateAction.md)|  | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoAction**](ArduinoAction.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.action+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_v1_create**
> ArduinoTrigger triggers_v1_create(trigger, x_organization=x_organization)

create triggers_v1

Creates a new trigger

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_trigger import ArduinoTrigger
from iot_api_client.models.trigger import Trigger
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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    trigger = iot_api_client.Trigger() # Trigger | 
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # create triggers_v1
        api_response = api_instance.triggers_v1_create(trigger, x_organization=x_organization)
        print("The response of TriggersV1Api->triggers_v1_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersV1Api->triggers_v1_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger** | [**Trigger**](Trigger.md)|  | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoTrigger**](ArduinoTrigger.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.trigger+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_v1_delete**
> triggers_v1_delete(id, force=force, x_organization=x_organization)

delete triggers_v1

Removes a trigger

### Example

* Bearer (JWT) Authentication (oauth2):

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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    id = 'id_example' # str | The id of the trigger
    force = False # bool | If true, hard delete the trigger (optional) (default to False)
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # delete triggers_v1
        api_instance.triggers_v1_delete(id, force=force, x_organization=x_organization)
    except Exception as e:
        print("Exception when calling TriggersV1Api->triggers_v1_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the trigger | 
 **force** | **bool**| If true, hard delete the trigger | [optional] [default to False]
 **x_organization** | **str**|  | [optional] 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_v1_list**
> List[ArduinoTrigger] triggers_v1_list(device_id=device_id, property_id=property_id, show_deleted=show_deleted, source_type=source_type, x_organization=x_organization)

list triggers_v1

Returns the list of triggers

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_trigger import ArduinoTrigger
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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    device_id = 'device_id_example' # str | The id of the device associated with the triggers (mutually exclusive with 'property_id') (optional)
    property_id = 'property_id_example' # str | The id of the property associated with the triggers (mutually exclusive with 'device_id') (optional)
    show_deleted = False # bool | If true, shows the soft deleted triggers (optional) (default to False)
    source_type = 'source_type_example' # str | The source type of the trigger, could be PROPERTY, DEVICE_INCLUDE or DEVICE_EXCLUDE (optional)
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # list triggers_v1
        api_response = api_instance.triggers_v1_list(device_id=device_id, property_id=property_id, show_deleted=show_deleted, source_type=source_type, x_organization=x_organization)
        print("The response of TriggersV1Api->triggers_v1_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersV1Api->triggers_v1_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| The id of the device associated with the triggers (mutually exclusive with &#39;property_id&#39;) | [optional] 
 **property_id** | **str**| The id of the property associated with the triggers (mutually exclusive with &#39;device_id&#39;) | [optional] 
 **show_deleted** | **bool**| If true, shows the soft deleted triggers | [optional] [default to False]
 **source_type** | **str**| The source type of the trigger, could be PROPERTY, DEVICE_INCLUDE or DEVICE_EXCLUDE | [optional] 
 **x_organization** | **str**|  | [optional] 

### Return type

[**List[ArduinoTrigger]**](ArduinoTrigger.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.trigger+json; type=collection, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_v1_patch**
> ArduinoTrigger triggers_v1_patch(id, trigger, x_organization=x_organization)

patch triggers_v1

Patch a trigger

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_trigger import ArduinoTrigger
from iot_api_client.models.trigger import Trigger
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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    id = 'id_example' # str | The id of the trigger
    trigger = iot_api_client.Trigger() # Trigger | 
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # patch triggers_v1
        api_response = api_instance.triggers_v1_patch(id, trigger, x_organization=x_organization)
        print("The response of TriggersV1Api->triggers_v1_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersV1Api->triggers_v1_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the trigger | 
 **trigger** | [**Trigger**](Trigger.md)|  | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoTrigger**](ArduinoTrigger.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.trigger+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_v1_show**
> ArduinoTriggerWithLinkedEntities triggers_v1_show(id, x_organization=x_organization)

show triggers_v1

Returns a trigger

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_trigger_with_linked_entities import ArduinoTriggerWithLinkedEntities
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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    id = 'id_example' # str | The id of the trigger
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # show triggers_v1
        api_response = api_instance.triggers_v1_show(id, x_organization=x_organization)
        print("The response of TriggersV1Api->triggers_v1_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersV1Api->triggers_v1_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the trigger | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoTriggerWithLinkedEntities**](ArduinoTriggerWithLinkedEntities.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.trigger_with_linked_entities+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_v1_template**
> ArduinoTriggerTemplate triggers_v1_template(id, x_organization=x_organization)

template triggers_v1

Extract template from the given trigger

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_trigger_template import ArduinoTriggerTemplate
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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    id = 'id_example' # str | The id of the trigger
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # template triggers_v1
        api_response = api_instance.triggers_v1_template(id, x_organization=x_organization)
        print("The response of TriggersV1Api->triggers_v1_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersV1Api->triggers_v1_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the trigger | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoTriggerTemplate**](ArduinoTriggerTemplate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.arduino.trigger_template+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_v1_update**
> ArduinoTrigger triggers_v1_update(id, trigger, x_organization=x_organization)

update triggers_v1

Updates a trigger

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_trigger import ArduinoTrigger
from iot_api_client.models.trigger import Trigger
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

# Configure Bearer authorization (JWT): oauth2
configuration = iot_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TriggersV1Api(api_client)
    id = 'id_example' # str | The id of the trigger
    trigger = iot_api_client.Trigger() # Trigger | 
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # update triggers_v1
        api_response = api_instance.triggers_v1_update(id, trigger, x_organization=x_organization)
        print("The response of TriggersV1Api->triggers_v1_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersV1Api->triggers_v1_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the trigger | 
 **trigger** | [**Trigger**](Trigger.md)|  | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoTrigger**](ArduinoTrigger.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.trigger+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# iot_api_client.TemplatesApi

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**templates_apply**](TemplatesApi.md#templates_apply) | **PUT** /v1/templates | apply templates


# **templates_apply**
> ArduinoTemplate templates_apply(template, x_organization=x_organization)

apply templates

Apply an existing cloud template and generate all the needed resources

### Example


```python
import iot_api_client
from iot_api_client.models.arduino_template import ArduinoTemplate
from iot_api_client.models.template import Template
from iot_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)


# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iot_api_client.TemplatesApi(api_client)
    template = iot_api_client.Template() # Template | TemplatePayload describes the needed attribute to apply a template
    x_organization = 'x_organization_example' # str |  (optional)

    try:
        # apply templates
        api_response = api_instance.templates_apply(template, x_organization=x_organization)
        print("The response of TemplatesApi->templates_apply:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplatesApi->templates_apply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | [**Template**](Template.md)| TemplatePayload describes the needed attribute to apply a template | 
 **x_organization** | **str**|  | [optional] 

### Return type

[**ArduinoTemplate**](ArduinoTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/vnd.arduino.template+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


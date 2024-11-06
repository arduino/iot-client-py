# iot_api_client.DevicesV2OtaApi

All URIs are relative to *https://api2.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_ota_send**](DevicesV2OtaApi.md#devices_v2_ota_send) | **PUT** /iot/v2/devices/{id}/ota | send devices_v2_ota
[**devices_v2_ota_upload**](DevicesV2OtaApi.md#devices_v2_ota_upload) | **POST** /iot/v2/devices/{id}/ota | upload devices_v2_ota
[**devices_v2_ota_url**](DevicesV2OtaApi.md#devices_v2_ota_url) | **POST** /iot/v2/devices/{id}/ota/url | url devices_v2_ota


# **devices_v2_ota_send**
> devices_v2_ota_send(id, devicev2_otabinaryurl)

send devices_v2_ota

Send a binary url to a device

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.devicev2_otabinaryurl import Devicev2Otabinaryurl
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
    api_instance = iot_api_client.DevicesV2OtaApi(api_client)
    id = 'id_example' # str | The id of the device
    devicev2_otabinaryurl = iot_api_client.Devicev2Otabinaryurl() # Devicev2Otabinaryurl | 

    try:
        # send devices_v2_ota
        api_instance.devices_v2_ota_send(id, devicev2_otabinaryurl)
    except Exception as e:
        print("Exception when calling DevicesV2OtaApi->devices_v2_ota_send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **devicev2_otabinaryurl** | [**Devicev2Otabinaryurl**](Devicev2Otabinaryurl.md)|  | 

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
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**410** | Gone |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_ota_upload**
> ArduinoDevicev2Otaupload devices_v2_ota_upload(id, ota_file, var_async=var_async, expire_in_mins=expire_in_mins)

upload devices_v2_ota

Upload a binary and send it to a device

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.arduino_devicev2_otaupload import ArduinoDevicev2Otaupload
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
    api_instance = iot_api_client.DevicesV2OtaApi(api_client)
    id = 'id_example' # str | The id of the device
    ota_file = None # bytearray | OTA file
    var_async = True # bool | If false, wait for the full OTA process, until it gets a result from the device (optional) (default to True)
    expire_in_mins = 10 # int | Binary expire time in minutes, default 10 mins (optional) (default to 10)

    try:
        # upload devices_v2_ota
        api_response = api_instance.devices_v2_ota_upload(id, ota_file, var_async=var_async, expire_in_mins=expire_in_mins)
        print("The response of DevicesV2OtaApi->devices_v2_ota_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesV2OtaApi->devices_v2_ota_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **ota_file** | **bytearray**| OTA file | 
 **var_async** | **bool**| If false, wait for the full OTA process, until it gets a result from the device | [optional] [default to True]
 **expire_in_mins** | **int**| Binary expire time in minutes, default 10 mins | [optional] [default to 10]

### Return type

[**ArduinoDevicev2Otaupload**](ArduinoDevicev2Otaupload.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/vnd.arduino.devicev2.otaupload+json, application/vnd.goa.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**410** | Gone |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_v2_ota_url**
> devices_v2_ota_url(id, devicev2_otaurlpyalod)

url devices_v2_ota

Generate a url for downloading a binary

### Example

* Bearer (JWT) Authentication (oauth2):

```python
import iot_api_client
from iot_api_client.models.devicev2_otaurlpyalod import Devicev2Otaurlpyalod
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
    api_instance = iot_api_client.DevicesV2OtaApi(api_client)
    id = 'id_example' # str | The id of the device
    devicev2_otaurlpyalod = iot_api_client.Devicev2Otaurlpyalod() # Devicev2Otaurlpyalod | 

    try:
        # url devices_v2_ota
        api_instance.devices_v2_ota_url(id, devicev2_otaurlpyalod)
    except Exception as e:
        print("Exception when calling DevicesV2OtaApi->devices_v2_ota_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **devicev2_otaurlpyalod** | [**Devicev2Otaurlpyalod**](Devicev2Otaurlpyalod.md)|  | 

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
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**410** | Gone |  -  |
**412** | Precondition Failed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


<a name="__pageTop"></a>
# iot_api_client.apis.tags.devices_v2_certs_api.DevicesV2CertsApi

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_certs_create**](#devices_v2_certs_create) | **put** /v2/devices/{id}/certs | create devices_v2_certs
[**devices_v2_certs_delete**](#devices_v2_certs_delete) | **delete** /v2/devices/{id}/certs/{cid} | delete devices_v2_certs
[**devices_v2_certs_list**](#devices_v2_certs_list) | **get** /v2/devices/{id}/certs | list devices_v2_certs
[**devices_v2_certs_show**](#devices_v2_certs_show) | **get** /v2/devices/{id}/certs/{cid} | show devices_v2_certs
[**devices_v2_certs_update**](#devices_v2_certs_update) | **post** /v2/devices/{id}/certs/{cid} | update devices_v2_certs

# **devices_v2_certs_create**
<a name="devices_v2_certs_create"></a>
> ArduinoDevicev2Cert devices_v2_certs_create(idcreate_devices_v2_certs_payload)

create devices_v2_certs

Creates a new cert associated to a device. The csr is signed and saved in database. The CommonName will be replaced with the device id.

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_certs_api
from iot_api_client.model.arduino_devicev2_cert import ArduinoDevicev2Cert
from iot_api_client.model.error import Error
from iot_api_client.model.create_devices_v2_certs_payload import CreateDevicesV2CertsPayload
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_certs_api.DevicesV2CertsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = CreateDevicesV2CertsPayload(
        ca="ca_example",
        csr="-----BEGIN CERTIFICATE-----\n\t\t\tMIIBeDCCAR4CAQAwgY0xCzAJBgNVBAYTAkFVMRMwEQYDVQQIEwpTb21lLVN0YXRl\n\t\t\tMQ8wDQYDVQQHEwZNeUNpdHkxFDASBgNVBAoTC0NvbXBhbnkgTHRkMQswCQYDVQQL\n\t\t\tEwJJVDEUMBIGA1UEAxMLZXhhbXBsZS5jb20xHzAdBgkqhkiG9w0BCQEMEHRlc3RA\n\t\t\tZXhhbXBsZS5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATf6J9Gk79XGJ2I\n\t\t\t+v6p/r0UmPufUcUwtlx7gx87+DaI8Vpj9R5KN71HsHYw5uq+Lm0cr0CZIdtZU4cP\n\t\t\tupd6jDQToC4wLAYJKoZIhvcNAQkOMR8wHTAbBgNVHREEFDASgRB0ZXN0QGV4YW1w\n\t\t\tbGUuY29tMAoGCCqGSM49BAMCA0gAMEUCIGQqtlGzYdjPwYZYJ41albMBcdrKI7+8\n\t\t\toiNSNWyDxJSGAiEAqQPPxMdr6vaXCCjr5s1J01WLKHzGoPFCR40rqAPs8eQ=\n\t\t\t-----END CERTIFICATE-----\n\t\t\t",
        enabled=True,
    )
    try:
        # create devices_v2_certs
        api_response = api_instance.devices_v2_certs_create(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2CertsApi->devices_v2_certs_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDevicesV2CertsPayload**](../../models/CreateDevicesV2CertsPayload.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDevicesV2CertsPayload**](../../models/CreateDevicesV2CertsPayload.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#devices_v2_certs_create.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#devices_v2_certs_create.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#devices_v2_certs_create.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#devices_v2_certs_create.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#devices_v2_certs_create.ApiResponseFor500) | Internal Server Error

#### devices_v2_certs_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2Cert**](../../models/ArduinoDevicev2Cert.md) |  | 


#### devices_v2_certs_create.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_certs_create.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_certs_create.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_certs_create.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_certs_delete**
<a name="devices_v2_certs_delete"></a>
> devices_v2_certs_delete(cidid)

delete devices_v2_certs

Removes a cert associated to a device

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_certs_api
from iot_api_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_certs_api.DevicesV2CertsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'cid': "cid_example",
        'id': "id_example",
    }
    try:
        # delete devices_v2_certs
        api_response = api_instance.devices_v2_certs_delete(
            path_params=path_params,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2CertsApi->devices_v2_certs_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cid | CidSchema | | 
id | IdSchema | | 

# CidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_certs_delete.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#devices_v2_certs_delete.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#devices_v2_certs_delete.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#devices_v2_certs_delete.ApiResponseFor500) | Internal Server Error

#### devices_v2_certs_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_certs_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_certs_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_certs_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_certs_list**
<a name="devices_v2_certs_list"></a>
> ArduinoDevicev2CertCollection devices_v2_certs_list(id)

list devices_v2_certs

Returns the list of certs associated to the device

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_certs_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_devicev2_cert_collection import ArduinoDevicev2CertCollection
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_certs_api.DevicesV2CertsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # list devices_v2_certs
        api_response = api_instance.devices_v2_certs_list(
            path_params=path_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2CertsApi->devices_v2_certs_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_certs_list.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#devices_v2_certs_list.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#devices_v2_certs_list.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#devices_v2_certs_list.ApiResponseFor500) | Internal Server Error

#### devices_v2_certs_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2CertCollection**](../../models/ArduinoDevicev2CertCollection.md) |  | 


#### devices_v2_certs_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_certs_list.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_certs_list.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_certs_show**
<a name="devices_v2_certs_show"></a>
> ArduinoDevicev2Cert devices_v2_certs_show(cidid)

show devices_v2_certs

Returns the cert requested by the user

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_certs_api
from iot_api_client.model.arduino_devicev2_cert import ArduinoDevicev2Cert
from iot_api_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_certs_api.DevicesV2CertsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'cid': "cid_example",
        'id': "id_example",
    }
    try:
        # show devices_v2_certs
        api_response = api_instance.devices_v2_certs_show(
            path_params=path_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2CertsApi->devices_v2_certs_show: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cid | CidSchema | | 
id | IdSchema | | 

# CidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_certs_show.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#devices_v2_certs_show.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#devices_v2_certs_show.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#devices_v2_certs_show.ApiResponseFor500) | Internal Server Error

#### devices_v2_certs_show.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2Cert**](../../models/ArduinoDevicev2Cert.md) |  | 


#### devices_v2_certs_show.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_certs_show.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_certs_show.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_certs_update**
<a name="devices_v2_certs_update"></a>
> ArduinoDevicev2Cert devices_v2_certs_update(cididdevicev2_cert)

update devices_v2_certs

Updates a cert associated to a device. The csr is signed and saved in database. The CommonName will be replaced with the device id.

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_certs_api
from iot_api_client.model.arduino_devicev2_cert import ArduinoDevicev2Cert
from iot_api_client.model.error import Error
from iot_api_client.model.devicev2_cert import Devicev2Cert
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_certs_api.DevicesV2CertsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'cid': "cid_example",
        'id': "id_example",
    }
    body = Devicev2Cert(
        ca="ca_example",
        csr="-----BEGIN CERTIFICATE-----\n\t\t\tMIIBeDCCAR4CAQAwgY0xCzAJBgNVBAYTAkFVMRMwEQYDVQQIEwpTb21lLVN0YXRl\n\t\t\tMQ8wDQYDVQQHEwZNeUNpdHkxFDASBgNVBAoTC0NvbXBhbnkgTHRkMQswCQYDVQQL\n\t\t\tEwJJVDEUMBIGA1UEAxMLZXhhbXBsZS5jb20xHzAdBgkqhkiG9w0BCQEMEHRlc3RA\n\t\t\tZXhhbXBsZS5jb20wWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATf6J9Gk79XGJ2I\n\t\t\t+v6p/r0UmPufUcUwtlx7gx87+DaI8Vpj9R5KN71HsHYw5uq+Lm0cr0CZIdtZU4cP\n\t\t\tupd6jDQToC4wLAYJKoZIhvcNAQkOMR8wHTAbBgNVHREEFDASgRB0ZXN0QGV4YW1w\n\t\t\tbGUuY29tMAoGCCqGSM49BAMCA0gAMEUCIGQqtlGzYdjPwYZYJ41albMBcdrKI7+8\n\t\t\toiNSNWyDxJSGAiEAqQPPxMdr6vaXCCjr5s1J01WLKHzGoPFCR40rqAPs8eQ=\n\t\t\t-----END CERTIFICATE-----\n\t\t\t",
        enabled=True,
    )
    try:
        # update devices_v2_certs
        api_response = api_instance.devices_v2_certs_update(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2CertsApi->devices_v2_certs_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Devicev2Cert**](../../models/Devicev2Cert.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**Devicev2Cert**](../../models/Devicev2Cert.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cid | CidSchema | | 
id | IdSchema | | 

# CidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_certs_update.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#devices_v2_certs_update.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#devices_v2_certs_update.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#devices_v2_certs_update.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#devices_v2_certs_update.ApiResponseFor500) | Internal Server Error

#### devices_v2_certs_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2Cert**](../../models/ArduinoDevicev2Cert.md) |  | 


#### devices_v2_certs_update.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_certs_update.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_certs_update.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_certs_update.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


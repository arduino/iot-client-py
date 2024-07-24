<a name="__pageTop"></a>
# iot_api_client.apis.tags.series_v2_api.SeriesV2Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**series_v2_batch_query**](#series_v2_batch_query) | **post** /v2/series/batch_query | batch_query series_v2
[**series_v2_batch_query_raw**](#series_v2_batch_query_raw) | **post** /v2/series/batch_query_raw | batch_query_raw series_v2
[**series_v2_batch_query_raw_last_value**](#series_v2_batch_query_raw_last_value) | **post** /v2/series/batch_query_raw/lastvalue | batch_query_raw_last_value series_v2
[**series_v2_batch_query_sampling**](#series_v2_batch_query_sampling) | **post** /v2/series/batch_query_sampling | batch_query_sampling series_v2
[**series_v2_historic_data**](#series_v2_historic_data) | **post** /v2/series/historic_data | historic_data series_v2

# **series_v2_batch_query**
<a name="series_v2_batch_query"></a>
> ArduinoSeriesBatch series_v2_batch_query(batch_query_requests_media_v1)

batch_query series_v2

Returns the batch of time-series aggregated samples

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import series_v2_api
from iot_api_client.model.batch_query_requests_media_v1 import BatchQueryRequestsMediaV1
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_series_batch import ArduinoSeriesBatch
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
    api_instance = series_v2_api.SeriesV2Api(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = BatchQueryRequestsMediaV1(
        requests=[
            BatchQueryRequestMediaV1(
                aggregation="AVG",
                _from="1970-01-01T00:00:00.00Z",
                interval=1,
                q="q_example",
                series_limit=1,
                to="1970-01-01T00:00:00.00Z",
            )
        ],
        resp_version=1,
    )
    try:
        # batch_query series_v2
        api_response = api_instance.series_v2_batch_query(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling SeriesV2Api->series_v2_batch_query: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = BatchQueryRequestsMediaV1(
        requests=[
            BatchQueryRequestMediaV1(
                aggregation="AVG",
                _from="1970-01-01T00:00:00.00Z",
                interval=1,
                q="q_example",
                series_limit=1,
                to="1970-01-01T00:00:00.00Z",
            )
        ],
        resp_version=1,
    )
    try:
        # batch_query series_v2
        api_response = api_instance.series_v2_batch_query(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling SeriesV2Api->series_v2_batch_query: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.series.batch+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchQueryRequestsMediaV1**](../../models/BatchQueryRequestsMediaV1.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchQueryRequestsMediaV1**](../../models/BatchQueryRequestsMediaV1.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#series_v2_batch_query.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#series_v2_batch_query.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#series_v2_batch_query.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#series_v2_batch_query.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#series_v2_batch_query.ApiResponseFor501) | Not Implemented
503 | [ApiResponseFor503](#series_v2_batch_query.ApiResponseFor503) | Service Unavailable

#### series_v2_batch_query.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoSeriesBatchjson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoSeriesBatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoSeriesBatch**](../../models/ArduinoSeriesBatch.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoSeriesBatch**](../../models/ArduinoSeriesBatch.md) |  | 


#### series_v2_batch_query.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndArduinoSeriesBatchjson, SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndArduinoSeriesBatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### series_v2_batch_query.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoSeriesBatchjson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoSeriesBatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### series_v2_batch_query.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### series_v2_batch_query.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### series_v2_batch_query.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationVndArduinoSeriesBatchjson, SchemaFor503ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationVndArduinoSeriesBatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor503ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **series_v2_batch_query_raw**
<a name="series_v2_batch_query_raw"></a>
> ArduinoSeriesRawBatch series_v2_batch_query_raw(batch_query_raw_requests_media_v1)

batch_query_raw series_v2

Returns the batch of time-series raw samples

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import series_v2_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_series_raw_batch import ArduinoSeriesRawBatch
from iot_api_client.model.batch_query_raw_requests_media_v1 import BatchQueryRawRequestsMediaV1
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
    api_instance = series_v2_api.SeriesV2Api(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = BatchQueryRawRequestsMediaV1(
        requests=[
            BatchQueryRawRequestMediaV1(
                _from="1970-01-01T00:00:00.00Z",
                q="q_example",
                series_limit=1,
                sort="DESC",
                to="1970-01-01T00:00:00.00Z",
            )
        ],
        resp_version=1,
    )
    try:
        # batch_query_raw series_v2
        api_response = api_instance.series_v2_batch_query_raw(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling SeriesV2Api->series_v2_batch_query_raw: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = BatchQueryRawRequestsMediaV1(
        requests=[
            BatchQueryRawRequestMediaV1(
                _from="1970-01-01T00:00:00.00Z",
                q="q_example",
                series_limit=1,
                sort="DESC",
                to="1970-01-01T00:00:00.00Z",
            )
        ],
        resp_version=1,
    )
    try:
        # batch_query_raw series_v2
        api_response = api_instance.series_v2_batch_query_raw(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling SeriesV2Api->series_v2_batch_query_raw: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.series.raw.batch+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchQueryRawRequestsMediaV1**](../../models/BatchQueryRawRequestsMediaV1.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchQueryRawRequestsMediaV1**](../../models/BatchQueryRawRequestsMediaV1.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#series_v2_batch_query_raw.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#series_v2_batch_query_raw.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#series_v2_batch_query_raw.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#series_v2_batch_query_raw.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#series_v2_batch_query_raw.ApiResponseFor501) | Not Implemented
503 | [ApiResponseFor503](#series_v2_batch_query_raw.ApiResponseFor503) | Service Unavailable

#### series_v2_batch_query_raw.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoSeriesRawBatchjson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoSeriesRawBatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoSeriesRawBatch**](../../models/ArduinoSeriesRawBatch.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoSeriesRawBatch**](../../models/ArduinoSeriesRawBatch.md) |  | 


#### series_v2_batch_query_raw.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndArduinoSeriesRawBatchjson, SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndArduinoSeriesRawBatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### series_v2_batch_query_raw.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoSeriesRawBatchjson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoSeriesRawBatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### series_v2_batch_query_raw.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### series_v2_batch_query_raw.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### series_v2_batch_query_raw.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationVndArduinoSeriesRawBatchjson, SchemaFor503ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationVndArduinoSeriesRawBatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor503ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **series_v2_batch_query_raw_last_value**
<a name="series_v2_batch_query_raw_last_value"></a>
> ArduinoSeriesRawBatchLastvalue series_v2_batch_query_raw_last_value(batch_last_value_requests_media_v1)

batch_query_raw_last_value series_v2

Returns the batch of time-series data raw

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import series_v2_api
from iot_api_client.model.batch_last_value_requests_media_v1 import BatchLastValueRequestsMediaV1
from iot_api_client.model.arduino_series_raw_batch_lastvalue import ArduinoSeriesRawBatchLastvalue
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
    api_instance = series_v2_api.SeriesV2Api(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = BatchLastValueRequestsMediaV1(
        requests=[
            BatchQueryRawLastValueRequestMediaV1(
                property_id="property_id_example",
                thing_id="thing_id_example",
            )
        ],
    )
    try:
        # batch_query_raw_last_value series_v2
        api_response = api_instance.series_v2_batch_query_raw_last_value(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling SeriesV2Api->series_v2_batch_query_raw_last_value: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = BatchLastValueRequestsMediaV1(
        requests=[
            BatchQueryRawLastValueRequestMediaV1(
                property_id="property_id_example",
                thing_id="thing_id_example",
            )
        ],
    )
    try:
        # batch_query_raw_last_value series_v2
        api_response = api_instance.series_v2_batch_query_raw_last_value(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling SeriesV2Api->series_v2_batch_query_raw_last_value: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.series.raw.batch.lastvalue+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchLastValueRequestsMediaV1**](../../models/BatchLastValueRequestsMediaV1.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchLastValueRequestsMediaV1**](../../models/BatchLastValueRequestsMediaV1.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#series_v2_batch_query_raw_last_value.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#series_v2_batch_query_raw_last_value.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#series_v2_batch_query_raw_last_value.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#series_v2_batch_query_raw_last_value.ApiResponseFor501) | Not Implemented
503 | [ApiResponseFor503](#series_v2_batch_query_raw_last_value.ApiResponseFor503) | Service Unavailable

#### series_v2_batch_query_raw_last_value.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoSeriesRawBatchLastvaluejson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoSeriesRawBatchLastvaluejson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoSeriesRawBatchLastvalue**](../../models/ArduinoSeriesRawBatchLastvalue.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoSeriesRawBatchLastvalue**](../../models/ArduinoSeriesRawBatchLastvalue.md) |  | 


#### series_v2_batch_query_raw_last_value.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoSeriesRawBatchLastvaluejson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoSeriesRawBatchLastvaluejson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### series_v2_batch_query_raw_last_value.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### series_v2_batch_query_raw_last_value.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### series_v2_batch_query_raw_last_value.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationVndArduinoSeriesRawBatchLastvaluejson, SchemaFor503ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationVndArduinoSeriesRawBatchLastvaluejson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor503ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **series_v2_batch_query_sampling**
<a name="series_v2_batch_query_sampling"></a>
> ArduinoSeriesBatchSampled series_v2_batch_query_sampling(batch_query_sampled_requests_media_v1)

batch_query_sampling series_v2

Returns a batch of time-series sampled samples. To be used for types that does not support mathematic aggregation. Types supported: strings, complex types.

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import series_v2_api
from iot_api_client.model.batch_query_sampled_requests_media_v1 import BatchQuerySampledRequestsMediaV1
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_series_batch_sampled import ArduinoSeriesBatchSampled
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
    api_instance = series_v2_api.SeriesV2Api(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = BatchQuerySampledRequestsMediaV1(
        requests=[
            BatchQuerySampledRequestMediaV1(
                _from="1970-01-01T00:00:00.00Z",
                interval=300,
                q="q_example",
                series_limit=1,
                to="1970-01-01T00:00:00.00Z",
            )
        ],
        resp_version=1,
    )
    try:
        # batch_query_sampling series_v2
        api_response = api_instance.series_v2_batch_query_sampling(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling SeriesV2Api->series_v2_batch_query_sampling: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = BatchQuerySampledRequestsMediaV1(
        requests=[
            BatchQuerySampledRequestMediaV1(
                _from="1970-01-01T00:00:00.00Z",
                interval=300,
                q="q_example",
                series_limit=1,
                to="1970-01-01T00:00:00.00Z",
            )
        ],
        resp_version=1,
    )
    try:
        # batch_query_sampling series_v2
        api_response = api_instance.series_v2_batch_query_sampling(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling SeriesV2Api->series_v2_batch_query_sampling: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.series.batch.sampled+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchQuerySampledRequestsMediaV1**](../../models/BatchQuerySampledRequestsMediaV1.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**BatchQuerySampledRequestsMediaV1**](../../models/BatchQuerySampledRequestsMediaV1.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#series_v2_batch_query_sampling.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#series_v2_batch_query_sampling.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#series_v2_batch_query_sampling.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#series_v2_batch_query_sampling.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#series_v2_batch_query_sampling.ApiResponseFor501) | Not Implemented
503 | [ApiResponseFor503](#series_v2_batch_query_sampling.ApiResponseFor503) | Service Unavailable

#### series_v2_batch_query_sampling.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoSeriesBatchSampledjson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoSeriesBatchSampledjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoSeriesBatchSampled**](../../models/ArduinoSeriesBatchSampled.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoSeriesBatchSampled**](../../models/ArduinoSeriesBatchSampled.md) |  | 


#### series_v2_batch_query_sampling.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndArduinoSeriesBatchSampledjson, SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndArduinoSeriesBatchSampledjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### series_v2_batch_query_sampling.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoSeriesBatchSampledjson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoSeriesBatchSampledjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### series_v2_batch_query_sampling.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### series_v2_batch_query_sampling.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### series_v2_batch_query_sampling.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationVndArduinoSeriesBatchSampledjson, SchemaFor503ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationVndArduinoSeriesBatchSampledjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor503ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **series_v2_historic_data**
<a name="series_v2_historic_data"></a>
> series_v2_historic_data(historic_data_request)

historic_data series_v2

Request sending of historical data of properties by email

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import series_v2_api
from iot_api_client.model.historic_data_request import HistoricDataRequest
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
    api_instance = series_v2_api.SeriesV2Api(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = HistoricDataRequest(
        _from="1970-01-01T00:00:00.00Z",
        properties=[
            "properties_example"
        ],
        to="1970-01-01T00:00:00.00Z",
    )
    try:
        # historic_data series_v2
        api_response = api_instance.series_v2_historic_data(
            header_params=header_params,
            body=body,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling SeriesV2Api->series_v2_historic_data: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = HistoricDataRequest(
        _from="1970-01-01T00:00:00.00Z",
        properties=[
            "properties_example"
        ],
        to="1970-01-01T00:00:00.00Z",
    )
    try:
        # historic_data series_v2
        api_response = api_instance.series_v2_historic_data(
            header_params=header_params,
            body=body,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling SeriesV2Api->series_v2_historic_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HistoricDataRequest**](../../models/HistoricDataRequest.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**HistoricDataRequest**](../../models/HistoricDataRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#series_v2_historic_data.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#series_v2_historic_data.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#series_v2_historic_data.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#series_v2_historic_data.ApiResponseFor500) | Internal Server Error

#### series_v2_historic_data.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### series_v2_historic_data.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### series_v2_historic_data.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### series_v2_historic_data.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


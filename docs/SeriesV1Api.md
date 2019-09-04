# iot_api_client.SeriesV1Api

All URIs are relative to *http://api-dev.arduino.cc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**series_v1_batch_query**](SeriesV1Api.md#series_v1_batch_query) | **POST** /v1/series/batch_query | batch_query series_v1
[**series_v1_batch_query_raw**](SeriesV1Api.md#series_v1_batch_query_raw) | **POST** /v1/series/batch_query_raw | batch_query_raw series_v1


# **series_v1_batch_query**
> ArduinoSeriesBatch series_v1_batch_query(batch_query_requests_media_v1)

batch_query series_v1

Returns the batch of time-series data

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
api_instance = iot_api_client.SeriesV1Api(iot_api_client.ApiClient(configuration))
batch_query_requests_media_v1 = iot_api_client.BatchQueryRequestsMediaV1() # BatchQueryRequestsMediaV1 | 

try:
    # batch_query series_v1
    api_response = api_instance.series_v1_batch_query(batch_query_requests_media_v1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeriesV1Api->series_v1_batch_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_query_requests_media_v1** | [**BatchQueryRequestsMediaV1**](BatchQueryRequestsMediaV1.md)|  | 

### Return type

[**ArduinoSeriesBatch**](ArduinoSeriesBatch.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.series.batch+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**501** | Not Implemented |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **series_v1_batch_query_raw**
> ArduinoSeriesRawBatch series_v1_batch_query_raw(batch_query_raw_requests_media_v1)

batch_query_raw series_v1

Returns the batch of time-series data raw

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
api_instance = iot_api_client.SeriesV1Api(iot_api_client.ApiClient(configuration))
batch_query_raw_requests_media_v1 = iot_api_client.BatchQueryRawRequestsMediaV1() # BatchQueryRawRequestsMediaV1 | 

try:
    # batch_query_raw series_v1
    api_response = api_instance.series_v1_batch_query_raw(batch_query_raw_requests_media_v1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SeriesV1Api->series_v1_batch_query_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_query_raw_requests_media_v1** | [**BatchQueryRawRequestsMediaV1**](BatchQueryRawRequestsMediaV1.md)|  | 

### Return type

[**ArduinoSeriesRawBatch**](ArduinoSeriesRawBatch.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.arduino.series.raw.batch+json, application/vnd.goa.error+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**501** | Not Implemented |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


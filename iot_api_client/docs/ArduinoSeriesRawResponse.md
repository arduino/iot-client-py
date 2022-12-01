# ArduinoSeriesRawResponse

ArduinoSeriesRawResponse media type (default view)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_values** | **int** | Total number of values in the array &#39;values&#39; | 
**from_date** | **datetime** | From date | 
**message** | **str** | If the response is different than &#39;ok&#39; | [optional] [default to '']
**query** | **str** | Query of for the data | 
**resp_version** | **int** | Response version | 
**series** | [**BatchQueryRawResponseSeriesMediaV1**](BatchQueryRawResponseSeriesMediaV1.md) |  | 
**series_limit** | **int** | Max of values | [optional] 
**sort** | **str** | Sorting | 
**status** | **str** | Status of the response | 
**times** | **list[datetime]** | Timestamp in RFC3339 | 
**to_date** | **datetime** | To date | 
**values** | **list[object]** | Values can be in Float, String, Bool, Object | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



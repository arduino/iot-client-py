# ArduinoSeriesRawResponse

ArduinoSeriesRawResponse media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_values** | **int** | Total number of values in the array &#39;values&#39; | 
**from_date** | **datetime** | From date | 
**message** | **str** | If the response is different than &#39;ok&#39; | [optional] [default to '']
**property_id** | **str** | Property id | [optional] 
**property_name** | **str** | Property name | [optional] 
**property_type** | **str** | Property type | [optional] 
**query** | **str** | Query of for the data | 
**resp_version** | **int** | Response version | 
**series** | [**BatchQueryRawResponseSeriesMediaV1**](BatchQueryRawResponseSeriesMediaV1.md) |  | 
**series_limit** | **int** | Max of values | [optional] 
**sort** | **str** | Sorting | 
**status** | **str** | Status of the response | 
**thing_id** | **str** | Thing id | [optional] 
**times** | **List[datetime]** | Timestamp in RFC3339 | 
**to_date** | **datetime** | To date | 
**values** | **List[object]** | Values can be in Float, String, Bool, Object | 

## Example

```python
from iot_api_client.models.arduino_series_raw_response import ArduinoSeriesRawResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoSeriesRawResponse from a JSON string
arduino_series_raw_response_instance = ArduinoSeriesRawResponse.from_json(json)
# print the JSON string representation of the object
print(ArduinoSeriesRawResponse.to_json())

# convert the object into a dict
arduino_series_raw_response_dict = arduino_series_raw_response_instance.to_dict()
# create an instance of ArduinoSeriesRawResponse from a dict
arduino_series_raw_response_from_dict = ArduinoSeriesRawResponse.from_dict(arduino_series_raw_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArduinoSeriesResponse

ArduinoSeriesResponse media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** | Aggregation statistic function. For numeric values, AVG statistic is used by default. PCT_X compute the Xth approximate percentile (e.g. PCT_95 is the 95th approximate percentile). For boolean, BOOL_OR statistic is used as default. | [optional] 
**count_values** | **int** | Total number of values in the array &#39;values&#39; | 
**from_date** | **datetime** | From date | 
**interval** | **int** | Resolution in seconds | 
**message** | **str** | If the response is different than &#39;ok&#39; | [optional] [default to '']
**property_id** | **str** | Property id | [optional] 
**property_name** | **str** | Property name | [optional] 
**property_type** | **str** | Property type | [optional] 
**query** | **str** | Query of for the data | 
**resp_version** | **int** | Response version | 
**series_limit** | **int** | Maximum number of values returned after data aggregation, if any | [optional] 
**status** | **str** | Status of the response | 
**thing_id** | **str** | Thing id | [optional] 
**times** | **List[datetime]** | Timestamp in RFC3339 | 
**to_date** | **datetime** | To date | 
**values** | **List[float]** | Values in Float | 

## Example

```python
from iot_api_client.models.arduino_series_response import ArduinoSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoSeriesResponse from a JSON string
arduino_series_response_instance = ArduinoSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(ArduinoSeriesResponse.to_json())

# convert the object into a dict
arduino_series_response_dict = arduino_series_response_instance.to_dict()
# create an instance of ArduinoSeriesResponse from a dict
arduino_series_response_from_dict = ArduinoSeriesResponse.from_dict(arduino_series_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



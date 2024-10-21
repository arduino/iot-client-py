# ArduinoSeriesRawLastValueResponse

ArduinoSeriesRawLastValueResponse media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_values** | **int** | Total number of values in the array &#39;values&#39; | 
**property_id** | **str** | Property id | 
**thing_id** | **str** | Thing id | 
**times** | **List[datetime]** | Timestamp in RFC3339 | 
**values** | **List[object]** | Values can be in Float, String, Bool, Object | 

## Example

```python
from iot_api_client.models.arduino_series_raw_last_value_response import ArduinoSeriesRawLastValueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoSeriesRawLastValueResponse from a JSON string
arduino_series_raw_last_value_response_instance = ArduinoSeriesRawLastValueResponse.from_json(json)
# print the JSON string representation of the object
print ArduinoSeriesRawLastValueResponse.to_json()

# convert the object into a dict
arduino_series_raw_last_value_response_dict = arduino_series_raw_last_value_response_instance.to_dict()
# create an instance of ArduinoSeriesRawLastValueResponse from a dict
arduino_series_raw_last_value_response_form_dict = arduino_series_raw_last_value_response.from_dict(arduino_series_raw_last_value_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



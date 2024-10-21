# ArduinoTimeseriesmedia

ArduinoTimeseriesmedia media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TimeseriesDataPoint]**](TimeseriesDataPoint.md) |  | 

## Example

```python
from iot_api_client.models.arduino_timeseriesmedia import ArduinoTimeseriesmedia

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoTimeseriesmedia from a JSON string
arduino_timeseriesmedia_instance = ArduinoTimeseriesmedia.from_json(json)
# print the JSON string representation of the object
print ArduinoTimeseriesmedia.to_json()

# convert the object into a dict
arduino_timeseriesmedia_dict = arduino_timeseriesmedia_instance.to_dict()
# create an instance of ArduinoTimeseriesmedia from a dict
arduino_timeseriesmedia_form_dict = arduino_timeseriesmedia.from_dict(arduino_timeseriesmedia_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



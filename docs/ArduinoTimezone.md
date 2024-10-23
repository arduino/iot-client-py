# ArduinoTimezone

ArduinoTimezone media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the time zone. | 
**offset** | **int** | Current UTC DST offset in seconds. | 
**until** | **datetime** | Date until the offset is valid. | 

## Example

```python
from iot_api_client.models.arduino_timezone import ArduinoTimezone

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoTimezone from a JSON string
arduino_timezone_instance = ArduinoTimezone.from_json(json)
# print the JSON string representation of the object
print(ArduinoTimezone.to_json())

# convert the object into a dict
arduino_timezone_dict = arduino_timezone_instance.to_dict()
# create an instance of ArduinoTimezone from a dict
arduino_timezone_from_dict = ArduinoTimezone.from_dict(arduino_timezone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



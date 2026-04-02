# ArduinoPagevariable

ArduinoPagevariable media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** | The icon of the Page | [optional] 
**id** | **str** | The id of the Page | 
**name** | **str** | The name of the Page | 
**position** | **int** | The position of the Page | 

## Example

```python
from iot_api_client.models.arduino_pagevariable import ArduinoPagevariable

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoPagevariable from a JSON string
arduino_pagevariable_instance = ArduinoPagevariable.from_json(json)
# print the JSON string representation of the object
print(ArduinoPagevariable.to_json())

# convert the object into a dict
arduino_pagevariable_dict = arduino_pagevariable_instance.to_dict()
# create an instance of ArduinoPagevariable from a dict
arduino_pagevariable_from_dict = ArduinoPagevariable.from_dict(arduino_pagevariable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



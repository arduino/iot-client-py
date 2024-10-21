# ArduinoVariableslinks

ArduinoVariableslinks media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | **List[str]** | The ids of the linked variables | 

## Example

```python
from iot_api_client.models.arduino_variableslinks import ArduinoVariableslinks

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoVariableslinks from a JSON string
arduino_variableslinks_instance = ArduinoVariableslinks.from_json(json)
# print the JSON string representation of the object
print ArduinoVariableslinks.to_json()

# convert the object into a dict
arduino_variableslinks_dict = arduino_variableslinks_instance.to_dict()
# create an instance of ArduinoVariableslinks from a dict
arduino_variableslinks_form_dict = arduino_variableslinks.from_dict(arduino_variableslinks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



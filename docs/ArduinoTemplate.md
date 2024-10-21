# ArduinoTemplate

ArduinoTemplate media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboards** | **List[str]** |  | [optional] 
**things** | [**List[ArduinoThingresult]**](ArduinoThingresult.md) | ArduinoThingresultCollection is the media type for an array of ArduinoThingresult (default view) | 
**triggers** | **List[str]** |  | [optional] 

## Example

```python
from iot_api_client.models.arduino_template import ArduinoTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoTemplate from a JSON string
arduino_template_instance = ArduinoTemplate.from_json(json)
# print the JSON string representation of the object
print ArduinoTemplate.to_json()

# convert the object into a dict
arduino_template_dict = arduino_template_instance.to_dict()
# create an instance of ArduinoTemplate from a dict
arduino_template_form_dict = arduino_template.from_dict(arduino_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



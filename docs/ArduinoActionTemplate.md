# ArduinoActionTemplate

ArduinoAction_template media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the action | [optional] 
**email** | [**EmailAction**](EmailAction.md) |  | [optional] 
**kind** | **str** | The kind of the action | [optional] 
**name** | **str** | The name of the action | [optional] 
**organization_id** | **str** | Id of the organization the trigger belongs to | [optional] 
**push_notification** | [**PushAction**](PushAction.md) |  | [optional] 

## Example

```python
from iot_api_client.models.arduino_action_template import ArduinoActionTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoActionTemplate from a JSON string
arduino_action_template_instance = ArduinoActionTemplate.from_json(json)
# print the JSON string representation of the object
print(ArduinoActionTemplate.to_json())

# convert the object into a dict
arduino_action_template_dict = arduino_action_template_instance.to_dict()
# create an instance of ArduinoActionTemplate from a dict
arduino_action_template_from_dict = ArduinoActionTemplate.from_dict(arduino_action_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



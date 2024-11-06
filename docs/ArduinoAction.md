# ArduinoAction

ArduinoAction media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | Id of the user who created the action | [optional] 
**description** | **str** | The description of the action | [optional] 
**email** | [**EmailAction**](EmailAction.md) |  | [optional] 
**id** | **str** | The id of the action | [optional] 
**kind** | **str** | The kind of the action | [optional] 
**name** | **str** | The name of the action | [optional] 
**organization_id** | **str** | Id of the organization the trigger belongs to | [optional] 
**push_notification** | [**PushAction**](PushAction.md) |  | [optional] 
**trigger_id** | **str** | Id of the trigger the action is associated to | [optional] 

## Example

```python
from iot_api_client.models.arduino_action import ArduinoAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoAction from a JSON string
arduino_action_instance = ArduinoAction.from_json(json)
# print the JSON string representation of the object
print(ArduinoAction.to_json())

# convert the object into a dict
arduino_action_dict = arduino_action_instance.to_dict()
# create an instance of ArduinoAction from a dict
arduino_action_from_dict = ArduinoAction.from_dict(arduino_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



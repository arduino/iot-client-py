# ArduinoTriggerTemplate

ArduinoTrigger_template media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[ArduinoActionTemplate]**](ArduinoActionTemplate.md) | A list of actions associated with the trigger | [optional] 
**active** | **bool** | Is true if the trigger is enabled | [optional] 
**criteria** | **str** | The criteria of the trigger, could be INCLUDE or EXCLUDE | [optional] 
**description** | **str** | The description of the trigger | [optional] 
**grace_period_offline** | **int** | The amount of seconds the trigger will wait before considering a matching device as offline | [optional] 
**grace_period_online** | **int** | The amount of seconds the trigger will wait before considering a matching device as online | [optional] 
**id** | **str** | The id of the trigger | 
**linked_devices** | [**List[ArduinoLinkedDeviceTemplate]**](ArduinoLinkedDeviceTemplate.md) | A list of devices the trigger is associated to | [optional] 
**linked_property** | [**ArduinoLinkedPropertyTemplate**](ArduinoLinkedPropertyTemplate.md) |  | [optional] 
**name** | **str** | The name of the trigger | 
**organization_id** | **str** | Id of the organization the trigger belongs to | [optional] 

## Example

```python
from iot_api_client.models.arduino_trigger_template import ArduinoTriggerTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoTriggerTemplate from a JSON string
arduino_trigger_template_instance = ArduinoTriggerTemplate.from_json(json)
# print the JSON string representation of the object
print(ArduinoTriggerTemplate.to_json())

# convert the object into a dict
arduino_trigger_template_dict = arduino_trigger_template_instance.to_dict()
# create an instance of ArduinoTriggerTemplate from a dict
arduino_trigger_template_from_dict = ArduinoTriggerTemplate.from_dict(arduino_trigger_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



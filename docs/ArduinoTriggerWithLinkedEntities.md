# ArduinoTriggerWithLinkedEntities

ArduinoTrigger_with_linked_entities media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[ArduinoAction]**](ArduinoAction.md) | A list of actions associated with the trigger | [optional] 
**active** | **bool** | Is true if the trigger is enabled | [optional] 
**created_by** | **str** | Id of the user who last updated the trigger | [optional] 
**description** | **str** | The description of the trigger | [optional] 
**device_status_source** | [**DeviceStatusSourceWithLinkedDevices**](DeviceStatusSourceWithLinkedDevices.md) |  | [optional] 
**id** | **str** | The id of the trigger | 
**linked_property** | [**ArduinoLinkedProperty**](ArduinoLinkedProperty.md) |  | [optional] 
**name** | **str** | The name of the trigger | 
**organization_id** | **str** | Id of the organization the trigger belongs to | [optional] 

## Example

```python
from iot_api_client.models.arduino_trigger_with_linked_entities import ArduinoTriggerWithLinkedEntities

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoTriggerWithLinkedEntities from a JSON string
arduino_trigger_with_linked_entities_instance = ArduinoTriggerWithLinkedEntities.from_json(json)
# print the JSON string representation of the object
print(ArduinoTriggerWithLinkedEntities.to_json())

# convert the object into a dict
arduino_trigger_with_linked_entities_dict = arduino_trigger_with_linked_entities_instance.to_dict()
# create an instance of ArduinoTriggerWithLinkedEntities from a dict
arduino_trigger_with_linked_entities_from_dict = ArduinoTriggerWithLinkedEntities.from_dict(arduino_trigger_with_linked_entities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



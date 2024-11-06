# ArduinoTrigger

ArduinoTrigger media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[ArduinoAction]**](ArduinoAction.md) | A list of actions associated with the trigger | [optional] 
**active** | **bool** | Is true if the trigger is enabled | [optional] 
**created_at** | **datetime** | Creation date of the trigger | [optional] 
**created_by** | **str** | Id of the user who last updated the trigger | [optional] 
**deleted_at** | **datetime** | Deletion date of the trigger | [optional] 
**description** | **str** | The description of the trigger | [optional] 
**device_status_source** | [**DeviceStatusSource**](DeviceStatusSource.md) |  | [optional] 
**id** | **str** | The id of the trigger | [optional] 
**name** | **str** | The name of the trigger | 
**organization_id** | **str** | Id of the organization the trigger belongs to | [optional] 
**property_id** | **str** | Id of the property the trigger is associated to (mutually exclusive with &#39;device_status_source&#39;) | [optional] 
**updated_at** | **datetime** | Update date of the trigger | [optional] 

## Example

```python
from iot_api_client.models.arduino_trigger import ArduinoTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoTrigger from a JSON string
arduino_trigger_instance = ArduinoTrigger.from_json(json)
# print the JSON string representation of the object
print(ArduinoTrigger.to_json())

# convert the object into a dict
arduino_trigger_dict = arduino_trigger_instance.to_dict()
# create an instance of ArduinoTrigger from a dict
arduino_trigger_from_dict = ArduinoTrigger.from_dict(arduino_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



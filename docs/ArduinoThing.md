# ArduinoThing

ArduinoThing media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistant** | **str** | The kind of voice assistant the thing is connected to, it can be ALEXA | GOOGLE | NONE | [optional] 
**created_at** | **datetime** | Creation date of the thing | [optional] 
**deleted_at** | **datetime** | Delete date of the thing | [optional] 
**device_fqbn** | **str** | The fqbn of the attached device, if any | [optional] 
**device_id** | **str** | The id of the device | [optional] 
**device_name** | **str** | The name of the attached device, if any | [optional] 
**device_type** | **str** | The type of the attached device, if any | [optional] 
**href** | **str** | The api reference of this thing | 
**id** | **str** | The id of the thing | 
**name** | **str** | The friendly name of the thing | 
**organization_id** | **str** | Id of the organization the thing belongs to | [optional] 
**properties** | [**List[ArduinoProperty]**](ArduinoProperty.md) | ArduinoPropertyCollection is the media type for an array of ArduinoProperty (default view) | [optional] 
**properties_count** | **int** | The number of properties of the thing | [optional] 
**sketch_id** | **str** | The id of the attached sketch | [optional] 
**tags** | **Dict[str, object]** | Tags of the thing | [optional] 
**timezone** | **str** | Time zone of the thing | 
**updated_at** | **datetime** | Update date of the thing | [optional] 
**user_id** | **str** | The user id of the owner | 
**webhook_active** | **bool** | Webhook uri | [optional] 
**webhook_uri** | **str** | Webhook uri | [optional] 

## Example

```python
from iot_api_client.models.arduino_thing import ArduinoThing

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoThing from a JSON string
arduino_thing_instance = ArduinoThing.from_json(json)
# print the JSON string representation of the object
print(ArduinoThing.to_json())

# convert the object into a dict
arduino_thing_dict = arduino_thing_instance.to_dict()
# create an instance of ArduinoThing from a dict
arduino_thing_from_dict = ArduinoThing.from_dict(arduino_thing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



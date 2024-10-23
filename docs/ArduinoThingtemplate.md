# ArduinoThingtemplate

ArduinoThingtemplate media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_metadata** | [**ArduinoDevicev2templatedevice**](ArduinoDevicev2templatedevice.md) |  | [optional] 
**id** | **str** | The friendly id of the thing | [optional] 
**name** | **str** | The friendly name of the thing | 
**organization_id** | **str** | Id of the organization the thing belongs to | [optional] 
**sketch_template** | **str** | The ID of the template&#39;s sketch | [optional] 
**tags** | [**List[Tag]**](Tag.md) | Tags of the thing | [optional] 
**timezone** | **str** | Time zone of the thing | 
**variables** | [**List[ArduinoTemplateproperty]**](ArduinoTemplateproperty.md) | ArduinoTemplatepropertyCollection is the media type for an array of ArduinoTemplateproperty (default view) | [optional] 
**webhook_uri** | **str** | Webhook uri | [optional] 

## Example

```python
from iot_api_client.models.arduino_thingtemplate import ArduinoThingtemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoThingtemplate from a JSON string
arduino_thingtemplate_instance = ArduinoThingtemplate.from_json(json)
# print the JSON string representation of the object
print(ArduinoThingtemplate.to_json())

# convert the object into a dict
arduino_thingtemplate_dict = arduino_thingtemplate_instance.to_dict()
# create an instance of ArduinoThingtemplate from a dict
arduino_thingtemplate_from_dict = ArduinoThingtemplate.from_dict(arduino_thingtemplate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



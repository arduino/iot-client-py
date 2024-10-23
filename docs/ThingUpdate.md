# ThingUpdate

Payload to update an existing thing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistant** | **str** | The kind of voice assistant the thing is connected to, it can be ALEXA | GOOGLE | NONE | [optional] 
**device_id** | **str** | The arn of the associated device | [optional] 
**id** | **str** | The id of the thing | [optional] 
**name** | **str** | The friendly name of the thing | [optional] 
**properties** | [**List[ModelProperty]**](ModelProperty.md) | The properties of the thing | [optional] 
**timezone** | **str** | A time zone name. Check /v2/timezones for a list of valid names. | [optional] 
**webhook_active** | **bool** | Webhook uri | [optional] 
**webhook_uri** | **str** | Webhook uri | [optional] 

## Example

```python
from iot_api_client.models.thing_update import ThingUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ThingUpdate from a JSON string
thing_update_instance = ThingUpdate.from_json(json)
# print the JSON string representation of the object
print(ThingUpdate.to_json())

# convert the object into a dict
thing_update_dict = thing_update_instance.to_dict()
# create an instance of ThingUpdate from a dict
thing_update_from_dict = ThingUpdate.from_dict(thing_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



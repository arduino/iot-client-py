# ThingCreate

Payload to create a new thing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistant** | **str** | The kind of voice assistant the thing is connected to, it can be ALEXA | GOOGLE | NONE | [optional] 
**device_id** | **str** | The arn of the associated device | [optional] 
**id** | **str** | The id of the thing | [optional] 
**name** | **str** | The friendly name of the thing | [optional] 
**properties** | [**List[ModelProperty]**](ModelProperty.md) | The properties of the thing | [optional] 
**tags** | [**List[Tag]**](Tag.md) | Optional set of tags | [optional] 
**timezone** | **str** | A time zone name Check /v2/timezones for a list of valid names. | [optional] [default to 'America/New_York']
**webhook_active** | **bool** | Webhook uri | [optional] 
**webhook_uri** | **str** | Webhook uri | [optional] 

## Example

```python
from iot_api_client.models.thing_create import ThingCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ThingCreate from a JSON string
thing_create_instance = ThingCreate.from_json(json)
# print the JSON string representation of the object
print(ThingCreate.to_json())

# convert the object into a dict
thing_create_dict = thing_create_instance.to_dict()
# create an instance of ThingCreate from a dict
thing_create_from_dict = ThingCreate.from_dict(thing_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



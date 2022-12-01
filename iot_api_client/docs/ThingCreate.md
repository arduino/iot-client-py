# ThingCreate

Payload to create a new thing
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | The arn of the associated device | [optional] 
**id** | **str** | The id of the thing | [optional] 
**name** | **str** | The friendly name of the thing | [optional] 
**properties** | [**list[ModelProperty]**](ModelProperty.md) | The properties of the thing | [optional] 
**timezone** | **str** | A time zone name Check /v2/timezones for a list of valid names. | [optional] [default to 'America/New_York']
**webhook_active** | **bool** | Webhook uri | [optional] 
**webhook_uri** | **str** | Webhook uri | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ModelProperty

PropertyPayload describes a property of a thing. No field is mandatory
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_value** | **float** | Maximum value of this property | [optional] 
**min_value** | **float** | Minimum value of this property | [optional] 
**name** | **str** | The friendly name of the property | 
**permission** | **str** | The permission of the property | 
**persist** | **bool** | If true, data will persist into a timeseries database | [optional] [default to True]
**tag** | **float** | The integer id of the property | [optional] 
**type** | **str** | The type of the property | 
**update_parameter** | **float** | The update frequency in seconds, or the amount of the property has to change in order to trigger an update | [optional] 
**update_strategy** | **str** | The update strategy for the property value | 
**variable_name** | **str** | The  sketch variable name of the property | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



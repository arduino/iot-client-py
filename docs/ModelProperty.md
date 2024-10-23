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
**tag** | **int** | The integer id of the property | [optional] 
**type** | **str** | The type of the property | 
**update_parameter** | **float** | The update frequency in seconds, or the amount of the property has to change in order to trigger an update | [optional] 
**update_strategy** | **str** | The update strategy for the property value | 
**variable_name** | **str** | The  sketch variable name of the property | [optional] 

## Example

```python
from iot_api_client.models.model_property import ModelProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ModelProperty from a JSON string
model_property_instance = ModelProperty.from_json(json)
# print the JSON string representation of the object
print(ModelProperty.to_json())

# convert the object into a dict
model_property_dict = model_property_instance.to_dict()
# create an instance of ModelProperty from a dict
model_property_from_dict = ModelProperty.from_dict(model_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



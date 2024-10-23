# PropertiesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the property | 
**type** | **str** | The type of the property | [default to 'infer']
**value** | **object** | The last value of the property | 

## Example

```python
from iot_api_client.models.properties_value import PropertiesValue

# TODO update the JSON string below
json = "{}"
# create an instance of PropertiesValue from a JSON string
properties_value_instance = PropertiesValue.from_json(json)
# print the JSON string representation of the object
print(PropertiesValue.to_json())

# convert the object into a dict
properties_value_dict = properties_value_instance.to_dict()
# create an instance of PropertiesValue from a dict
properties_value_from_dict = PropertiesValue.from_dict(properties_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



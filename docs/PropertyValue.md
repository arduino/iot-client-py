# PropertyValue

PropertyValuePayload describes a property value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | The device who send the property | [optional] 
**value** | **object** | The property value | 

## Example

```python
from iot_api_client.models.property_value import PropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyValue from a JSON string
property_value_instance = PropertyValue.from_json(json)
# print the JSON string representation of the object
print(PropertyValue.to_json())

# convert the object into a dict
property_value_dict = property_value_instance.to_dict()
# create an instance of PropertyValue from a dict
property_value_from_dict = PropertyValue.from_dict(property_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



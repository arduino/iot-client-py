# PropertyTimedValue

PropertyValuePayload describes a property value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The timestamp of the property value | 
**value** | **object** | The property value | 

## Example

```python
from iot_api_client.models.property_timed_value import PropertyTimedValue

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyTimedValue from a JSON string
property_timed_value_instance = PropertyTimedValue.from_json(json)
# print the JSON string representation of the object
print(PropertyTimedValue.to_json())

# convert the object into a dict
property_timed_value_dict = property_timed_value_instance.to_dict()
# create an instance of PropertyTimedValue from a dict
property_timed_value_from_dict = PropertyTimedValue.from_dict(property_timed_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



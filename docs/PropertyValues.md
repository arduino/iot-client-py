# PropertyValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**List[PropertyDefinition]**](PropertyDefinition.md) | The set of properties to publish | 
**to_device** | **bool** | Handle data direction, simulating data from or to device (default false - data sent by device) | [optional] [default to False]

## Example

```python
from iot_api_client.models.property_values import PropertyValues

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyValues from a JSON string
property_values_instance = PropertyValues.from_json(json)
# print the JSON string representation of the object
print(PropertyValues.to_json())

# convert the object into a dict
property_values_dict = property_values_instance.to_dict()
# create an instance of PropertyValues from a dict
property_values_from_dict = PropertyValues.from_dict(property_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



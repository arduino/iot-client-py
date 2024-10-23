# PropertiesValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **bool** | If true, send property values to device&#39;s input topic. | [optional] [default to False]
**properties** | [**List[PropertiesValue]**](PropertiesValue.md) |  | 

## Example

```python
from iot_api_client.models.properties_values import PropertiesValues

# TODO update the JSON string below
json = "{}"
# create an instance of PropertiesValues from a JSON string
properties_values_instance = PropertiesValues.from_json(json)
# print the JSON string representation of the object
print(PropertiesValues.to_json())

# convert the object into a dict
properties_values_dict = properties_values_instance.to_dict()
# create an instance of PropertiesValues from a dict
properties_values_from_dict = PropertiesValues.from_dict(properties_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



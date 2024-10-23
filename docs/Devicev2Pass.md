# Devicev2Pass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password for the device | [optional] 

## Example

```python
from iot_api_client.models.devicev2_pass import Devicev2Pass

# TODO update the JSON string below
json = "{}"
# create an instance of Devicev2Pass from a JSON string
devicev2_pass_instance = Devicev2Pass.from_json(json)
# print the JSON string representation of the object
print(Devicev2Pass.to_json())

# convert the object into a dict
devicev2_pass_dict = devicev2_pass_instance.to_dict()
# create an instance of Devicev2Pass from a dict
devicev2_pass_from_dict = Devicev2Pass.from_dict(devicev2_pass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Devicev2Otaurlpyalod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_key** | **str** | The object key of the binary | [optional] 
**sha256** | **str** | The sha256 of the binary | [optional] 
**user_id** | **str** | The id of the user who is requesting the url | [optional] 

## Example

```python
from iot_api_client.models.devicev2_otaurlpyalod import Devicev2Otaurlpyalod

# TODO update the JSON string below
json = "{}"
# create an instance of Devicev2Otaurlpyalod from a JSON string
devicev2_otaurlpyalod_instance = Devicev2Otaurlpyalod.from_json(json)
# print the JSON string representation of the object
print Devicev2Otaurlpyalod.to_json()

# convert the object into a dict
devicev2_otaurlpyalod_dict = devicev2_otaurlpyalod_instance.to_dict()
# create an instance of Devicev2Otaurlpyalod from a dict
devicev2_otaurlpyalod_form_dict = devicev2_otaurlpyalod.from_dict(devicev2_otaurlpyalod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



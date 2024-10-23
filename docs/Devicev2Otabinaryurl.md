# Devicev2Otabinaryurl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_async** | **bool** | If false, wait for the full OTA process, until it gets a result from the device | [optional] [default to True]
**binary_key** | **str** | The object key of the binary | 
**expire_in_mins** | **int** | Binary expire time in minutes, default 10 mins | [optional] [default to 10]

## Example

```python
from iot_api_client.models.devicev2_otabinaryurl import Devicev2Otabinaryurl

# TODO update the JSON string below
json = "{}"
# create an instance of Devicev2Otabinaryurl from a JSON string
devicev2_otabinaryurl_instance = Devicev2Otabinaryurl.from_json(json)
# print the JSON string representation of the object
print(Devicev2Otabinaryurl.to_json())

# convert the object into a dict
devicev2_otabinaryurl_dict = devicev2_otabinaryurl_instance.to_dict()
# create an instance of Devicev2Otabinaryurl from a dict
devicev2_otabinaryurl_from_dict = Devicev2Otabinaryurl.from_dict(devicev2_otabinaryurl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Devicev2Cert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | The Certification Authority you want to use | [optional] 
**csr** | **str** | The certificate request in pem format | [optional] 
**enabled** | **bool** | Whether the certificate is enabled | [optional] 

## Example

```python
from iot_api_client.models.devicev2_cert import Devicev2Cert

# TODO update the JSON string below
json = "{}"
# create an instance of Devicev2Cert from a JSON string
devicev2_cert_instance = Devicev2Cert.from_json(json)
# print the JSON string representation of the object
print(Devicev2Cert.to_json())

# convert the object into a dict
devicev2_cert_dict = devicev2_cert_instance.to_dict()
# create an instance of Devicev2Cert from a dict
devicev2_cert_from_dict = Devicev2Cert.from_dict(devicev2_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



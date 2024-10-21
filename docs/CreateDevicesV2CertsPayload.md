# CreateDevicesV2CertsPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | The Certification Authority you want to use | [optional] 
**csr** | **str** | The certificate request in pem format | 
**enabled** | **bool** | Whether the certificate is enabled | 

## Example

```python
from iot_api_client.models.create_devices_v2_certs_payload import CreateDevicesV2CertsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDevicesV2CertsPayload from a JSON string
create_devices_v2_certs_payload_instance = CreateDevicesV2CertsPayload.from_json(json)
# print the JSON string representation of the object
print CreateDevicesV2CertsPayload.to_json()

# convert the object into a dict
create_devices_v2_certs_payload_dict = create_devices_v2_certs_payload_instance.to_dict()
# create an instance of CreateDevicesV2CertsPayload from a dict
create_devices_v2_certs_payload_form_dict = create_devices_v2_certs_payload.from_dict(create_devices_v2_certs_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



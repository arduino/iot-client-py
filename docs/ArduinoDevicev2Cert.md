# ArduinoDevicev2Cert

DeviceCertV2 describes a certificate associated to the device (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | The Certification Authority used to sign the certificate | [optional] 
**compressed** | [**ArduinoCompressedv2**](ArduinoCompressedv2.md) |  | 
**der** | **str** | The certificate in DER format | 
**device_id** | **str** | The unique identifier of the device | 
**enabled** | **bool** | Whether the certificate is enabled | [default to True]
**href** | **str** | The api reference of this cert | 
**id** | **str** | The unique identifier of the key | 
**pem** | **str** | The certificate in pem format | 

## Example

```python
from iot_api_client.models.arduino_devicev2_cert import ArduinoDevicev2Cert

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2Cert from a JSON string
arduino_devicev2_cert_instance = ArduinoDevicev2Cert.from_json(json)
# print the JSON string representation of the object
print ArduinoDevicev2Cert.to_json()

# convert the object into a dict
arduino_devicev2_cert_dict = arduino_devicev2_cert_instance.to_dict()
# create an instance of ArduinoDevicev2Cert from a dict
arduino_devicev2_cert_form_dict = arduino_devicev2_cert.from_dict(arduino_devicev2_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



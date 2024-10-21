# ArduinoCompressedv2

compressed contains the info from which to generate the certificate (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authority_key_identifier** | **str** | The Authority Key Identifier of the certificate | [optional] 
**not_after** | **datetime** | The ending date of the certificate | 
**not_before** | **datetime** | The starting date of the certificate | 
**serial** | **str** | The serial number of the certificate | 
**signature** | **str** | The signature of the certificate | 
**signature_asn1_x** | **str** | The ASN1 X component of certificate signature | 
**signature_asn1_y** | **str** | The ASN1 Y component of certificate signature | 

## Example

```python
from iot_api_client.models.arduino_compressedv2 import ArduinoCompressedv2

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoCompressedv2 from a JSON string
arduino_compressedv2_instance = ArduinoCompressedv2.from_json(json)
# print the JSON string representation of the object
print ArduinoCompressedv2.to_json()

# convert the object into a dict
arduino_compressedv2_dict = arduino_compressedv2_instance.to_dict()
# create an instance of ArduinoCompressedv2 from a dict
arduino_compressedv2_form_dict = arduino_compressedv2.from_dict(arduino_compressedv2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



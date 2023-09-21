# iot_api_client.model.arduino_compressedv2.ArduinoCompressedv2

compressed contains the info from which to generate the certificate (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | compressed contains the info from which to generate the certificate (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**not_after** | str, datetime,  | str,  | The ending date of the certificate | value must conform to RFC-3339 date-time
**serial** | str,  | str,  | The serial number of the certificate | 
**signature** | str,  | str,  | The signature of the certificate | 
**not_before** | str, datetime,  | str,  | The starting date of the certificate | value must conform to RFC-3339 date-time
**signature_asn1_x** | str,  | str,  | The ASN1 X component of certificate signature | 
**signature_asn1_y** | str,  | str,  | The ASN1 Y component of certificate signature | 
**authority_key_identifier** | str,  | str,  | The Authority Key Identifier of the certificate | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


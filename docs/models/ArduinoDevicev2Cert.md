# iot_api_client.model.arduino_devicev2_cert.ArduinoDevicev2Cert

DeviceCertV2 describes a certificate associated to the device (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DeviceCertV2 describes a certificate associated to the device (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**der** | str,  | str,  | The certificate in DER format | 
**device_id** | str, uuid.UUID,  | str,  | The unique identifier of the device | value must be a uuid
**pem** | str,  | str,  | The certificate in pem format | 
**compressed** | [**ArduinoCompressedv2**](ArduinoCompressedv2.md) | [**ArduinoCompressedv2**](ArduinoCompressedv2.md) |  | 
**href** | str,  | str,  | The api reference of this cert | 
**id** | str, uuid.UUID,  | str,  | The unique identifier of the key | value must be a uuid
**enabled** | bool,  | BoolClass,  | Whether the certificate is enabled | if omitted the server will use the default value of True
**ca** | str,  | str,  | The Certification Authority used to sign the certificate | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


# iot_api_client.model.create_devices_v2_payload.CreateDevicesV2Payload

DeviceV2 describes a device.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DeviceV2 describes a device. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | The type of the device | must be one of ["mkrwifi1010", "mkr1000", "nano_33_iot", "mkrgsm1400", "mkrwan1310", "mkrwan1300", "mkrnb1500", "lora-device", "login_and_secretkey_wifi", "envie_m7", "nanorp2040connect", "nicla_vision", "phone", "portenta_x8", "opta", "giga", "generic_device_secretkey", "portenta_c33", "unor4wifi", "nano_nora", ] 
**connection_type** | str,  | str,  | The type of the connections selected by the user when multiple connections are available | [optional] must be one of ["wifi", "eth", "wifiandsecret", "gsm", "nb", "lora", "catm1", "cellular", ] 
**fqbn** | str,  | str,  | The fully qualified board name | [optional] 
**name** | str,  | str,  | The friendly name of the device | [optional] 
**serial** | str,  | str,  | The serial uuid of the device | [optional] 
**user_id** | str, uuid.UUID,  | str,  | The user_id associated to the device. If absent it will be inferred from the authentication header | [optional] value must be a uuid
**wifi_fw_version** | str,  | str,  | The version of the NINA/WIFI101 firmware running on the device | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


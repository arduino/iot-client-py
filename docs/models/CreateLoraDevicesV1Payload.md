# iot_api_client.model.create_lora_devices_v1_payload.CreateLoraDevicesV1Payload

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**app** | str,  | str,  | The app name | 
**user_id** | str,  | str,  | The id of the user. Can be the special string &#x27;me&#x27; | 
**eui** | str,  | str,  | The eui of the lora device | 
**frequency_plan** | str,  | str,  | The frequency plan required by your country  | must be one of ["EU_863_870_TTN", "US_902_928_FSB_2", "EU_433", "AU_915_928_FSB_2", "CN_470_510_FSB_11", "AS_920_923", "AS_920_923_TTN_AU", "AS_923_925", "AS_923_925_TTN_AU", "KR_920_923_TTN", "IN_865_867", ] 
**name** | str,  | str,  | A common name for the device | 
**type** | str,  | str,  | The type of device | must be one of ["lora-device", "mkrwan1300", "mkrwan1310", ] 
**app_eui** | str,  | str,  | The app eui of the lora device | [optional] 
**app_key** | str,  | str,  | The app key of the lora device | [optional] 
**serial** | str,  | str,  | The optional serial number | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


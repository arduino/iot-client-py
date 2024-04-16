# iot_api_client.model.arduino_devicev2_otaupload.ArduinoDevicev2Otaupload

ArduinoDevicev2Otaupload media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoDevicev2Otaupload media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ota_version** | decimal.Decimal, int,  | decimal.Decimal,  | OTA version | value must be a 64 bit integer
**file_sha** | str,  | str,  | SHA256 of the uploaded file | [optional] 
**ota_id** | str,  | str,  | OTA request id (only available from OTA version 2 and above) | [optional] 
**status** | str,  | str,  | OTA request status (only available from OTA version 2 and above) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


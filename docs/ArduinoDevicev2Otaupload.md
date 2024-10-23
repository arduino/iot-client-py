# ArduinoDevicev2Otaupload

ArduinoDevicev2Otaupload media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_sha** | **str** | SHA256 of the uploaded file | [optional] 
**ota_id** | **str** | OTA request id (only available from OTA version 2 and above) | [optional] 
**ota_version** | **int** | OTA version | 
**status** | **str** | OTA request status (only available from OTA version 2 and above) | [optional] 

## Example

```python
from iot_api_client.models.arduino_devicev2_otaupload import ArduinoDevicev2Otaupload

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2Otaupload from a JSON string
arduino_devicev2_otaupload_instance = ArduinoDevicev2Otaupload.from_json(json)
# print the JSON string representation of the object
print(ArduinoDevicev2Otaupload.to_json())

# convert the object into a dict
arduino_devicev2_otaupload_dict = arduino_devicev2_otaupload_instance.to_dict()
# create an instance of ArduinoDevicev2Otaupload from a dict
arduino_devicev2_otaupload_from_dict = ArduinoDevicev2Otaupload.from_dict(arduino_devicev2_otaupload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



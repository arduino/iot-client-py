# ArduinoArduinoconnectionsV1

ArduinoArduinoconnectionsV1 media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catm1** | [**List[ArduinoCredentialsv1]**](ArduinoCredentialsv1.md) | ArduinoCredentialsv1Collection is the media type for an array of ArduinoCredentialsv1 (default view) | [optional] 
**cellular** | [**List[ArduinoCredentialsv1]**](ArduinoCredentialsv1.md) | ArduinoCredentialsv1Collection is the media type for an array of ArduinoCredentialsv1 (default view) | [optional] 
**eth** | [**List[ArduinoCredentialsv1]**](ArduinoCredentialsv1.md) | ArduinoCredentialsv1Collection is the media type for an array of ArduinoCredentialsv1 (default view) | [optional] 
**gsm** | [**List[ArduinoCredentialsv1]**](ArduinoCredentialsv1.md) | ArduinoCredentialsv1Collection is the media type for an array of ArduinoCredentialsv1 (default view) | [optional] 
**lora** | [**List[ArduinoCredentialsv1]**](ArduinoCredentialsv1.md) | ArduinoCredentialsv1Collection is the media type for an array of ArduinoCredentialsv1 (default view) | [optional] 
**nb** | [**List[ArduinoCredentialsv1]**](ArduinoCredentialsv1.md) | ArduinoCredentialsv1Collection is the media type for an array of ArduinoCredentialsv1 (default view) | [optional] 
**wifi** | [**List[ArduinoCredentialsv1]**](ArduinoCredentialsv1.md) | ArduinoCredentialsv1Collection is the media type for an array of ArduinoCredentialsv1 (default view) | [optional] 
**wifiandsecret** | [**List[ArduinoCredentialsv1]**](ArduinoCredentialsv1.md) | ArduinoCredentialsv1Collection is the media type for an array of ArduinoCredentialsv1 (default view) | [optional] 

## Example

```python
from iot_api_client.models.arduino_arduinoconnections_v1 import ArduinoArduinoconnectionsV1

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoArduinoconnectionsV1 from a JSON string
arduino_arduinoconnections_v1_instance = ArduinoArduinoconnectionsV1.from_json(json)
# print the JSON string representation of the object
print(ArduinoArduinoconnectionsV1.to_json())

# convert the object into a dict
arduino_arduinoconnections_v1_dict = arduino_arduinoconnections_v1_instance.to_dict()
# create an instance of ArduinoArduinoconnectionsV1 from a dict
arduino_arduinoconnections_v1_from_dict = ArduinoArduinoconnectionsV1.from_dict(arduino_arduinoconnections_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



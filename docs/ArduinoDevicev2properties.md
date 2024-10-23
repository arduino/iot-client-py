# ArduinoDevicev2properties

ArduinoDevicev2properties media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_retention_days** | **float** | How many days the data will be kept | 
**device_id** | **str** | The device of the property | 
**properties** | [**List[ArduinoProperty]**](ArduinoProperty.md) | ArduinoPropertyCollection is the media type for an array of ArduinoProperty (default view) | 
**user_id** | **str** | The user id of the owner | 

## Example

```python
from iot_api_client.models.arduino_devicev2properties import ArduinoDevicev2properties

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2properties from a JSON string
arduino_devicev2properties_instance = ArduinoDevicev2properties.from_json(json)
# print the JSON string representation of the object
print(ArduinoDevicev2properties.to_json())

# convert the object into a dict
arduino_devicev2properties_dict = arduino_devicev2properties_instance.to_dict()
# create an instance of ArduinoDevicev2properties from a dict
arduino_devicev2properties_from_dict = ArduinoDevicev2properties.from_dict(arduino_devicev2properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



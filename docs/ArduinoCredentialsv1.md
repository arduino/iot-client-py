# ArduinoCredentialsv1

ArduinoCredentialsv1 media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friendly_name** | **str** | Friendly name | 
**required** | **bool** | Tell if the parameter is required or not | 
**secret_name** | **str** | The secret parameter name | 
**sensitive** | **bool** | Tell if the field is sensitive | 

## Example

```python
from iot_api_client.models.arduino_credentialsv1 import ArduinoCredentialsv1

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoCredentialsv1 from a JSON string
arduino_credentialsv1_instance = ArduinoCredentialsv1.from_json(json)
# print the JSON string representation of the object
print ArduinoCredentialsv1.to_json()

# convert the object into a dict
arduino_credentialsv1_dict = arduino_credentialsv1_instance.to_dict()
# create an instance of ArduinoCredentialsv1 from a dict
arduino_credentialsv1_form_dict = arduino_credentialsv1.from_dict(arduino_credentialsv1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



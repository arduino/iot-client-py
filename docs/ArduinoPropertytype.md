# ArduinoPropertytype

ArduinoPropertytype media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistants** | **List[str]** | The voice assistants available for this type | [optional] 
**declaration** | **str** | The c++ type we are using for this variable type | 
**deprecated** | **bool** | Tell if this type is deprecated | 
**example** | **str** | Example of use | [optional] 
**name** | **str** | The friendly name of the property type | 
**rw** | **bool** | Tell if the type allow a R/W permission | 
**superseded_by** | **str** | The type of property to use if it&#39;s deprecated | [optional] 
**tags** | **List[str]** | The tags related to the type | [optional] 
**type** | **str** | The api reference of this type | 
**units** | **List[str]** | The measure units available for this type | [optional] 

## Example

```python
from iot_api_client.models.arduino_propertytype import ArduinoPropertytype

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoPropertytype from a JSON string
arduino_propertytype_instance = ArduinoPropertytype.from_json(json)
# print the JSON string representation of the object
print(ArduinoPropertytype.to_json())

# convert the object into a dict
arduino_propertytype_dict = arduino_propertytype_instance.to_dict()
# create an instance of ArduinoPropertytype from a dict
arduino_propertytype_from_dict = ArduinoPropertytype.from_dict(arduino_propertytype_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



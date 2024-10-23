# ArduinoProperty

ArduinoProperty media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Creation date of the property | [optional] 
**deleted_at** | **datetime** | Delete date of the property | [optional] 
**href** | **str** | The api reference of this property | 
**id** | **str** | The id of the property | 
**last_value** | **object** | Last value of this property | [optional] 
**linked_to_trigger** | **bool** | Indicates if the property is involved in the activation of at least a trigger | [optional] 
**max_value** | **float** | Maximum value of this property | [optional] 
**min_value** | **float** | Minimum value of this property | [optional] 
**name** | **str** | The friendly name of the property | 
**permission** | **str** | The permission of the property | 
**persist** | **bool** | If true, data will persist into a timeseries database | [optional] 
**sync_id** | **str** | The id of the sync pool | [optional] 
**tag** | **int** | The integer id of the property | [optional] 
**thing_id** | **str** | The id of the thing | 
**thing_name** | **str** | The name of the associated thing | [optional] 
**type** | **str** | The type of the property | 
**update_parameter** | **float** | The update frequency in seconds, or the amount of the property has to change in order to trigger an update | [optional] 
**update_strategy** | **str** | The update strategy for the property value | 
**updated_at** | **datetime** | Update date of the property | [optional] 
**value_updated_at** | **datetime** | Last update timestamp of this property | [optional] 
**variable_name** | **str** | The sketch variable name of the property | [optional] 

## Example

```python
from iot_api_client.models.arduino_property import ArduinoProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoProperty from a JSON string
arduino_property_instance = ArduinoProperty.from_json(json)
# print the JSON string representation of the object
print(ArduinoProperty.to_json())

# convert the object into a dict
arduino_property_dict = arduino_property_instance.to_dict()
# create an instance of ArduinoProperty from a dict
arduino_property_from_dict = ArduinoProperty.from_dict(arduino_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArduinoTags

ArduinoTags media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[Tag]**](Tag.md) |  | 

## Example

```python
from iot_api_client.models.arduino_tags import ArduinoTags

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoTags from a JSON string
arduino_tags_instance = ArduinoTags.from_json(json)
# print the JSON string representation of the object
print(ArduinoTags.to_json())

# convert the object into a dict
arduino_tags_dict = arduino_tags_instance.to_dict()
# create an instance of ArduinoTags from a dict
arduino_tags_from_dict = ArduinoTags.from_dict(arduino_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArduinoWidgetv2template

ArduinoWidgetv2template media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | Widget current height for desktop | 
**height_mobile** | **int** | Widget current height for mobile | [optional] 
**name** | **str** | The name of the widget | [optional] 
**options** | **Dict[str, object]** | Widget options | 
**type** | **str** | The type of the widget | 
**variables** | [**List[ArduinoTemplatevariable]**](ArduinoTemplatevariable.md) | ArduinoTemplatevariableCollection is the media type for an array of ArduinoTemplatevariable (default view) | [optional] 
**width** | **int** | Widget current width for desktop | 
**width_mobile** | **int** | Widget current width for mobile | [optional] 
**x** | **int** | Widget x position for desktop | 
**x_mobile** | **int** | Widget x position for mobile | [optional] 
**y** | **int** | Widget y position for desktop | 
**y_mobile** | **int** | Widget y position for mobile | [optional] 

## Example

```python
from iot_api_client.models.arduino_widgetv2template import ArduinoWidgetv2template

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoWidgetv2template from a JSON string
arduino_widgetv2template_instance = ArduinoWidgetv2template.from_json(json)
# print the JSON string representation of the object
print(ArduinoWidgetv2template.to_json())

# convert the object into a dict
arduino_widgetv2template_dict = arduino_widgetv2template_instance.to_dict()
# create an instance of ArduinoWidgetv2template from a dict
arduino_widgetv2template_from_dict = ArduinoWidgetv2template.from_dict(arduino_widgetv2template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



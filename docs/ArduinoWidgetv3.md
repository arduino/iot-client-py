# ArduinoWidgetv3

ArduinoWidgetv3 media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_permission_incompatibility** | **bool** | True if the linked variables permissions are incompatible with the widget | [optional] 
**has_type_incompatibility** | **bool** | True if the linked variables types are incompatible with the widget | [optional] 
**has_unlinked_variable** | **bool** | If it&#39;s true the widget is linked to a soft-deleted variable | [optional] 
**height** | **int** | Widget current height for desktop | 
**height_mobile** | **int** | Widget current height for mobile | [optional] 
**id** | **str** | The UUID of the widget, set by client | 
**name** | **str** | The name of the widget | [optional] 
**options** | **Dict[str, object]** | Widget options | 
**page_id** | **str** | The ID of the page the widget belongs to, \&quot;0\&quot; if it&#39;s in the main page | 
**type** | **str** | The type of the widget | 
**variables** | [**List[ArduinoLinkedvariable]**](ArduinoLinkedvariable.md) | ArduinoLinkedvariableCollection is the media type for an array of ArduinoLinkedvariable (default view) | [optional] 
**width** | **int** | Widget current width for desktop | 
**width_mobile** | **int** | Widget current width for mobile | [optional] 
**x** | **int** | Widget x position for desktop | 
**x_mobile** | **int** | Widget x position for mobile | [optional] 
**y** | **int** | Widget y position for desktop | 
**y_mobile** | **int** | Widget y position for mobile | [optional] 

## Example

```python
from iot_api_client.models.arduino_widgetv3 import ArduinoWidgetv3

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoWidgetv3 from a JSON string
arduino_widgetv3_instance = ArduinoWidgetv3.from_json(json)
# print the JSON string representation of the object
print(ArduinoWidgetv3.to_json())

# convert the object into a dict
arduino_widgetv3_dict = arduino_widgetv3_instance.to_dict()
# create an instance of ArduinoWidgetv3 from a dict
arduino_widgetv3_from_dict = ArduinoWidgetv3.from_dict(arduino_widgetv3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Widget

Widget describes a dashboard widget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | Widget current height for desktop | 
**height_mobile** | **int** | Widget current height for mobile | [optional] 
**id** | **str** | The UUID of the widget, set by client | 
**name** | **str** | The name of the widget | [optional] 
**options** | **Dict[str, object]** | Widget options | 
**type** | **str** | The type of the widget | 
**variables** | **List[str]** |  | [optional] 
**width** | **int** | Widget current width for desktop | 
**width_mobile** | **int** | Widget current width for mobile | [optional] 
**x** | **int** | Widget x position for desktop | 
**x_mobile** | **int** | Widget x position for mobile | [optional] 
**y** | **int** | Widget y position for desktop | 
**y_mobile** | **int** | Widget y position for mobile | [optional] 

## Example

```python
from iot_api_client.models.widget import Widget

# TODO update the JSON string below
json = "{}"
# create an instance of Widget from a JSON string
widget_instance = Widget.from_json(json)
# print the JSON string representation of the object
print(Widget.to_json())

# convert the object into a dict
widget_dict = widget_instance.to_dict()
# create an instance of Widget from a dict
widget_from_dict = Widget.from_dict(widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



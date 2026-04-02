# Widgetv3

Widget describes a dashboard widget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | Widget current height for desktop | 
**height_mobile** | **int** | Widget current height for mobile | [optional] 
**id** | **str** | The UUID of the widget, set by client | 
**name** | **str** | The name of the widget | [optional] 
**options** | **Dict[str, object]** | Widget options | 
**page_id** | **str** | The ID of the page the widget belongs to, \&quot;0\&quot; if it&#39;s in the main page | [optional] 
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
from iot_api_client.models.widgetv3 import Widgetv3

# TODO update the JSON string below
json = "{}"
# create an instance of Widgetv3 from a JSON string
widgetv3_instance = Widgetv3.from_json(json)
# print the JSON string representation of the object
print(Widgetv3.to_json())

# convert the object into a dict
widgetv3_dict = widgetv3_instance.to_dict()
# create an instance of Widgetv3 from a dict
widgetv3_from_dict = Widgetv3.from_dict(widgetv3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



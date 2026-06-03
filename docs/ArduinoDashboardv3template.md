# ArduinoDashboardv3template

ArduinoDashboardv3template media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cover_image** | **str** | The cover image of the dashboard | [optional] 
**id** | **str** | The friendly ID of the dashboard | [optional] 
**name** | **str** | The friendly name of the dashboard | 
**pages** | [**List[ArduinoPagevariable]**](ArduinoPagevariable.md) | ArduinoPagevariableCollection is the media type for an array of ArduinoPagevariable (default view) | [optional] 
**widgets** | [**List[ArduinoWidgetv3template]**](ArduinoWidgetv3template.md) | ArduinoWidgetv3templateCollection is the media type for an array of ArduinoWidgetv3template (default view) | [optional] 

## Example

```python
from iot_api_client.models.arduino_dashboardv3template import ArduinoDashboardv3template

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDashboardv3template from a JSON string
arduino_dashboardv3template_instance = ArduinoDashboardv3template.from_json(json)
# print the JSON string representation of the object
print(ArduinoDashboardv3template.to_json())

# convert the object into a dict
arduino_dashboardv3template_dict = arduino_dashboardv3template_instance.to_dict()
# create an instance of ArduinoDashboardv3template from a dict
arduino_dashboardv3template_from_dict = ArduinoDashboardv3template.from_dict(arduino_dashboardv3template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



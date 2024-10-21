# ArduinoDashboardv2template

ArduinoDashboardv2template media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cover_image** | **str** | The cover image of the dashboard | [optional] 
**id** | **str** | The friendly ID of the dashboard | [optional] 
**name** | **str** | The friendly name of the dashboard | 
**widgets** | [**List[ArduinoWidgetv2template]**](ArduinoWidgetv2template.md) | ArduinoWidgetv2templateCollection is the media type for an array of ArduinoWidgetv2template (default view) | [optional] 

## Example

```python
from iot_api_client.models.arduino_dashboardv2template import ArduinoDashboardv2template

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDashboardv2template from a JSON string
arduino_dashboardv2template_instance = ArduinoDashboardv2template.from_json(json)
# print the JSON string representation of the object
print ArduinoDashboardv2template.to_json()

# convert the object into a dict
arduino_dashboardv2template_dict = arduino_dashboardv2template_instance.to_dict()
# create an instance of ArduinoDashboardv2template from a dict
arduino_dashboardv2template_form_dict = arduino_dashboardv2template.from_dict(arduino_dashboardv2template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



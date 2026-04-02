# ArduinoDashboardv3

Dashboard is a collection of widgets (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cover_image** | **str** | The cover image of the dashboard | [optional] 
**created_by** | [**ArduinoDashboardowner**](ArduinoDashboardowner.md) |  | [optional] 
**id** | **str** | The friendly name of the dashboard | 
**name** | **str** | The friendly name of the dashboard | 
**organization_id** | **str** | Id of the organization the dashboard belongs to | [optional] 
**pages** | [**List[ArduinoPagevariable]**](ArduinoPagevariable.md) | ArduinoPagevariableCollection is the media type for an array of ArduinoPagevariable (default view) | [optional] 
**shared_by** | [**ArduinoDashboardshare**](ArduinoDashboardshare.md) |  | [optional] 
**shared_with** | [**List[ArduinoDashboardshare]**](ArduinoDashboardshare.md) | ArduinoDashboardshareCollection is the media type for an array of ArduinoDashboardshare (default view) | [optional] 
**updated_at** | **datetime** | Last update date | 
**widgets** | [**List[ArduinoWidgetv3]**](ArduinoWidgetv3.md) | ArduinoWidgetv3Collection is the media type for an array of ArduinoWidgetv3 (default view) | [optional] 

## Example

```python
from iot_api_client.models.arduino_dashboardv3 import ArduinoDashboardv3

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDashboardv3 from a JSON string
arduino_dashboardv3_instance = ArduinoDashboardv3.from_json(json)
# print the JSON string representation of the object
print(ArduinoDashboardv3.to_json())

# convert the object into a dict
arduino_dashboardv3_dict = arduino_dashboardv3_instance.to_dict()
# create an instance of ArduinoDashboardv3 from a dict
arduino_dashboardv3_from_dict = ArduinoDashboardv3.from_dict(arduino_dashboardv3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



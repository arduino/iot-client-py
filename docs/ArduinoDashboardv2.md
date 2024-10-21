# ArduinoDashboardv2

Dashboard is a collection of widgets (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cover_image** | **str** | The cover image of the dashboard | [optional] 
**created_by** | [**ArduinoDashboardowner**](ArduinoDashboardowner.md) |  | [optional] 
**id** | **str** | The friendly name of the dashboard | 
**name** | **str** | The friendly name of the dashboard | 
**organization_id** | **str** | Id of the organization the dashboard belongs to | [optional] 
**shared_by** | [**ArduinoDashboardshare**](ArduinoDashboardshare.md) |  | [optional] 
**shared_with** | [**List[ArduinoDashboardshare]**](ArduinoDashboardshare.md) | ArduinoDashboardshareCollection is the media type for an array of ArduinoDashboardshare (default view) | [optional] 
**updated_at** | **datetime** | Last update date | 
**widgets** | [**List[ArduinoWidgetv2]**](ArduinoWidgetv2.md) | ArduinoWidgetv2Collection is the media type for an array of ArduinoWidgetv2 (default view) | [optional] 

## Example

```python
from iot_api_client.models.arduino_dashboardv2 import ArduinoDashboardv2

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDashboardv2 from a JSON string
arduino_dashboardv2_instance = ArduinoDashboardv2.from_json(json)
# print the JSON string representation of the object
print ArduinoDashboardv2.to_json()

# convert the object into a dict
arduino_dashboardv2_dict = arduino_dashboardv2_instance.to_dict()
# create an instance of ArduinoDashboardv2 from a dict
arduino_dashboardv2_form_dict = arduino_dashboardv2.from_dict(arduino_dashboardv2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



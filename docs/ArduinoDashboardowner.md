# ArduinoDashboardowner

ArduinoDashboardowner media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The userID of the user who created the dashboard | 
**username** | **str** | The username of the user who created the dashboard | [optional] 

## Example

```python
from iot_api_client.models.arduino_dashboardowner import ArduinoDashboardowner

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDashboardowner from a JSON string
arduino_dashboardowner_instance = ArduinoDashboardowner.from_json(json)
# print the JSON string representation of the object
print ArduinoDashboardowner.to_json()

# convert the object into a dict
arduino_dashboardowner_dict = arduino_dashboardowner_instance.to_dict()
# create an instance of ArduinoDashboardowner from a dict
arduino_dashboardowner_form_dict = arduino_dashboardowner.from_dict(arduino_dashboardowner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



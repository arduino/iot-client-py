# ArduinoDashboardshare

ArduinoDashboardshare media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The userID of the user you want to share the dashboard with | 
**username** | **str** | The username of the user you want to share the dashboard with | [optional] 

## Example

```python
from iot_api_client.models.arduino_dashboardshare import ArduinoDashboardshare

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDashboardshare from a JSON string
arduino_dashboardshare_instance = ArduinoDashboardshare.from_json(json)
# print the JSON string representation of the object
print ArduinoDashboardshare.to_json()

# convert the object into a dict
arduino_dashboardshare_dict = arduino_dashboardshare_instance.to_dict()
# create an instance of ArduinoDashboardshare from a dict
arduino_dashboardshare_form_dict = arduino_dashboardshare.from_dict(arduino_dashboardshare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Dashboardv2

DashboardV2Payload describes a dashboard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cover_image** | **str** | The cover image of the dashboard | [optional] 
**name** | **str** | The friendly name of the dashboard | [optional] 
**widgets** | [**List[Widget]**](Widget.md) | Widgets attached to this dashboard | [optional] 

## Example

```python
from iot_api_client.models.dashboardv2 import Dashboardv2

# TODO update the JSON string below
json = "{}"
# create an instance of Dashboardv2 from a JSON string
dashboardv2_instance = Dashboardv2.from_json(json)
# print the JSON string representation of the object
print Dashboardv2.to_json()

# convert the object into a dict
dashboardv2_dict = dashboardv2_instance.to_dict()
# create an instance of Dashboardv2 from a dict
dashboardv2_form_dict = dashboardv2.from_dict(dashboardv2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



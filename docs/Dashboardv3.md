# Dashboardv3

DashboardV3Payload describes a dashboard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cover_image** | **str** | The cover image of the dashboard | [optional] 
**name** | **str** | The friendly name of the dashboard | [optional] 
**pages** | [**List[Pagepayload]**](Pagepayload.md) | List of sub-pages | [optional] 
**soft_deleted** | **bool** | If false, restore the thing from the soft deletion | [optional] [default to False]
**widgets** | [**List[Widgetv3]**](Widgetv3.md) | Widgets attached to this dashboard | [optional] 

## Example

```python
from iot_api_client.models.dashboardv3 import Dashboardv3

# TODO update the JSON string below
json = "{}"
# create an instance of Dashboardv3 from a JSON string
dashboardv3_instance = Dashboardv3.from_json(json)
# print the JSON string representation of the object
print(Dashboardv3.to_json())

# convert the object into a dict
dashboardv3_dict = dashboardv3_instance.to_dict()
# create an instance of Dashboardv3 from a dict
dashboardv3_from_dict = Dashboardv3.from_dict(dashboardv3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



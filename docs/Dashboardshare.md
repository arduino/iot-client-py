# Dashboardshare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The userID of the user you want to share the dashboard with | [optional] 
**username** | **str** | The username of the user you want to share the dashboard with | [optional] 

## Example

```python
from iot_api_client.models.dashboardshare import Dashboardshare

# TODO update the JSON string below
json = "{}"
# create an instance of Dashboardshare from a JSON string
dashboardshare_instance = Dashboardshare.from_json(json)
# print the JSON string representation of the object
print(Dashboardshare.to_json())

# convert the object into a dict
dashboardshare_dict = dashboardshare_instance.to_dict()
# create an instance of Dashboardshare from a dict
dashboardshare_from_dict = Dashboardshare.from_dict(dashboardshare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



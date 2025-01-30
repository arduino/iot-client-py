# Usershare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The userID of the user you want to share the dashboard with | [optional] 
**username** | **str** | The username of the user you want to share the dashboard with | [optional] 

## Example

```python
from iot_api_client.models.usershare import Usershare

# TODO update the JSON string below
json = "{}"
# create an instance of Usershare from a JSON string
usershare_instance = Usershare.from_json(json)
# print the JSON string representation of the object
print(Usershare.to_json())

# convert the object into a dict
usershare_dict = usershare_instance.to_dict()
# create an instance of Usershare from a dict
usershare_from_dict = Usershare.from_dict(usershare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



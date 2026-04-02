# Pagepayload

Page describes a dashboard page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** | The icon of the Page | [optional] 
**id** | **str** | The id of the Page | 
**name** | **str** | The name of the Page | 
**position** | **int** | The position of the Page | 

## Example

```python
from iot_api_client.models.pagepayload import Pagepayload

# TODO update the JSON string below
json = "{}"
# create an instance of Pagepayload from a JSON string
pagepayload_instance = Pagepayload.from_json(json)
# print the JSON string representation of the object
print(Pagepayload.to_json())

# convert the object into a dict
pagepayload_dict = pagepayload_instance.to_dict()
# create an instance of Pagepayload from a dict
pagepayload_from_dict = Pagepayload.from_dict(pagepayload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



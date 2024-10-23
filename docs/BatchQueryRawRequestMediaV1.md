# BatchQueryRawRequestMediaV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** | From timestamp | [optional] 
**q** | **str** | Data selection query (e.g. property.2a99729d-2556-4220-a139-023348a1e6b5 or thing.95717675-4786-4ffc-afcc-799777755391) | 
**series_limit** | **int** | Maximum number of values returned, if any (default/limit: 1000, 10000 in case of thing query) | [optional] 
**sort** | **str** | Sorting | [optional] [default to 'DESC']
**to** | **datetime** | To timestamp | [optional] 

## Example

```python
from iot_api_client.models.batch_query_raw_request_media_v1 import BatchQueryRawRequestMediaV1

# TODO update the JSON string below
json = "{}"
# create an instance of BatchQueryRawRequestMediaV1 from a JSON string
batch_query_raw_request_media_v1_instance = BatchQueryRawRequestMediaV1.from_json(json)
# print the JSON string representation of the object
print(BatchQueryRawRequestMediaV1.to_json())

# convert the object into a dict
batch_query_raw_request_media_v1_dict = batch_query_raw_request_media_v1_instance.to_dict()
# create an instance of BatchQueryRawRequestMediaV1 from a dict
batch_query_raw_request_media_v1_from_dict = BatchQueryRawRequestMediaV1.from_dict(batch_query_raw_request_media_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BatchQueryRequestMediaV1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **str** | Aggregation statistic function. For numeric values, AVG statistic is used by default. PCT_X compute the Xth approximate percentile (e.g. PCT_95 is the 95th approximate percentile). For boolean, BOOL_OR statistic is used as default. | [optional] 
**var_from** | **datetime** | From timestamp | 
**interval** | **int** | Resolution in seconds (max allowed: 86400) | [optional] 
**q** | **str** | Data selection query (e.g. property.2a99729d-2556-4220-a139-023348a1e6b5 or thing.95717675-4786-4ffc-afcc-799777755391) | 
**series_limit** | **int** | Maximum number of values returned after data aggregation, if any (default: 300, limit: 1000 - 10000 in case of thing query) | [optional] 
**to** | **datetime** | To timestamp | 

## Example

```python
from iot_api_client.models.batch_query_request_media_v1 import BatchQueryRequestMediaV1

# TODO update the JSON string below
json = "{}"
# create an instance of BatchQueryRequestMediaV1 from a JSON string
batch_query_request_media_v1_instance = BatchQueryRequestMediaV1.from_json(json)
# print the JSON string representation of the object
print BatchQueryRequestMediaV1.to_json()

# convert the object into a dict
batch_query_request_media_v1_dict = batch_query_request_media_v1_instance.to_dict()
# create an instance of BatchQueryRequestMediaV1 from a dict
batch_query_request_media_v1_form_dict = batch_query_request_media_v1.from_dict(batch_query_request_media_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



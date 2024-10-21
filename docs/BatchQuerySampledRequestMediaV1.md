# BatchQuerySampledRequestMediaV1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** | From timestamp (default: now UTC - 24h) | [optional] 
**interval** | **int** | Resolution in seconds (allowed min:60, max:86400) | [optional] [default to 300]
**q** | **str** | Data selection query (e.g. property.2a99729d-2556-4220-a139-023348a1e6b5) | 
**series_limit** | **int** | Maximum number of values returned after data aggregation, if any (default: 300, limit: 1000) | [optional] 
**to** | **datetime** | To timestamp (default: now UTC) | [optional] 

## Example

```python
from iot_api_client.models.batch_query_sampled_request_media_v1 import BatchQuerySampledRequestMediaV1

# TODO update the JSON string below
json = "{}"
# create an instance of BatchQuerySampledRequestMediaV1 from a JSON string
batch_query_sampled_request_media_v1_instance = BatchQuerySampledRequestMediaV1.from_json(json)
# print the JSON string representation of the object
print BatchQuerySampledRequestMediaV1.to_json()

# convert the object into a dict
batch_query_sampled_request_media_v1_dict = batch_query_sampled_request_media_v1_instance.to_dict()
# create an instance of BatchQuerySampledRequestMediaV1 from a dict
batch_query_sampled_request_media_v1_form_dict = batch_query_sampled_request_media_v1.from_dict(batch_query_sampled_request_media_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



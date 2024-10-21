# BatchQuerySampledRequestsMediaV1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BatchQuerySampledRequestMediaV1]**](BatchQuerySampledRequestMediaV1.md) | Requests | 
**resp_version** | **int** | Response version | 

## Example

```python
from iot_api_client.models.batch_query_sampled_requests_media_v1 import BatchQuerySampledRequestsMediaV1

# TODO update the JSON string below
json = "{}"
# create an instance of BatchQuerySampledRequestsMediaV1 from a JSON string
batch_query_sampled_requests_media_v1_instance = BatchQuerySampledRequestsMediaV1.from_json(json)
# print the JSON string representation of the object
print BatchQuerySampledRequestsMediaV1.to_json()

# convert the object into a dict
batch_query_sampled_requests_media_v1_dict = batch_query_sampled_requests_media_v1_instance.to_dict()
# create an instance of BatchQuerySampledRequestsMediaV1 from a dict
batch_query_sampled_requests_media_v1_form_dict = batch_query_sampled_requests_media_v1.from_dict(batch_query_sampled_requests_media_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



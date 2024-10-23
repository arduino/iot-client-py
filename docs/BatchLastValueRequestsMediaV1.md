# BatchLastValueRequestsMediaV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[BatchQueryRawLastValueRequestMediaV1]**](BatchQueryRawLastValueRequestMediaV1.md) | Requests | 

## Example

```python
from iot_api_client.models.batch_last_value_requests_media_v1 import BatchLastValueRequestsMediaV1

# TODO update the JSON string below
json = "{}"
# create an instance of BatchLastValueRequestsMediaV1 from a JSON string
batch_last_value_requests_media_v1_instance = BatchLastValueRequestsMediaV1.from_json(json)
# print the JSON string representation of the object
print(BatchLastValueRequestsMediaV1.to_json())

# convert the object into a dict
batch_last_value_requests_media_v1_dict = batch_last_value_requests_media_v1_instance.to_dict()
# create an instance of BatchLastValueRequestsMediaV1 from a dict
batch_last_value_requests_media_v1_from_dict = BatchLastValueRequestsMediaV1.from_dict(batch_last_value_requests_media_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



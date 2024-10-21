# Error

Error response media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | an application-specific error code, expressed as a string value. | [optional] 
**detail** | **str** | a human-readable explanation specific to this occurrence of the problem. | [optional] 
**id** | **str** | a unique identifier for this particular occurrence of the problem. | [optional] 
**meta** | **Dict[str, object]** | a meta object containing non-standard meta-information about the error. | [optional] 
**status** | **int** | the HTTP status code applicable to this problem | [optional] 

## Example

```python
from iot_api_client.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print Error.to_json()

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_form_dict = error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



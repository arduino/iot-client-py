# BodyExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Content of the body of a message, variables are allowed | 
**variables** | [**List[Variable]**](Variable.md) | Variables used by the expression | [optional] 

## Example

```python
from iot_api_client.models.body_expression import BodyExpression

# TODO update the JSON string below
json = "{}"
# create an instance of BodyExpression from a JSON string
body_expression_instance = BodyExpression.from_json(json)
# print the JSON string representation of the object
print(BodyExpression.to_json())

# convert the object into a dict
body_expression_dict = body_expression_instance.to_dict()
# create an instance of BodyExpression from a dict
body_expression_from_dict = BodyExpression.from_dict(body_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



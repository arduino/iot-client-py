# TitleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Content of the title (or subject) of a message, variables are allowed | 
**variables** | [**List[Variable]**](Variable.md) | Variables used by the expression | [optional] 

## Example

```python
from iot_api_client.models.title_expression import TitleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of TitleExpression from a JSON string
title_expression_instance = TitleExpression.from_json(json)
# print the JSON string representation of the object
print(TitleExpression.to_json())

# convert the object into a dict
title_expression_dict = title_expression_instance.to_dict()
# create an instance of TitleExpression from a dict
title_expression_from_dict = TitleExpression.from_dict(title_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Template

TemplatePayload describes the needed attribute to apply a template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_template_id** | **str** | The name of the directory on S3 bucket containing the user&#39;s template | [optional] 
**prefix_name** | **str** | The prefix to apply to the names of the generated resources | [optional] 
**template_name** | **str** | The name of the directory on S3 bucket containing the template | 
**things_options** | **Dict[str, object]** |  | [optional] 

## Example

```python
from iot_api_client.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



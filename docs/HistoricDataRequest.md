# HistoricDataRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** | Get data starting from this date | 
**properties** | **List[str]** | IDs of properties | 
**to** | **datetime** | Get data up to this date | 

## Example

```python
from iot_api_client.models.historic_data_request import HistoricDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HistoricDataRequest from a JSON string
historic_data_request_instance = HistoricDataRequest.from_json(json)
# print the JSON string representation of the object
print HistoricDataRequest.to_json()

# convert the object into a dict
historic_data_request_dict = historic_data_request_instance.to_dict()
# create an instance of HistoricDataRequest from a dict
historic_data_request_form_dict = historic_data_request.from_dict(historic_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



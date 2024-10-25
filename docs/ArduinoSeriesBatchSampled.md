# ArduinoSeriesBatchSampled

ArduinoSeriesBatchSampled media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp_version** | **int** | Response version | 
**responses** | [**List[ArduinoSeriesSampledResponse]**](ArduinoSeriesSampledResponse.md) | Responses of the request | 

## Example

```python
from iot_api_client.models.arduino_series_batch_sampled import ArduinoSeriesBatchSampled

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoSeriesBatchSampled from a JSON string
arduino_series_batch_sampled_instance = ArduinoSeriesBatchSampled.from_json(json)
# print the JSON string representation of the object
print(ArduinoSeriesBatchSampled.to_json())

# convert the object into a dict
arduino_series_batch_sampled_dict = arduino_series_batch_sampled_instance.to_dict()
# create an instance of ArduinoSeriesBatchSampled from a dict
arduino_series_batch_sampled_from_dict = ArduinoSeriesBatchSampled.from_dict(arduino_series_batch_sampled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



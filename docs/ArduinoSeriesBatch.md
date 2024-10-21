# ArduinoSeriesBatch

ArduinoSeriesBatch media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp_version** | **int** | Response version | 
**responses** | [**List[ArduinoSeriesResponse]**](ArduinoSeriesResponse.md) | Responses of the request | 

## Example

```python
from iot_api_client.models.arduino_series_batch import ArduinoSeriesBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoSeriesBatch from a JSON string
arduino_series_batch_instance = ArduinoSeriesBatch.from_json(json)
# print the JSON string representation of the object
print ArduinoSeriesBatch.to_json()

# convert the object into a dict
arduino_series_batch_dict = arduino_series_batch_instance.to_dict()
# create an instance of ArduinoSeriesBatch from a dict
arduino_series_batch_form_dict = arduino_series_batch.from_dict(arduino_series_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



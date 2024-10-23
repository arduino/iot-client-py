# ArduinoSeriesRawBatch

ArduinoSeriesRawBatch media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resp_version** | **int** | Response version | 
**responses** | [**List[ArduinoSeriesRawResponse]**](ArduinoSeriesRawResponse.md) | Responses of the request | 

## Example

```python
from iot_api_client.models.arduino_series_raw_batch import ArduinoSeriesRawBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoSeriesRawBatch from a JSON string
arduino_series_raw_batch_instance = ArduinoSeriesRawBatch.from_json(json)
# print the JSON string representation of the object
print(ArduinoSeriesRawBatch.to_json())

# convert the object into a dict
arduino_series_raw_batch_dict = arduino_series_raw_batch_instance.to_dict()
# create an instance of ArduinoSeriesRawBatch from a dict
arduino_series_raw_batch_from_dict = ArduinoSeriesRawBatch.from_dict(arduino_series_raw_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



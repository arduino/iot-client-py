# ArduinoSeriesRawBatchLastvalue

ArduinoSeriesRawBatchLastvalue media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**List[ArduinoSeriesRawLastValueResponse]**](ArduinoSeriesRawLastValueResponse.md) | Responses of the request | 
**status** | **str** | Status of the response | 

## Example

```python
from iot_api_client.models.arduino_series_raw_batch_lastvalue import ArduinoSeriesRawBatchLastvalue

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoSeriesRawBatchLastvalue from a JSON string
arduino_series_raw_batch_lastvalue_instance = ArduinoSeriesRawBatchLastvalue.from_json(json)
# print the JSON string representation of the object
print(ArduinoSeriesRawBatchLastvalue.to_json())

# convert the object into a dict
arduino_series_raw_batch_lastvalue_dict = arduino_series_raw_batch_lastvalue_instance.to_dict()
# create an instance of ArduinoSeriesRawBatchLastvalue from a dict
arduino_series_raw_batch_lastvalue_from_dict = ArduinoSeriesRawBatchLastvalue.from_dict(arduino_series_raw_batch_lastvalue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArduinoDevicev2Webhook

DeviceWebhookV2 describes a webhook associated to the device (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the webhook is active | [optional] [default to True]
**id** | **str** | The uuid of the webhook | 
**uri** | **str** | The uri of the webhook | 

## Example

```python
from iot_api_client.models.arduino_devicev2_webhook import ArduinoDevicev2Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2Webhook from a JSON string
arduino_devicev2_webhook_instance = ArduinoDevicev2Webhook.from_json(json)
# print the JSON string representation of the object
print ArduinoDevicev2Webhook.to_json()

# convert the object into a dict
arduino_devicev2_webhook_dict = arduino_devicev2_webhook_instance.to_dict()
# create an instance of ArduinoDevicev2Webhook from a dict
arduino_devicev2_webhook_form_dict = arduino_devicev2_webhook.from_dict(arduino_devicev2_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# iot_api_client.model.arduino_dashboardv2.ArduinoDashboardv2

Dashboard is a collection of widgets (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Dashboard is a collection of widgets (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**updated_at** | str, datetime,  | str,  | Last update date | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The friendly name of the dashboard | 
**id** | str, uuid.UUID,  | str,  | The friendly name of the dashboard | value must be a uuid
**created_by** | [**ArduinoDashboardowner**](ArduinoDashboardowner.md) | [**ArduinoDashboardowner**](ArduinoDashboardowner.md) |  | [optional] 
**organization_id** | str, uuid.UUID,  | str,  | Id of the organization the dashboard belongs to | [optional] value must be a uuid
**shared_by** | [**ArduinoDashboardshare**](ArduinoDashboardshare.md) | [**ArduinoDashboardshare**](ArduinoDashboardshare.md) |  | [optional] 
**shared_with** | [**ArduinoDashboardshareCollection**](ArduinoDashboardshareCollection.md) | [**ArduinoDashboardshareCollection**](ArduinoDashboardshareCollection.md) |  | [optional] 
**widgets** | [**ArduinoWidgetv2Collection**](ArduinoWidgetv2Collection.md) | [**ArduinoWidgetv2Collection**](ArduinoWidgetv2Collection.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


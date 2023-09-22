# iot_api_client.model.model_property.ModelProperty

PropertyPayload describes a property of a thing. No field is mandatory

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PropertyPayload describes a property of a thing. No field is mandatory | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_strategy** | str,  | str,  | The update strategy for the property value | must be one of ["ON_CHANGE", "TIMED", ] 
**name** | str,  | str,  | The friendly name of the property | 
**permission** | str,  | str,  | The permission of the property | must be one of ["READ_ONLY", "READ_WRITE", ] 
**type** | str,  | str,  | The type of the property | must be one of ["ANALOG", "CHARSTRING", "FLOAT", "INT", "LENGHT_C", "LENGHT_I", "LENGHT_M", "PERCENTAGE", "STATUS", "TEMPERATURE_C", "TEMPERATURE_F", "METER", "KILOGRAM", "GRAM", "SECOND", "AMPERE", "KELVIN", "CANDELA", "MOLE", "HERTZ", "RADIAN", "STERADIAN", "NEWTON", "PASCAL", "JOULE", "WATT", "COULOMB", "VOLT", "FARAD", "OHM", "SIEMENS", "WEBER", "TESLA", "HENRY", "DEGREES_CELSIUS", "LUMEN", "LUX", "BECQUEREL", "GRAY", "SIEVERT", "KATAL", "SQUARE_METER", "CUBIC_METER", "LITER", "METER_PER_SECOND", "METER_PER_SQUARE_SECOND", "CUBIC_METER_PER_SECOND", "LITER_PER_SECOND", "WATT_PER_SQUARE_METER", "CANDELA_PER_SQUARE_METER", "BIT", "BIT_PER_SECOND", "DEGREES_LATITUDE", "DEGREES_LONGITUDE", "PH_VALUE", "DECIBEL", "DECIBEL_1W", "BEL", "COUNT", "RATIO_DIV", "RATIO_MOD", "PERCENTAGE_RELATIVE_HUMIDITY", "PERCENTAGE_BATTERY_LEVEL", "SECONDS_BATTERY_LEVEL", "EVENT_RATE_SECOND", "EVENT_RATE_MINUTE", "HEART_RATE", "HEART_BEATS", "SIEMENS_PER_METER", "LOCATION", "COLOR_HSB", "COLOR_RGB", "GENERIC_COMPLEX_PROPERTY", "HOME_COLORED_LIGHT", "HOME_DIMMED_LIGHT", "HOME_LIGHT", "HOME_CONTACT_SENSOR", "HOME_MOTION_SENSOR", "HOME_SMART_PLUG", "HOME_TEMPERATURE", "HOME_TEMPERATURE_C", "HOME_TEMPERATURE_F", "HOME_SWITCH", "HOME_TELEVISION", "ENERGY", "FORCE", "TEMPERATURE", "POWER", "ELECTRIC_CURRENT", "ELECTRIC_POTENTIAL", "ELECTRICAL_RESISTANCE", "CAPACITANCE", "TIME", "FREQUENCY", "DATA_RATE", "ACCELERATION", "AREA", "LENGTH", "VELOCITY", "MASS", "VOLUME", "FLOW_RATE", "ANGLE", "ILLUMINANCE", "LUMINOUS_FLUX", "LUMINANCE", "LUMINOUS_INTENSITY", "LOGARITHMIC_QUANTITY", "PRESSURE", "INFORMATION_CONTENT", "SCHEDULE", ] 
**max_value** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum value of this property | [optional] value must be a 64 bit float
**min_value** | decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum value of this property | [optional] value must be a 64 bit float
**persist** | bool,  | BoolClass,  | If true, data will persist into a timeseries database | [optional] if omitted the server will use the default value of True
**tag** | decimal.Decimal, int, float,  | decimal.Decimal,  | The integer id of the property | [optional] value must be a 64 bit float
**update_parameter** | decimal.Decimal, int, float,  | decimal.Decimal,  | The update frequency in seconds, or the amount of the property has to change in order to trigger an update | [optional] value must be a 64 bit float
**variable_name** | str,  | str,  | The  sketch variable name of the property | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from iot_api_client.paths.v2_series_historic_data import Api

from iot_api_client.paths import PathValues

path = PathValues.V2_SERIES_HISTORIC_DATA
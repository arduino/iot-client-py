# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from iot_api_client.paths.v2_devices_id_ota_url import Api

from iot_api_client.paths import PathValues

path = PathValues.V2_DEVICES_ID_OTA_URL
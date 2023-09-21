# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from iot_api_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    DASHBOARDS_V2 = "dashboards_v2"
    DEVICES_V2 = "devices_v2"
    DEVICES_V2_CERTS = "devices_v2_certs"
    DEVICES_V2_OTA = "devices_v2_ota"
    DEVICES_V2_PASS = "devices_v2_pass"
    DEVICES_V2_TAGS = "devices_v2_tags"
    LORA_DEVICES_V1 = "lora_devices_v1"
    LORA_FREQ_PLAN_V1 = "lora_freq_plan_v1"
    PROPERTIES_V2 = "properties_v2"
    SERIES_V2 = "series_v2"
    THINGS_V2 = "things_v2"
    THINGS_V2_TAGS = "things_v2_tags"

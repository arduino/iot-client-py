# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from iot_api_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_LORADEVICES_ = "/v1/lora-devices/"
    V1_LORAFREQPLANS_ = "/v1/lora-freq-plans/"
    V2_DASHBOARDS = "/v2/dashboards"
    V2_DASHBOARDS_ID = "/v2/dashboards/{id}"
    V2_DASHBOARDS_ID_SHARE_REQUEST = "/v2/dashboards/{id}/share_request"
    V2_DASHBOARDS_ID_SHARES = "/v2/dashboards/{id}/shares"
    V2_DASHBOARDS_ID_SHARES_USER_ID = "/v2/dashboards/{id}/shares/{user_id}"
    V2_DASHBOARDS_ID_WIDGETS_WIDGET_ID_VARIABLES = "/v2/dashboards/{id}/widgets/{widgetId}/variables"
    V2_DEVICES = "/v2/devices"
    V2_DEVICES_ID = "/v2/devices/{id}"
    V2_DEVICES_ID_CERTS = "/v2/devices/{id}/certs"
    V2_DEVICES_ID_CERTS_CID = "/v2/devices/{id}/certs/{cid}"
    V2_DEVICES_ID_EVENTS = "/v2/devices/{id}/events"
    V2_DEVICES_ID_OTA = "/v2/devices/{id}/ota"
    V2_DEVICES_ID_PASS = "/v2/devices/{id}/pass"
    V2_DEVICES_ID_PROPERTIES = "/v2/devices/{id}/properties"
    V2_DEVICES_ID_PROPERTIES_PID = "/v2/devices/{id}/properties/{pid}"
    V2_DEVICES_ID_TAGS = "/v2/devices/{id}/tags"
    V2_DEVICES_ID_TAGS_KEY = "/v2/devices/{id}/tags/{key}"
    V2_SERIES_BATCH_QUERY = "/v2/series/batch_query"
    V2_SERIES_BATCH_QUERY_RAW = "/v2/series/batch_query_raw"
    V2_SERIES_BATCH_QUERY_RAW_LASTVALUE = "/v2/series/batch_query_raw/lastvalue"
    V2_SERIES_HISTORIC_DATA = "/v2/series/historic_data"
    V2_THINGS = "/v2/things"
    V2_THINGS_ID = "/v2/things/{id}"
    V2_THINGS_ID_PROPERTIES = "/v2/things/{id}/properties"
    V2_THINGS_ID_PROPERTIES_PID = "/v2/things/{id}/properties/{pid}"
    V2_THINGS_ID_PROPERTIES_PID_PUBLISH = "/v2/things/{id}/properties/{pid}/publish"
    V2_THINGS_ID_PROPERTIES_PID_TIMESERIES = "/v2/things/{id}/properties/{pid}/timeseries"
    V2_THINGS_ID_SKETCH = "/v2/things/{id}/sketch"
    V2_THINGS_ID_SKETCH_SKETCH_ID = "/v2/things/{id}/sketch/{sketchId}"
    V2_THINGS_ID_TAGS = "/v2/things/{id}/tags"
    V2_THINGS_ID_TAGS_KEY = "/v2/things/{id}/tags/{key}"

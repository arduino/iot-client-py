import typing_extensions

from iot_api_client.paths import PathValues
from iot_api_client.apis.paths.v1_lora_devices_ import V1LoraDevices
from iot_api_client.apis.paths.v1_lora_freq_plans_ import V1LoraFreqPlans
from iot_api_client.apis.paths.v2_dashboards import V2Dashboards
from iot_api_client.apis.paths.v2_dashboards_id import V2DashboardsId
from iot_api_client.apis.paths.v2_dashboards_id_share_request import V2DashboardsIdShareRequest
from iot_api_client.apis.paths.v2_dashboards_id_shares import V2DashboardsIdShares
from iot_api_client.apis.paths.v2_dashboards_id_shares_user_id import V2DashboardsIdSharesUserId
from iot_api_client.apis.paths.v2_dashboards_id_widgets_widget_id_variables import V2DashboardsIdWidgetsWidgetIdVariables
from iot_api_client.apis.paths.v2_devices import V2Devices
from iot_api_client.apis.paths.v2_devices_id import V2DevicesId
from iot_api_client.apis.paths.v2_devices_id_certs import V2DevicesIdCerts
from iot_api_client.apis.paths.v2_devices_id_certs_cid import V2DevicesIdCertsCid
from iot_api_client.apis.paths.v2_devices_id_events import V2DevicesIdEvents
from iot_api_client.apis.paths.v2_devices_id_ota import V2DevicesIdOta
from iot_api_client.apis.paths.v2_devices_id_pass import V2DevicesIdPass
from iot_api_client.apis.paths.v2_devices_id_properties import V2DevicesIdProperties
from iot_api_client.apis.paths.v2_devices_id_properties_pid import V2DevicesIdPropertiesPid
from iot_api_client.apis.paths.v2_devices_id_tags import V2DevicesIdTags
from iot_api_client.apis.paths.v2_devices_id_tags_key import V2DevicesIdTagsKey
from iot_api_client.apis.paths.v2_series_batch_query import V2SeriesBatchQuery
from iot_api_client.apis.paths.v2_series_batch_query_raw import V2SeriesBatchQueryRaw
from iot_api_client.apis.paths.v2_series_batch_query_raw_lastvalue import V2SeriesBatchQueryRawLastvalue
from iot_api_client.apis.paths.v2_series_historic_data import V2SeriesHistoricData
from iot_api_client.apis.paths.v2_things import V2Things
from iot_api_client.apis.paths.v2_things_id import V2ThingsId
from iot_api_client.apis.paths.v2_things_id_properties import V2ThingsIdProperties
from iot_api_client.apis.paths.v2_things_id_properties_pid import V2ThingsIdPropertiesPid
from iot_api_client.apis.paths.v2_things_id_properties_pid_publish import V2ThingsIdPropertiesPidPublish
from iot_api_client.apis.paths.v2_things_id_properties_pid_timeseries import V2ThingsIdPropertiesPidTimeseries
from iot_api_client.apis.paths.v2_things_id_sketch import V2ThingsIdSketch
from iot_api_client.apis.paths.v2_things_id_sketch_sketch_id import V2ThingsIdSketchSketchId
from iot_api_client.apis.paths.v2_things_id_tags import V2ThingsIdTags
from iot_api_client.apis.paths.v2_things_id_tags_key import V2ThingsIdTagsKey

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_LORADEVICES_: V1LoraDevices,
        PathValues.V1_LORAFREQPLANS_: V1LoraFreqPlans,
        PathValues.V2_DASHBOARDS: V2Dashboards,
        PathValues.V2_DASHBOARDS_ID: V2DashboardsId,
        PathValues.V2_DASHBOARDS_ID_SHARE_REQUEST: V2DashboardsIdShareRequest,
        PathValues.V2_DASHBOARDS_ID_SHARES: V2DashboardsIdShares,
        PathValues.V2_DASHBOARDS_ID_SHARES_USER_ID: V2DashboardsIdSharesUserId,
        PathValues.V2_DASHBOARDS_ID_WIDGETS_WIDGET_ID_VARIABLES: V2DashboardsIdWidgetsWidgetIdVariables,
        PathValues.V2_DEVICES: V2Devices,
        PathValues.V2_DEVICES_ID: V2DevicesId,
        PathValues.V2_DEVICES_ID_CERTS: V2DevicesIdCerts,
        PathValues.V2_DEVICES_ID_CERTS_CID: V2DevicesIdCertsCid,
        PathValues.V2_DEVICES_ID_EVENTS: V2DevicesIdEvents,
        PathValues.V2_DEVICES_ID_OTA: V2DevicesIdOta,
        PathValues.V2_DEVICES_ID_PASS: V2DevicesIdPass,
        PathValues.V2_DEVICES_ID_PROPERTIES: V2DevicesIdProperties,
        PathValues.V2_DEVICES_ID_PROPERTIES_PID: V2DevicesIdPropertiesPid,
        PathValues.V2_DEVICES_ID_TAGS: V2DevicesIdTags,
        PathValues.V2_DEVICES_ID_TAGS_KEY: V2DevicesIdTagsKey,
        PathValues.V2_SERIES_BATCH_QUERY: V2SeriesBatchQuery,
        PathValues.V2_SERIES_BATCH_QUERY_RAW: V2SeriesBatchQueryRaw,
        PathValues.V2_SERIES_BATCH_QUERY_RAW_LASTVALUE: V2SeriesBatchQueryRawLastvalue,
        PathValues.V2_SERIES_HISTORIC_DATA: V2SeriesHistoricData,
        PathValues.V2_THINGS: V2Things,
        PathValues.V2_THINGS_ID: V2ThingsId,
        PathValues.V2_THINGS_ID_PROPERTIES: V2ThingsIdProperties,
        PathValues.V2_THINGS_ID_PROPERTIES_PID: V2ThingsIdPropertiesPid,
        PathValues.V2_THINGS_ID_PROPERTIES_PID_PUBLISH: V2ThingsIdPropertiesPidPublish,
        PathValues.V2_THINGS_ID_PROPERTIES_PID_TIMESERIES: V2ThingsIdPropertiesPidTimeseries,
        PathValues.V2_THINGS_ID_SKETCH: V2ThingsIdSketch,
        PathValues.V2_THINGS_ID_SKETCH_SKETCH_ID: V2ThingsIdSketchSketchId,
        PathValues.V2_THINGS_ID_TAGS: V2ThingsIdTags,
        PathValues.V2_THINGS_ID_TAGS_KEY: V2ThingsIdTagsKey,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_LORADEVICES_: V1LoraDevices,
        PathValues.V1_LORAFREQPLANS_: V1LoraFreqPlans,
        PathValues.V2_DASHBOARDS: V2Dashboards,
        PathValues.V2_DASHBOARDS_ID: V2DashboardsId,
        PathValues.V2_DASHBOARDS_ID_SHARE_REQUEST: V2DashboardsIdShareRequest,
        PathValues.V2_DASHBOARDS_ID_SHARES: V2DashboardsIdShares,
        PathValues.V2_DASHBOARDS_ID_SHARES_USER_ID: V2DashboardsIdSharesUserId,
        PathValues.V2_DASHBOARDS_ID_WIDGETS_WIDGET_ID_VARIABLES: V2DashboardsIdWidgetsWidgetIdVariables,
        PathValues.V2_DEVICES: V2Devices,
        PathValues.V2_DEVICES_ID: V2DevicesId,
        PathValues.V2_DEVICES_ID_CERTS: V2DevicesIdCerts,
        PathValues.V2_DEVICES_ID_CERTS_CID: V2DevicesIdCertsCid,
        PathValues.V2_DEVICES_ID_EVENTS: V2DevicesIdEvents,
        PathValues.V2_DEVICES_ID_OTA: V2DevicesIdOta,
        PathValues.V2_DEVICES_ID_PASS: V2DevicesIdPass,
        PathValues.V2_DEVICES_ID_PROPERTIES: V2DevicesIdProperties,
        PathValues.V2_DEVICES_ID_PROPERTIES_PID: V2DevicesIdPropertiesPid,
        PathValues.V2_DEVICES_ID_TAGS: V2DevicesIdTags,
        PathValues.V2_DEVICES_ID_TAGS_KEY: V2DevicesIdTagsKey,
        PathValues.V2_SERIES_BATCH_QUERY: V2SeriesBatchQuery,
        PathValues.V2_SERIES_BATCH_QUERY_RAW: V2SeriesBatchQueryRaw,
        PathValues.V2_SERIES_BATCH_QUERY_RAW_LASTVALUE: V2SeriesBatchQueryRawLastvalue,
        PathValues.V2_SERIES_HISTORIC_DATA: V2SeriesHistoricData,
        PathValues.V2_THINGS: V2Things,
        PathValues.V2_THINGS_ID: V2ThingsId,
        PathValues.V2_THINGS_ID_PROPERTIES: V2ThingsIdProperties,
        PathValues.V2_THINGS_ID_PROPERTIES_PID: V2ThingsIdPropertiesPid,
        PathValues.V2_THINGS_ID_PROPERTIES_PID_PUBLISH: V2ThingsIdPropertiesPidPublish,
        PathValues.V2_THINGS_ID_PROPERTIES_PID_TIMESERIES: V2ThingsIdPropertiesPidTimeseries,
        PathValues.V2_THINGS_ID_SKETCH: V2ThingsIdSketch,
        PathValues.V2_THINGS_ID_SKETCH_SKETCH_ID: V2ThingsIdSketchSketchId,
        PathValues.V2_THINGS_ID_TAGS: V2ThingsIdTags,
        PathValues.V2_THINGS_ID_TAGS_KEY: V2ThingsIdTagsKey,
    }
)

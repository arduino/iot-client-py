import typing_extensions

from iot_api_client.apis.tags import TagValues
from iot_api_client.apis.tags.dashboards_v2_api import DashboardsV2Api
from iot_api_client.apis.tags.devices_v2_api import DevicesV2Api
from iot_api_client.apis.tags.devices_v2_certs_api import DevicesV2CertsApi
from iot_api_client.apis.tags.devices_v2_ota_api import DevicesV2OtaApi
from iot_api_client.apis.tags.devices_v2_pass_api import DevicesV2PassApi
from iot_api_client.apis.tags.devices_v2_tags_api import DevicesV2TagsApi
from iot_api_client.apis.tags.lora_devices_v1_api import LoraDevicesV1Api
from iot_api_client.apis.tags.lora_freq_plan_v1_api import LoraFreqPlanV1Api
from iot_api_client.apis.tags.network_credentials_v1_api import NetworkCredentialsV1Api
from iot_api_client.apis.tags.properties_v2_api import PropertiesV2Api
from iot_api_client.apis.tags.property_types_v1_api import PropertyTypesV1Api
from iot_api_client.apis.tags.series_v2_api import SeriesV2Api
from iot_api_client.apis.tags.templates_api import TemplatesApi
from iot_api_client.apis.tags.things_v2_api import ThingsV2Api
from iot_api_client.apis.tags.things_v2_tags_api import ThingsV2TagsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DASHBOARDS_V2: DashboardsV2Api,
        TagValues.DEVICES_V2: DevicesV2Api,
        TagValues.DEVICES_V2_CERTS: DevicesV2CertsApi,
        TagValues.DEVICES_V2_OTA: DevicesV2OtaApi,
        TagValues.DEVICES_V2_PASS: DevicesV2PassApi,
        TagValues.DEVICES_V2_TAGS: DevicesV2TagsApi,
        TagValues.LORA_DEVICES_V1: LoraDevicesV1Api,
        TagValues.LORA_FREQ_PLAN_V1: LoraFreqPlanV1Api,
        TagValues.NETWORK_CREDENTIALS_V1: NetworkCredentialsV1Api,
        TagValues.PROPERTIES_V2: PropertiesV2Api,
        TagValues.PROPERTY_TYPES_V1: PropertyTypesV1Api,
        TagValues.SERIES_V2: SeriesV2Api,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.THINGS_V2: ThingsV2Api,
        TagValues.THINGS_V2_TAGS: ThingsV2TagsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DASHBOARDS_V2: DashboardsV2Api,
        TagValues.DEVICES_V2: DevicesV2Api,
        TagValues.DEVICES_V2_CERTS: DevicesV2CertsApi,
        TagValues.DEVICES_V2_OTA: DevicesV2OtaApi,
        TagValues.DEVICES_V2_PASS: DevicesV2PassApi,
        TagValues.DEVICES_V2_TAGS: DevicesV2TagsApi,
        TagValues.LORA_DEVICES_V1: LoraDevicesV1Api,
        TagValues.LORA_FREQ_PLAN_V1: LoraFreqPlanV1Api,
        TagValues.NETWORK_CREDENTIALS_V1: NetworkCredentialsV1Api,
        TagValues.PROPERTIES_V2: PropertiesV2Api,
        TagValues.PROPERTY_TYPES_V1: PropertyTypesV1Api,
        TagValues.SERIES_V2: SeriesV2Api,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.THINGS_V2: ThingsV2Api,
        TagValues.THINGS_V2_TAGS: ThingsV2TagsApi,
    }
)

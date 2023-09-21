from iot_api_client.paths.v2_devices_id.get import ApiForget
from iot_api_client.paths.v2_devices_id.post import ApiForpost
from iot_api_client.paths.v2_devices_id.delete import ApiFordelete


class V2DevicesId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

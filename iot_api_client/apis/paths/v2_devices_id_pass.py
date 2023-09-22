from iot_api_client.paths.v2_devices_id_pass.get import ApiForget
from iot_api_client.paths.v2_devices_id_pass.put import ApiForput
from iot_api_client.paths.v2_devices_id_pass.post import ApiForpost
from iot_api_client.paths.v2_devices_id_pass.delete import ApiFordelete


class V2DevicesIdPass(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass

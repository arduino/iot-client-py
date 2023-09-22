from iot_api_client.paths.v2_things_id.get import ApiForget
from iot_api_client.paths.v2_things_id.post import ApiForpost
from iot_api_client.paths.v2_things_id.delete import ApiFordelete


class V2ThingsId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass

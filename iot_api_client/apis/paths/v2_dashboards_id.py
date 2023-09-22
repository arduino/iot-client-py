from iot_api_client.paths.v2_dashboards_id.get import ApiForget
from iot_api_client.paths.v2_dashboards_id.put import ApiForput
from iot_api_client.paths.v2_dashboards_id.delete import ApiFordelete


class V2DashboardsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass

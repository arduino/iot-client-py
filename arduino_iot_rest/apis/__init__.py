
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.devices_v2_api import DevicesV2Api
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from arduino_iot_rest.api.devices_v2_api import DevicesV2Api
from arduino_iot_rest.api.devices_v2_certs_api import DevicesV2CertsApi
from arduino_iot_rest.api.devices_v2_pass_api import DevicesV2PassApi
from arduino_iot_rest.api.properties_v2_api import PropertiesV2Api
from arduino_iot_rest.api.series_v2_api import SeriesV2Api
from arduino_iot_rest.api.things_v2_api import ThingsV2Api

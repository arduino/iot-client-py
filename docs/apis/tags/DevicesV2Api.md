<a name="__pageTop"></a>
# iot_api_client.apis.tags.devices_v2_api.DevicesV2Api

All URIs are relative to *https://api2.arduino.cc/iot*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_v2_create**](#devices_v2_create) | **put** /v2/devices | create devices_v2
[**devices_v2_delete**](#devices_v2_delete) | **delete** /v2/devices/{id} | delete devices_v2
[**devices_v2_get_events**](#devices_v2_get_events) | **get** /v2/devices/{id}/events | getEvents devices_v2
[**devices_v2_get_properties**](#devices_v2_get_properties) | **get** /v2/devices/{id}/properties | getProperties devices_v2
[**devices_v2_get_status_events**](#devices_v2_get_status_events) | **get** /v2/devices/{id}/status | GetStatusEvents devices_v2
[**devices_v2_list**](#devices_v2_list) | **get** /v2/devices | list devices_v2
[**devices_v2_show**](#devices_v2_show) | **get** /v2/devices/{id} | show devices_v2
[**devices_v2_timeseries**](#devices_v2_timeseries) | **get** /v2/devices/{id}/properties/{pid} | timeseries devices_v2
[**devices_v2_update**](#devices_v2_update) | **post** /v2/devices/{id} | update devices_v2
[**devices_v2_update_properties**](#devices_v2_update_properties) | **put** /v2/devices/{id}/properties | updateProperties devices_v2

# **devices_v2_create**
<a name="devices_v2_create"></a>
> ArduinoDevicev2 devices_v2_create(create_devices_v2_payload)

create devices_v2

Creates a new device associated to the user.

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_api
from iot_api_client.model.arduino_devicev2 import ArduinoDevicev2
from iot_api_client.model.create_devices_v2_payload import CreateDevicesV2Payload
from iot_api_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_api.DevicesV2Api(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = CreateDevicesV2Payload(
        connection_type="wifi",
        fqbn="fqbn_example",
        name="0",
        serial="0",
        type="mkrwifi1010",
        user_id="user_id_example",
        wifi_fw_version="9072888001528021798096225500850762068629339333975650685139102691291.0.0+RjsmInY9s-EmMH6kw8gsnXv2Z7jRPK542XGp8ZohR8p.ziKqEde8fXg9wdpfxa2-zRi2iAxU4NCUavTrirUe4ba7JnjrgEdBCJE-ArE6U3CZ-Vnrj9RmauFxv71lRsCjOv6MeuvKG.DRGKUIQ8yNXhXoEdbZpGptfI4pvLXGuLk-kwwO2jcMEEkIa.W5ApNaDi5ackLaR2kw9-zmvqRnM-dar09VaHCQz0TlT4b42Jml4PJXMbVMO8G0e5q9Z4WMWovY63Gk6ixTd5NxR.25mQYd6VBLRGkQ5H9-FH2v5iUaMQ6iIJ-7auxDSR-lIIfhhw9bP3XhsKpT6YkX2ymMVY.YsFBx8OyxaBZ75cAidDZ6lvrLQxekRdyiJFjhCbEZunVXTqV3VP-DPQpzY-c9WhD1h649MeAEDz67NG9dihNlL1.PO1GvRUDnbsR0-SswaNzc7s9ONPZw-HNPtVfykpnotMPK4.qhv7VjToBNn1oLFWRpSx-dyd2clYhZAGiUmDTPB5iVX1lhmY7Gh2I3pT2S.uv6.tyxEBpX6RQusWUzrY2Ial.FJfz8Zwx6YGCNhQCndVdQ8Zqh8o9Fu3-luW1PzrlptgIbB7lMjnQXJdim087U4e00bXYP.263P2Qk0LGzQ-Q5b8qpf900OPrJ7NsXeu0SeHiC.or8kJwu9CQe1tTxWk3GoxqObZMXxUrU.PuO24.6xCEEGYs5NZ9BhURG1p1vKPKEsa.a3pD3hXM15Q-LQUOofFYT6wb4OCgvTgDaAqbKuYurrDjTDCxu.ecKtov6lMCwqpGvF10AyNzlABWKNXeFooO85mDfPdkPvuMP4UItRxglXsbfmNlQ5dxg25oBYSAJH9pP2AsvJ1ScQkpdOFo.b48VqkgYNMd7LrDcYKGedFO0HBfI81yv9G-D76SNMcY0UPPPdI22mRwN8gXBGGp92k53.1KEc7ag0ak9ETa6LnPl34V.5Jc4YC3r.ILhaa6Jcc4hzAqllACM9319wGio4p44OFkGlPpgNlbtJZS0AaW9X3CHj-n2hyQAB8SPpfju.1nTBPTJPb-Hj0L.cV6H860Rpwn8zGLfibFlAiPGyvhU8Ye52iQcNh1XhyIjU5N0a56m2ONPCsy2yJE2MQH9Vtj3dWmBLqET.auRy5wUhGt7xNZoWfe9JGrar3ZeHRc4dSsd0RIlQ1YUo31fGOwi1Xfgv.he4JPG5EYj9qSsH3icZps5aXdx--TYsRRGn8p-Q2t9ufMVk0G3LCRAkC2MHGjLeFDChVzm1sl-Bu5nHUPV3JcSLLtzHgWd203hy.cgItmozD9jSoTmmDlQzmeuMjs4cmyHkc7OcK.a5ZkmXKIhuWWL1PB8JQFInAlUihvIRKWmd74vVNVouUUq7lr13izMpQeXTwCX7eZR4diuBp12rqic.-pO1cprK6eZP-b1SuInOS2bPzpLsEcDg9JOefS2IKCBgZkZN1VM5iisCMqqvZJfQbTm0l8TqUvVVYQzBM3pTF3YFunJjn79r.X76dFbUfrQdC.CsMXdVXhXKWhK7aKxfLZMGV1t5ZLSwBhCBeSp3g1WqnxFKTMlmqL5kYD0D-.lZnDQWB6CfFrfdWw.lB5yxG2ZsNwUTxPepPDck0MHjx1bWWkthueuyZwIYJFC-DP.pDz0q9BcSZ9lSO3Fm1Aw-wm4asDrqk8Aqw1gHodBjUGpKTy8xuN4TvW3wydnv61CL6-Ma55v-.ci4bPbKvnn4ON1zDx0RE5Nx-CnGmqNNhQQuMJYkjplO3Qdqu9Y32Xmk.ws1aTVFSrXW-Cc3Zlfh6YwbO-wd61ok6dkgj3fNOb.daoZA1F02Pi3WxdBRfK7kZq-foRRQUAGEMz-biz--psyEvzi6C8Y89wwxrOADQYuRsYgAFe.Oz26sXflDj3ZKPbb.5LwwjHM1Zfj0bJ3cHAnEwK3LXdBrD99XSqFR6aV9uyoVGq.EJe-wvWZmWi.Ihctr-seZcIsU78A-6.6uPNyWu.as5q7-lfce9-8Do101kYW1tCLjm3EPHhKxm.hBJAlXkoQZqOkDB7wcPWkqotc6fQJs52.QKpgtkhgJP2pCWDIqetgTZsY7xlN3E7zxLDrXBGblu1s7At6U2M5I0H33HhkJRPicrz91Mnqr4yUQy3nOCQv4yqY.M8d7UUXqQdz8ORLX7PhYoA5ITVLr1rCs1.daEl0tG5if.npOOAVHva9i7wKGIOmsYkpwPB08qBqbgiKD8h-jhgoAD6oEaEIg9hqdBk87piJu2fHTHWNw1WGbDvKMClEM0pWG7gx2yb.AuT6q1dUrLCN6NPK0brTSwMFavOBDfYh6SWUkJ7XO32vfW9YRga.03cIqVgnG7dDviEQYeYsVp6bNv9XqJoDDSwcwkJvnEdiYdDcVLlRMsgGfQl-tGvdMnDqnxRe7EAipxSvUxD6lhGX0wQGc87.OhmM3dQkRuht7pIqysrRPSNqVg2qV7yPxS6zN1jFxe9RVYcK-J.hbgms67HfNYbVp9oaT6x-W9PX5eTeltcxj.VBajOnyD0pkOF1WFBnF.mcWC6Ggb7ozlleM8QgTjBaA9mfSMCxZLogapWzy373M4zkkTNr-J5dkUMXZbHzFcOhyLEEaimeL.3YKjuAetlS3KzQ3re5yyNydVmSrcU07T2IefMatN.9EwBjoSdfp0qUZT9ZEikdceGh-PrN5eZiRnbnxhaAGJdNWy8YuT1nhbdHhnszeIEGYoiOAz3w8t8JeOqP.8wcdt3n9Q18SKzea-IlLBLRzcEhoqVuUCEMQ93-aK7kTUKwGpNFs6oxf4rK2c2cqKr6NdT0mVcCzXpEYgd4j2pfz2OhgwjH.7.TeTNn-kC1tWGTwvSe04Vuj8uQ5FMrHjWbBFGHMprQcHDQ9X.R45mJyb0kvP09gLqmLT2ZBctrFe4rKz49D.bgU2rmVhxKQwKj2CvvcelO-a4qXa3zFRMnF0L.Tb2XXgfhZnLhogeg-lX38MmIJ9H8.woZJXltyMySvaJ2YVjDcbdQ3VQQRHJW1zsoJEJN7qLewjxfK3R3vVJYDnMtqbnX0dYax2JyQF6TkCgEBc.KhM4sm4rjZsdx7lu4l53pRPPb8XS149u1VRYFMhW1wn.rzgV53Dpcj0YE965xb8tPZiBI",
    )
    try:
        # create devices_v2
        api_response = api_instance.devices_v2_create(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_create: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = CreateDevicesV2Payload(
        connection_type="wifi",
        fqbn="fqbn_example",
        name="0",
        serial="0",
        type="mkrwifi1010",
        user_id="user_id_example",
        wifi_fw_version="9072888001528021798096225500850762068629339333975650685139102691291.0.0+RjsmInY9s-EmMH6kw8gsnXv2Z7jRPK542XGp8ZohR8p.ziKqEde8fXg9wdpfxa2-zRi2iAxU4NCUavTrirUe4ba7JnjrgEdBCJE-ArE6U3CZ-Vnrj9RmauFxv71lRsCjOv6MeuvKG.DRGKUIQ8yNXhXoEdbZpGptfI4pvLXGuLk-kwwO2jcMEEkIa.W5ApNaDi5ackLaR2kw9-zmvqRnM-dar09VaHCQz0TlT4b42Jml4PJXMbVMO8G0e5q9Z4WMWovY63Gk6ixTd5NxR.25mQYd6VBLRGkQ5H9-FH2v5iUaMQ6iIJ-7auxDSR-lIIfhhw9bP3XhsKpT6YkX2ymMVY.YsFBx8OyxaBZ75cAidDZ6lvrLQxekRdyiJFjhCbEZunVXTqV3VP-DPQpzY-c9WhD1h649MeAEDz67NG9dihNlL1.PO1GvRUDnbsR0-SswaNzc7s9ONPZw-HNPtVfykpnotMPK4.qhv7VjToBNn1oLFWRpSx-dyd2clYhZAGiUmDTPB5iVX1lhmY7Gh2I3pT2S.uv6.tyxEBpX6RQusWUzrY2Ial.FJfz8Zwx6YGCNhQCndVdQ8Zqh8o9Fu3-luW1PzrlptgIbB7lMjnQXJdim087U4e00bXYP.263P2Qk0LGzQ-Q5b8qpf900OPrJ7NsXeu0SeHiC.or8kJwu9CQe1tTxWk3GoxqObZMXxUrU.PuO24.6xCEEGYs5NZ9BhURG1p1vKPKEsa.a3pD3hXM15Q-LQUOofFYT6wb4OCgvTgDaAqbKuYurrDjTDCxu.ecKtov6lMCwqpGvF10AyNzlABWKNXeFooO85mDfPdkPvuMP4UItRxglXsbfmNlQ5dxg25oBYSAJH9pP2AsvJ1ScQkpdOFo.b48VqkgYNMd7LrDcYKGedFO0HBfI81yv9G-D76SNMcY0UPPPdI22mRwN8gXBGGp92k53.1KEc7ag0ak9ETa6LnPl34V.5Jc4YC3r.ILhaa6Jcc4hzAqllACM9319wGio4p44OFkGlPpgNlbtJZS0AaW9X3CHj-n2hyQAB8SPpfju.1nTBPTJPb-Hj0L.cV6H860Rpwn8zGLfibFlAiPGyvhU8Ye52iQcNh1XhyIjU5N0a56m2ONPCsy2yJE2MQH9Vtj3dWmBLqET.auRy5wUhGt7xNZoWfe9JGrar3ZeHRc4dSsd0RIlQ1YUo31fGOwi1Xfgv.he4JPG5EYj9qSsH3icZps5aXdx--TYsRRGn8p-Q2t9ufMVk0G3LCRAkC2MHGjLeFDChVzm1sl-Bu5nHUPV3JcSLLtzHgWd203hy.cgItmozD9jSoTmmDlQzmeuMjs4cmyHkc7OcK.a5ZkmXKIhuWWL1PB8JQFInAlUihvIRKWmd74vVNVouUUq7lr13izMpQeXTwCX7eZR4diuBp12rqic.-pO1cprK6eZP-b1SuInOS2bPzpLsEcDg9JOefS2IKCBgZkZN1VM5iisCMqqvZJfQbTm0l8TqUvVVYQzBM3pTF3YFunJjn79r.X76dFbUfrQdC.CsMXdVXhXKWhK7aKxfLZMGV1t5ZLSwBhCBeSp3g1WqnxFKTMlmqL5kYD0D-.lZnDQWB6CfFrfdWw.lB5yxG2ZsNwUTxPepPDck0MHjx1bWWkthueuyZwIYJFC-DP.pDz0q9BcSZ9lSO3Fm1Aw-wm4asDrqk8Aqw1gHodBjUGpKTy8xuN4TvW3wydnv61CL6-Ma55v-.ci4bPbKvnn4ON1zDx0RE5Nx-CnGmqNNhQQuMJYkjplO3Qdqu9Y32Xmk.ws1aTVFSrXW-Cc3Zlfh6YwbO-wd61ok6dkgj3fNOb.daoZA1F02Pi3WxdBRfK7kZq-foRRQUAGEMz-biz--psyEvzi6C8Y89wwxrOADQYuRsYgAFe.Oz26sXflDj3ZKPbb.5LwwjHM1Zfj0bJ3cHAnEwK3LXdBrD99XSqFR6aV9uyoVGq.EJe-wvWZmWi.Ihctr-seZcIsU78A-6.6uPNyWu.as5q7-lfce9-8Do101kYW1tCLjm3EPHhKxm.hBJAlXkoQZqOkDB7wcPWkqotc6fQJs52.QKpgtkhgJP2pCWDIqetgTZsY7xlN3E7zxLDrXBGblu1s7At6U2M5I0H33HhkJRPicrz91Mnqr4yUQy3nOCQv4yqY.M8d7UUXqQdz8ORLX7PhYoA5ITVLr1rCs1.daEl0tG5if.npOOAVHva9i7wKGIOmsYkpwPB08qBqbgiKD8h-jhgoAD6oEaEIg9hqdBk87piJu2fHTHWNw1WGbDvKMClEM0pWG7gx2yb.AuT6q1dUrLCN6NPK0brTSwMFavOBDfYh6SWUkJ7XO32vfW9YRga.03cIqVgnG7dDviEQYeYsVp6bNv9XqJoDDSwcwkJvnEdiYdDcVLlRMsgGfQl-tGvdMnDqnxRe7EAipxSvUxD6lhGX0wQGc87.OhmM3dQkRuht7pIqysrRPSNqVg2qV7yPxS6zN1jFxe9RVYcK-J.hbgms67HfNYbVp9oaT6x-W9PX5eTeltcxj.VBajOnyD0pkOF1WFBnF.mcWC6Ggb7ozlleM8QgTjBaA9mfSMCxZLogapWzy373M4zkkTNr-J5dkUMXZbHzFcOhyLEEaimeL.3YKjuAetlS3KzQ3re5yyNydVmSrcU07T2IefMatN.9EwBjoSdfp0qUZT9ZEikdceGh-PrN5eZiRnbnxhaAGJdNWy8YuT1nhbdHhnszeIEGYoiOAz3w8t8JeOqP.8wcdt3n9Q18SKzea-IlLBLRzcEhoqVuUCEMQ93-aK7kTUKwGpNFs6oxf4rK2c2cqKr6NdT0mVcCzXpEYgd4j2pfz2OhgwjH.7.TeTNn-kC1tWGTwvSe04Vuj8uQ5FMrHjWbBFGHMprQcHDQ9X.R45mJyb0kvP09gLqmLT2ZBctrFe4rKz49D.bgU2rmVhxKQwKj2CvvcelO-a4qXa3zFRMnF0L.Tb2XXgfhZnLhogeg-lX38MmIJ9H8.woZJXltyMySvaJ2YVjDcbdQ3VQQRHJW1zsoJEJN7qLewjxfK3R3vVJYDnMtqbnX0dYax2JyQF6TkCgEBc.KhM4sm4rjZsdx7lu4l53pRPPb8XS149u1VRYFMhW1wn.rzgV53Dpcj0YE965xb8tPZiBI",
    )
    try:
        # create devices_v2
        api_response = api_instance.devices_v2_create(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.devicev2+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDevicesV2Payload**](../../models/CreateDevicesV2Payload.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateDevicesV2Payload**](../../models/CreateDevicesV2Payload.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#devices_v2_create.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#devices_v2_create.ApiResponseFor401) | Unauthorized
412 | [ApiResponseFor412](#devices_v2_create.ApiResponseFor412) | Precondition Failed
500 | [ApiResponseFor500](#devices_v2_create.ApiResponseFor500) | Internal Server Error

#### devices_v2_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndArduinoDevicev2json, SchemaFor201ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationVndArduinoDevicev2json
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2**](../../models/ArduinoDevicev2.md) |  | 


# SchemaFor201ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2**](../../models/ArduinoDevicev2.md) |  | 


#### devices_v2_create.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoDevicev2json, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoDevicev2json
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_create.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor412ResponseBodyApplicationVndArduinoDevicev2json, SchemaFor412ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor412ResponseBodyApplicationVndArduinoDevicev2json
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor412ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_create.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoDevicev2json, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoDevicev2json
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_delete**
<a name="devices_v2_delete"></a>
> devices_v2_delete(id)

delete devices_v2

Removes a device associated to the user

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_api
from iot_api_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_api.DevicesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    try:
        # delete devices_v2
        api_response = api_instance.devices_v2_delete(
            path_params=path_params,
            header_params=header_params,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # delete devices_v2
        api_response = api_instance.devices_v2_delete(
            path_params=path_params,
            header_params=header_params,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.goa.error+json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_delete.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#devices_v2_delete.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#devices_v2_delete.ApiResponseFor500) | Internal Server Error

#### devices_v2_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndGoaErrorjson, SchemaFor401ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndGoaErrorjson, SchemaFor500ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_get_events**
<a name="devices_v2_get_events"></a>
> ArduinoDevicev2EventProperties devices_v2_get_events(id)

getEvents devices_v2

GET device events

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_devicev2_event_properties import ArduinoDevicev2EventProperties
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_api.DevicesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # getEvents devices_v2
        api_response = api_instance.devices_v2_get_events(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_get_events: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'limit': 1,
        'start': "start_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # getEvents devices_v2
        api_response = api_instance.devices_v2_get_events(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_get_events: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.devicev2.event.properties+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
start | StartSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_get_events.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#devices_v2_get_events.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#devices_v2_get_events.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#devices_v2_get_events.ApiResponseFor503) | Service Unavailable

#### devices_v2_get_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoDevicev2EventPropertiesjson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoDevicev2EventPropertiesjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2EventProperties**](../../models/ArduinoDevicev2EventProperties.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2EventProperties**](../../models/ArduinoDevicev2EventProperties.md) |  | 


#### devices_v2_get_events.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoDevicev2EventPropertiesjson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoDevicev2EventPropertiesjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_get_events.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoDevicev2EventPropertiesjson, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoDevicev2EventPropertiesjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_get_events.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationVndArduinoDevicev2EventPropertiesjson, SchemaFor503ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationVndArduinoDevicev2EventPropertiesjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor503ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_get_properties**
<a name="devices_v2_get_properties"></a>
> ArduinoDevicev2properties devices_v2_get_properties(id)

getProperties devices_v2

GET device properties

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_api
from iot_api_client.model.arduino_devicev2properties import ArduinoDevicev2properties
from iot_api_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_api.DevicesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # getProperties devices_v2
        api_response = api_instance.devices_v2_get_properties(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_get_properties: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'show_deleted': False,
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # getProperties devices_v2
        api_response = api_instance.devices_v2_get_properties(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_get_properties: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.devicev2properties+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
show_deleted | ShowDeletedSchema | | optional


# ShowDeletedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_get_properties.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#devices_v2_get_properties.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#devices_v2_get_properties.ApiResponseFor500) | Internal Server Error

#### devices_v2_get_properties.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoDevicev2propertiesjson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoDevicev2propertiesjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2properties**](../../models/ArduinoDevicev2properties.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2properties**](../../models/ArduinoDevicev2properties.md) |  | 


#### devices_v2_get_properties.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoDevicev2propertiesjson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoDevicev2propertiesjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_get_properties.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoDevicev2propertiesjson, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoDevicev2propertiesjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_get_status_events**
<a name="devices_v2_get_status_events"></a>
> ArduinoDevicev2StatusEvents devices_v2_get_status_events(id)

GetStatusEvents devices_v2

GET connection status events

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_devicev2_status_events import ArduinoDevicev2StatusEvents
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_api.DevicesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # GetStatusEvents devices_v2
        api_response = api_instance.devices_v2_get_status_events(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_get_status_events: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'limit': 30,
        'start': "start_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # GetStatusEvents devices_v2
        api_response = api_instance.devices_v2_get_status_events(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_get_status_events: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.devicev2.status.events+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
start | StartSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 30

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_get_status_events.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#devices_v2_get_status_events.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#devices_v2_get_status_events.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#devices_v2_get_status_events.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#devices_v2_get_status_events.ApiResponseFor503) | Service Unavailable

#### devices_v2_get_status_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoDevicev2StatusEventsjson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoDevicev2StatusEventsjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2StatusEvents**](../../models/ArduinoDevicev2StatusEvents.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2StatusEvents**](../../models/ArduinoDevicev2StatusEvents.md) |  | 


#### devices_v2_get_status_events.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndArduinoDevicev2StatusEventsjson, SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndArduinoDevicev2StatusEventsjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_get_status_events.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoDevicev2StatusEventsjson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoDevicev2StatusEventsjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_get_status_events.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoDevicev2StatusEventsjson, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoDevicev2StatusEventsjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_get_status_events.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationVndArduinoDevicev2StatusEventsjson, SchemaFor503ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationVndArduinoDevicev2StatusEventsjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor503ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_list**
<a name="devices_v2_list"></a>
> ArduinoDevicev2Collection devices_v2_list()

list devices_v2

Returns the list of devices associated to the user

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_devicev2_collection import ArduinoDevicev2Collection
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_api.DevicesV2Api(api_client)

    # example passing only optional values
    query_params = {
        'across_user_ids': False,
        'serial': "serial_example",
        'tags': [
        "0:@9JLe6iL71-aa-.Ctq@dcsc.3-8@1gAa8Xa6u61"
    ],
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # list devices_v2
        api_response = api_instance.devices_v2_list(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.devicev2+json; type&#x3D;collection', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
across_user_ids | AcrossUserIdsSchema | | optional
serial | SerialSchema | | optional
tags | TagsSchema | | optional


# AcrossUserIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# SerialSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_list.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#devices_v2_list.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#devices_v2_list.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#devices_v2_list.ApiResponseFor500) | Internal Server Error

#### devices_v2_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoDevicev2jsonTypecollection, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoDevicev2jsonTypecollection
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2Collection**](../../models/ArduinoDevicev2Collection.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2Collection**](../../models/ArduinoDevicev2Collection.md) |  | 


#### devices_v2_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndArduinoDevicev2jsonTypecollection, SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndArduinoDevicev2jsonTypecollection
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_list.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoDevicev2jsonTypecollection, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoDevicev2jsonTypecollection
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_list.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoDevicev2jsonTypecollection, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoDevicev2jsonTypecollection
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_show**
<a name="devices_v2_show"></a>
> ArduinoDevicev2 devices_v2_show(id)

show devices_v2

Returns the device requested by the user

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_api
from iot_api_client.model.arduino_devicev2 import ArduinoDevicev2
from iot_api_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_api.DevicesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    try:
        # show devices_v2
        api_response = api_instance.devices_v2_show(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_show: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # show devices_v2
        api_response = api_instance.devices_v2_show(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_show: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.devicev2+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_show.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#devices_v2_show.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#devices_v2_show.ApiResponseFor500) | Internal Server Error

#### devices_v2_show.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoDevicev2json, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoDevicev2json
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2**](../../models/ArduinoDevicev2.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2**](../../models/ArduinoDevicev2.md) |  | 


#### devices_v2_show.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoDevicev2json, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoDevicev2json
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_show.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoDevicev2json, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoDevicev2json
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_timeseries**
<a name="devices_v2_timeseries"></a>
> ArduinoDevicev2propertyvalues devices_v2_timeseries(idpid)

timeseries devices_v2

GET device properties values in a range of time

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_api
from iot_api_client.model.error import Error
from iot_api_client.model.arduino_devicev2propertyvalues import ArduinoDevicev2propertyvalues
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_api.DevicesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # timeseries devices_v2
        api_response = api_instance.devices_v2_timeseries(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_timeseries: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
        'pid': "pid_example",
    }
    query_params = {
        'limit': 1,
        'start': "start_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    try:
        # timeseries devices_v2
        api_response = api_instance.devices_v2_timeseries(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_timeseries: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.devicev2propertyvalues+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
limit | LimitSchema | | optional
start | StartSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
pid | PidSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_timeseries.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#devices_v2_timeseries.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#devices_v2_timeseries.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#devices_v2_timeseries.ApiResponseFor500) | Internal Server Error

#### devices_v2_timeseries.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoDevicev2propertyvaluesjson, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoDevicev2propertyvaluesjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2propertyvalues**](../../models/ArduinoDevicev2propertyvalues.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2propertyvalues**](../../models/ArduinoDevicev2propertyvalues.md) |  | 


#### devices_v2_timeseries.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndArduinoDevicev2propertyvaluesjson, SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndArduinoDevicev2propertyvaluesjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_timeseries.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoDevicev2propertyvaluesjson, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoDevicev2propertyvaluesjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_timeseries.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoDevicev2propertyvaluesjson, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoDevicev2propertyvaluesjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_update**
<a name="devices_v2_update"></a>
> ArduinoDevicev2 devices_v2_update(iddevicev2)

update devices_v2

Updates a device associated to the user

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_api
from iot_api_client.model.arduino_devicev2 import ArduinoDevicev2
from iot_api_client.model.devicev2 import Devicev2
from iot_api_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_api.DevicesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    body = Devicev2(
        connection_type="wifi",
        fqbn="fqbn_example",
        name="0",
        serial="0",
        type="mkrwifi1010",
        user_id="user_id_example",
        wifi_fw_version="9072888001528021798096225500850762068629339333975650685139102691291.0.0+RjsmInY9s-EmMH6kw8gsnXv2Z7jRPK542XGp8ZohR8p.ziKqEde8fXg9wdpfxa2-zRi2iAxU4NCUavTrirUe4ba7JnjrgEdBCJE-ArE6U3CZ-Vnrj9RmauFxv71lRsCjOv6MeuvKG.DRGKUIQ8yNXhXoEdbZpGptfI4pvLXGuLk-kwwO2jcMEEkIa.W5ApNaDi5ackLaR2kw9-zmvqRnM-dar09VaHCQz0TlT4b42Jml4PJXMbVMO8G0e5q9Z4WMWovY63Gk6ixTd5NxR.25mQYd6VBLRGkQ5H9-FH2v5iUaMQ6iIJ-7auxDSR-lIIfhhw9bP3XhsKpT6YkX2ymMVY.YsFBx8OyxaBZ75cAidDZ6lvrLQxekRdyiJFjhCbEZunVXTqV3VP-DPQpzY-c9WhD1h649MeAEDz67NG9dihNlL1.PO1GvRUDnbsR0-SswaNzc7s9ONPZw-HNPtVfykpnotMPK4.qhv7VjToBNn1oLFWRpSx-dyd2clYhZAGiUmDTPB5iVX1lhmY7Gh2I3pT2S.uv6.tyxEBpX6RQusWUzrY2Ial.FJfz8Zwx6YGCNhQCndVdQ8Zqh8o9Fu3-luW1PzrlptgIbB7lMjnQXJdim087U4e00bXYP.263P2Qk0LGzQ-Q5b8qpf900OPrJ7NsXeu0SeHiC.or8kJwu9CQe1tTxWk3GoxqObZMXxUrU.PuO24.6xCEEGYs5NZ9BhURG1p1vKPKEsa.a3pD3hXM15Q-LQUOofFYT6wb4OCgvTgDaAqbKuYurrDjTDCxu.ecKtov6lMCwqpGvF10AyNzlABWKNXeFooO85mDfPdkPvuMP4UItRxglXsbfmNlQ5dxg25oBYSAJH9pP2AsvJ1ScQkpdOFo.b48VqkgYNMd7LrDcYKGedFO0HBfI81yv9G-D76SNMcY0UPPPdI22mRwN8gXBGGp92k53.1KEc7ag0ak9ETa6LnPl34V.5Jc4YC3r.ILhaa6Jcc4hzAqllACM9319wGio4p44OFkGlPpgNlbtJZS0AaW9X3CHj-n2hyQAB8SPpfju.1nTBPTJPb-Hj0L.cV6H860Rpwn8zGLfibFlAiPGyvhU8Ye52iQcNh1XhyIjU5N0a56m2ONPCsy2yJE2MQH9Vtj3dWmBLqET.auRy5wUhGt7xNZoWfe9JGrar3ZeHRc4dSsd0RIlQ1YUo31fGOwi1Xfgv.he4JPG5EYj9qSsH3icZps5aXdx--TYsRRGn8p-Q2t9ufMVk0G3LCRAkC2MHGjLeFDChVzm1sl-Bu5nHUPV3JcSLLtzHgWd203hy.cgItmozD9jSoTmmDlQzmeuMjs4cmyHkc7OcK.a5ZkmXKIhuWWL1PB8JQFInAlUihvIRKWmd74vVNVouUUq7lr13izMpQeXTwCX7eZR4diuBp12rqic.-pO1cprK6eZP-b1SuInOS2bPzpLsEcDg9JOefS2IKCBgZkZN1VM5iisCMqqvZJfQbTm0l8TqUvVVYQzBM3pTF3YFunJjn79r.X76dFbUfrQdC.CsMXdVXhXKWhK7aKxfLZMGV1t5ZLSwBhCBeSp3g1WqnxFKTMlmqL5kYD0D-.lZnDQWB6CfFrfdWw.lB5yxG2ZsNwUTxPepPDck0MHjx1bWWkthueuyZwIYJFC-DP.pDz0q9BcSZ9lSO3Fm1Aw-wm4asDrqk8Aqw1gHodBjUGpKTy8xuN4TvW3wydnv61CL6-Ma55v-.ci4bPbKvnn4ON1zDx0RE5Nx-CnGmqNNhQQuMJYkjplO3Qdqu9Y32Xmk.ws1aTVFSrXW-Cc3Zlfh6YwbO-wd61ok6dkgj3fNOb.daoZA1F02Pi3WxdBRfK7kZq-foRRQUAGEMz-biz--psyEvzi6C8Y89wwxrOADQYuRsYgAFe.Oz26sXflDj3ZKPbb.5LwwjHM1Zfj0bJ3cHAnEwK3LXdBrD99XSqFR6aV9uyoVGq.EJe-wvWZmWi.Ihctr-seZcIsU78A-6.6uPNyWu.as5q7-lfce9-8Do101kYW1tCLjm3EPHhKxm.hBJAlXkoQZqOkDB7wcPWkqotc6fQJs52.QKpgtkhgJP2pCWDIqetgTZsY7xlN3E7zxLDrXBGblu1s7At6U2M5I0H33HhkJRPicrz91Mnqr4yUQy3nOCQv4yqY.M8d7UUXqQdz8ORLX7PhYoA5ITVLr1rCs1.daEl0tG5if.npOOAVHva9i7wKGIOmsYkpwPB08qBqbgiKD8h-jhgoAD6oEaEIg9hqdBk87piJu2fHTHWNw1WGbDvKMClEM0pWG7gx2yb.AuT6q1dUrLCN6NPK0brTSwMFavOBDfYh6SWUkJ7XO32vfW9YRga.03cIqVgnG7dDviEQYeYsVp6bNv9XqJoDDSwcwkJvnEdiYdDcVLlRMsgGfQl-tGvdMnDqnxRe7EAipxSvUxD6lhGX0wQGc87.OhmM3dQkRuht7pIqysrRPSNqVg2qV7yPxS6zN1jFxe9RVYcK-J.hbgms67HfNYbVp9oaT6x-W9PX5eTeltcxj.VBajOnyD0pkOF1WFBnF.mcWC6Ggb7ozlleM8QgTjBaA9mfSMCxZLogapWzy373M4zkkTNr-J5dkUMXZbHzFcOhyLEEaimeL.3YKjuAetlS3KzQ3re5yyNydVmSrcU07T2IefMatN.9EwBjoSdfp0qUZT9ZEikdceGh-PrN5eZiRnbnxhaAGJdNWy8YuT1nhbdHhnszeIEGYoiOAz3w8t8JeOqP.8wcdt3n9Q18SKzea-IlLBLRzcEhoqVuUCEMQ93-aK7kTUKwGpNFs6oxf4rK2c2cqKr6NdT0mVcCzXpEYgd4j2pfz2OhgwjH.7.TeTNn-kC1tWGTwvSe04Vuj8uQ5FMrHjWbBFGHMprQcHDQ9X.R45mJyb0kvP09gLqmLT2ZBctrFe4rKz49D.bgU2rmVhxKQwKj2CvvcelO-a4qXa3zFRMnF0L.Tb2XXgfhZnLhogeg-lX38MmIJ9H8.woZJXltyMySvaJ2YVjDcbdQ3VQQRHJW1zsoJEJN7qLewjxfK3R3vVJYDnMtqbnX0dYax2JyQF6TkCgEBc.KhM4sm4rjZsdx7lu4l53pRPPb8XS149u1VRYFMhW1wn.rzgV53Dpcj0YE965xb8tPZiBI",
    )
    try:
        # update devices_v2
        api_response = api_instance.devices_v2_update(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_update: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = Devicev2(
        connection_type="wifi",
        fqbn="fqbn_example",
        name="0",
        serial="0",
        type="mkrwifi1010",
        user_id="user_id_example",
        wifi_fw_version="9072888001528021798096225500850762068629339333975650685139102691291.0.0+RjsmInY9s-EmMH6kw8gsnXv2Z7jRPK542XGp8ZohR8p.ziKqEde8fXg9wdpfxa2-zRi2iAxU4NCUavTrirUe4ba7JnjrgEdBCJE-ArE6U3CZ-Vnrj9RmauFxv71lRsCjOv6MeuvKG.DRGKUIQ8yNXhXoEdbZpGptfI4pvLXGuLk-kwwO2jcMEEkIa.W5ApNaDi5ackLaR2kw9-zmvqRnM-dar09VaHCQz0TlT4b42Jml4PJXMbVMO8G0e5q9Z4WMWovY63Gk6ixTd5NxR.25mQYd6VBLRGkQ5H9-FH2v5iUaMQ6iIJ-7auxDSR-lIIfhhw9bP3XhsKpT6YkX2ymMVY.YsFBx8OyxaBZ75cAidDZ6lvrLQxekRdyiJFjhCbEZunVXTqV3VP-DPQpzY-c9WhD1h649MeAEDz67NG9dihNlL1.PO1GvRUDnbsR0-SswaNzc7s9ONPZw-HNPtVfykpnotMPK4.qhv7VjToBNn1oLFWRpSx-dyd2clYhZAGiUmDTPB5iVX1lhmY7Gh2I3pT2S.uv6.tyxEBpX6RQusWUzrY2Ial.FJfz8Zwx6YGCNhQCndVdQ8Zqh8o9Fu3-luW1PzrlptgIbB7lMjnQXJdim087U4e00bXYP.263P2Qk0LGzQ-Q5b8qpf900OPrJ7NsXeu0SeHiC.or8kJwu9CQe1tTxWk3GoxqObZMXxUrU.PuO24.6xCEEGYs5NZ9BhURG1p1vKPKEsa.a3pD3hXM15Q-LQUOofFYT6wb4OCgvTgDaAqbKuYurrDjTDCxu.ecKtov6lMCwqpGvF10AyNzlABWKNXeFooO85mDfPdkPvuMP4UItRxglXsbfmNlQ5dxg25oBYSAJH9pP2AsvJ1ScQkpdOFo.b48VqkgYNMd7LrDcYKGedFO0HBfI81yv9G-D76SNMcY0UPPPdI22mRwN8gXBGGp92k53.1KEc7ag0ak9ETa6LnPl34V.5Jc4YC3r.ILhaa6Jcc4hzAqllACM9319wGio4p44OFkGlPpgNlbtJZS0AaW9X3CHj-n2hyQAB8SPpfju.1nTBPTJPb-Hj0L.cV6H860Rpwn8zGLfibFlAiPGyvhU8Ye52iQcNh1XhyIjU5N0a56m2ONPCsy2yJE2MQH9Vtj3dWmBLqET.auRy5wUhGt7xNZoWfe9JGrar3ZeHRc4dSsd0RIlQ1YUo31fGOwi1Xfgv.he4JPG5EYj9qSsH3icZps5aXdx--TYsRRGn8p-Q2t9ufMVk0G3LCRAkC2MHGjLeFDChVzm1sl-Bu5nHUPV3JcSLLtzHgWd203hy.cgItmozD9jSoTmmDlQzmeuMjs4cmyHkc7OcK.a5ZkmXKIhuWWL1PB8JQFInAlUihvIRKWmd74vVNVouUUq7lr13izMpQeXTwCX7eZR4diuBp12rqic.-pO1cprK6eZP-b1SuInOS2bPzpLsEcDg9JOefS2IKCBgZkZN1VM5iisCMqqvZJfQbTm0l8TqUvVVYQzBM3pTF3YFunJjn79r.X76dFbUfrQdC.CsMXdVXhXKWhK7aKxfLZMGV1t5ZLSwBhCBeSp3g1WqnxFKTMlmqL5kYD0D-.lZnDQWB6CfFrfdWw.lB5yxG2ZsNwUTxPepPDck0MHjx1bWWkthueuyZwIYJFC-DP.pDz0q9BcSZ9lSO3Fm1Aw-wm4asDrqk8Aqw1gHodBjUGpKTy8xuN4TvW3wydnv61CL6-Ma55v-.ci4bPbKvnn4ON1zDx0RE5Nx-CnGmqNNhQQuMJYkjplO3Qdqu9Y32Xmk.ws1aTVFSrXW-Cc3Zlfh6YwbO-wd61ok6dkgj3fNOb.daoZA1F02Pi3WxdBRfK7kZq-foRRQUAGEMz-biz--psyEvzi6C8Y89wwxrOADQYuRsYgAFe.Oz26sXflDj3ZKPbb.5LwwjHM1Zfj0bJ3cHAnEwK3LXdBrD99XSqFR6aV9uyoVGq.EJe-wvWZmWi.Ihctr-seZcIsU78A-6.6uPNyWu.as5q7-lfce9-8Do101kYW1tCLjm3EPHhKxm.hBJAlXkoQZqOkDB7wcPWkqotc6fQJs52.QKpgtkhgJP2pCWDIqetgTZsY7xlN3E7zxLDrXBGblu1s7At6U2M5I0H33HhkJRPicrz91Mnqr4yUQy3nOCQv4yqY.M8d7UUXqQdz8ORLX7PhYoA5ITVLr1rCs1.daEl0tG5if.npOOAVHva9i7wKGIOmsYkpwPB08qBqbgiKD8h-jhgoAD6oEaEIg9hqdBk87piJu2fHTHWNw1WGbDvKMClEM0pWG7gx2yb.AuT6q1dUrLCN6NPK0brTSwMFavOBDfYh6SWUkJ7XO32vfW9YRga.03cIqVgnG7dDviEQYeYsVp6bNv9XqJoDDSwcwkJvnEdiYdDcVLlRMsgGfQl-tGvdMnDqnxRe7EAipxSvUxD6lhGX0wQGc87.OhmM3dQkRuht7pIqysrRPSNqVg2qV7yPxS6zN1jFxe9RVYcK-J.hbgms67HfNYbVp9oaT6x-W9PX5eTeltcxj.VBajOnyD0pkOF1WFBnF.mcWC6Ggb7ozlleM8QgTjBaA9mfSMCxZLogapWzy373M4zkkTNr-J5dkUMXZbHzFcOhyLEEaimeL.3YKjuAetlS3KzQ3re5yyNydVmSrcU07T2IefMatN.9EwBjoSdfp0qUZT9ZEikdceGh-PrN5eZiRnbnxhaAGJdNWy8YuT1nhbdHhnszeIEGYoiOAz3w8t8JeOqP.8wcdt3n9Q18SKzea-IlLBLRzcEhoqVuUCEMQ93-aK7kTUKwGpNFs6oxf4rK2c2cqKr6NdT0mVcCzXpEYgd4j2pfz2OhgwjH.7.TeTNn-kC1tWGTwvSe04Vuj8uQ5FMrHjWbBFGHMprQcHDQ9X.R45mJyb0kvP09gLqmLT2ZBctrFe4rKz49D.bgU2rmVhxKQwKj2CvvcelO-a4qXa3zFRMnF0L.Tb2XXgfhZnLhogeg-lX38MmIJ9H8.woZJXltyMySvaJ2YVjDcbdQ3VQQRHJW1zsoJEJN7qLewjxfK3R3vVJYDnMtqbnX0dYax2JyQF6TkCgEBc.KhM4sm4rjZsdx7lu4l53pRPPb8XS149u1VRYFMhW1wn.rzgV53Dpcj0YE965xb8tPZiBI",
    )
    try:
        # update devices_v2
        api_response = api_instance.devices_v2_update(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.arduino.devicev2+json', 'application/vnd.goa.error+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Devicev2**](../../models/Devicev2.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**Devicev2**](../../models/Devicev2.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_update.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#devices_v2_update.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#devices_v2_update.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#devices_v2_update.ApiResponseFor500) | Internal Server Error

#### devices_v2_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndArduinoDevicev2json, SchemaFor200ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndArduinoDevicev2json
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2**](../../models/ArduinoDevicev2.md) |  | 


# SchemaFor200ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ArduinoDevicev2**](../../models/ArduinoDevicev2.md) |  | 


#### devices_v2_update.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationVndArduinoDevicev2json, SchemaFor400ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationVndArduinoDevicev2json
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor400ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_update.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndArduinoDevicev2json, SchemaFor401ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndArduinoDevicev2json
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_update.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndArduinoDevicev2json, SchemaFor500ResponseBodyApplicationVndGoaErrorjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndArduinoDevicev2json
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **devices_v2_update_properties**
<a name="devices_v2_update_properties"></a>
> devices_v2_update_properties(idproperties_values)

updateProperties devices_v2

Update device properties last values

### Example

* OAuth Authentication (oauth2):
```python
import iot_api_client
from iot_api_client.apis.tags import devices_v2_api
from iot_api_client.model.properties_values import PropertiesValues
from iot_api_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api2.arduino.cc/iot
# See configuration.py for a list of all supported configuration parameters.
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = iot_api_client.Configuration(
    host = "https://api2.arduino.cc/iot",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with iot_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devices_v2_api.DevicesV2Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    body = PropertiesValues(
        input=False,
        properties=[
            PropertiesValue(
                name="name_example",
                type="infer",
                value=None,
            )
        ],
    )
    try:
        # updateProperties devices_v2
        api_response = api_instance.devices_v2_update_properties(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_update_properties: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'X-Organization': "X-Organization_example",
    }
    body = PropertiesValues(
        input=False,
        properties=[
            PropertiesValue(
                name="name_example",
                type="infer",
                value=None,
            )
        ],
    )
    try:
        # updateProperties devices_v2
        api_response = api_instance.devices_v2_update_properties(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
    except iot_api_client.ApiException as e:
        print("Exception when calling DevicesV2Api->devices_v2_update_properties: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.goa.error+json', 'text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertiesValues**](../../models/PropertiesValues.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**PropertiesValues**](../../models/PropertiesValues.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Organization | XOrganizationSchema | | optional

# XOrganizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#devices_v2_update_properties.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#devices_v2_update_properties.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#devices_v2_update_properties.ApiResponseFor500) | Internal Server Error

#### devices_v2_update_properties.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### devices_v2_update_properties.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationVndGoaErrorjson, SchemaFor401ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor401ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### devices_v2_update_properties.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationVndGoaErrorjson, SchemaFor500ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationVndGoaErrorjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


# SchemaFor500ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


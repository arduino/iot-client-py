# coding: utf-8

"""
    Arduino IoT Cloud API

     Provides a set of endpoints to manage Arduino IoT Cloud **Devices**, **Things**, **Properties** and **Timeseries**. This API can be called just with any HTTP Client, or using one of these clients:  * [Javascript NPM package](https://www.npmjs.com/package/@arduino/arduino-iot-client)  * [Python PYPI Package](https://pypi.org/project/arduino-iot-client/)  * [Golang Module](https://github.com/arduino/iot-client-go)  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from iot_api_client import schemas  # noqa: F401


class ArduinoSeriesResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ArduinoSeriesResponse media type (default view)
    """


    class MetaOapg:
        required = {
            "count_values",
            "resp_version",
            "times",
            "from_date",
            "to_date",
            "query",
            "values",
            "interval",
            "status",
        }
        
        class properties:
            count_values = schemas.Int64Schema
            from_date = schemas.DateTimeSchema
            interval = schemas.Int64Schema
            query = schemas.StrSchema
            resp_version = schemas.Int64Schema
            status = schemas.StrSchema
            
            
            class times(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.DateTimeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, datetime, ]], typing.List[typing.Union[MetaOapg.items, str, datetime, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'times':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            to_date = schemas.DateTimeSchema
            
            
            class values(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Float64Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'values':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            message = schemas.StrSchema
            series_limit = schemas.Int64Schema
            __annotations__ = {
                "count_values": count_values,
                "from_date": from_date,
                "interval": interval,
                "query": query,
                "resp_version": resp_version,
                "status": status,
                "times": times,
                "to_date": to_date,
                "values": values,
                "message": message,
                "series_limit": series_limit,
            }
    
    count_values: MetaOapg.properties.count_values
    resp_version: MetaOapg.properties.resp_version
    times: MetaOapg.properties.times
    from_date: MetaOapg.properties.from_date
    to_date: MetaOapg.properties.to_date
    query: MetaOapg.properties.query
    values: MetaOapg.properties.values
    interval: MetaOapg.properties.interval
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count_values"]) -> MetaOapg.properties.count_values: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_date"]) -> MetaOapg.properties.from_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interval"]) -> MetaOapg.properties.interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resp_version"]) -> MetaOapg.properties.resp_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["times"]) -> MetaOapg.properties.times: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_date"]) -> MetaOapg.properties.to_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["values"]) -> MetaOapg.properties.values: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["series_limit"]) -> MetaOapg.properties.series_limit: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["count_values", "from_date", "interval", "query", "resp_version", "status", "times", "to_date", "values", "message", "series_limit", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count_values"]) -> MetaOapg.properties.count_values: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_date"]) -> MetaOapg.properties.from_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interval"]) -> MetaOapg.properties.interval: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resp_version"]) -> MetaOapg.properties.resp_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["times"]) -> MetaOapg.properties.times: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_date"]) -> MetaOapg.properties.to_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["values"]) -> MetaOapg.properties.values: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["series_limit"]) -> typing.Union[MetaOapg.properties.series_limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["count_values", "from_date", "interval", "query", "resp_version", "status", "times", "to_date", "values", "message", "series_limit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        count_values: typing.Union[MetaOapg.properties.count_values, decimal.Decimal, int, ],
        resp_version: typing.Union[MetaOapg.properties.resp_version, decimal.Decimal, int, ],
        times: typing.Union[MetaOapg.properties.times, list, tuple, ],
        from_date: typing.Union[MetaOapg.properties.from_date, str, datetime, ],
        to_date: typing.Union[MetaOapg.properties.to_date, str, datetime, ],
        query: typing.Union[MetaOapg.properties.query, str, ],
        values: typing.Union[MetaOapg.properties.values, list, tuple, ],
        interval: typing.Union[MetaOapg.properties.interval, decimal.Decimal, int, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        series_limit: typing.Union[MetaOapg.properties.series_limit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ArduinoSeriesResponse':
        return super().__new__(
            cls,
            *_args,
            count_values=count_values,
            resp_version=resp_version,
            times=times,
            from_date=from_date,
            to_date=to_date,
            query=query,
            values=values,
            interval=interval,
            status=status,
            message=message,
            series_limit=series_limit,
            _configuration=_configuration,
            **kwargs,
        )

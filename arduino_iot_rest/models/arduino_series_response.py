# coding: utf-8

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ArduinoSeriesResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'count_values': 'int',
        'from_date': 'datetime',
        'interval': 'int',
        'message': 'str',
        'query': 'str',
        'resp_version': 'int',
        'series_limit': 'int',
        'status': 'str',
        'times': 'list[datetime]',
        'to_date': 'datetime',
        'values': 'list[float]'
    }

    attribute_map = {
        'count_values': 'count_values',
        'from_date': 'from_date',
        'interval': 'interval',
        'message': 'message',
        'query': 'query',
        'resp_version': 'resp_version',
        'series_limit': 'series_limit',
        'status': 'status',
        'times': 'times',
        'to_date': 'to_date',
        'values': 'values'
    }

    def __init__(self, count_values=None, from_date=None, interval=None, message='', query=None, resp_version=None, series_limit=None, status=None, times=None, to_date=None, values=None):  # noqa: E501
        """ArduinoSeriesResponse - a model defined in OpenAPI"""  # noqa: E501

        self._count_values = None
        self._from_date = None
        self._interval = None
        self._message = None
        self._query = None
        self._resp_version = None
        self._series_limit = None
        self._status = None
        self._times = None
        self._to_date = None
        self._values = None
        self.discriminator = None

        self.count_values = count_values
        self.from_date = from_date
        self.interval = interval
        if message is not None:
            self.message = message
        self.query = query
        self.resp_version = resp_version
        if series_limit is not None:
            self.series_limit = series_limit
        self.status = status
        self.times = times
        self.to_date = to_date
        self.values = values

    @property
    def count_values(self):
        """Gets the count_values of this ArduinoSeriesResponse.  # noqa: E501

        Total number of values in the array 'values'  # noqa: E501

        :return: The count_values of this ArduinoSeriesResponse.  # noqa: E501
        :rtype: int
        """
        return self._count_values

    @count_values.setter
    def count_values(self, count_values):
        """Sets the count_values of this ArduinoSeriesResponse.

        Total number of values in the array 'values'  # noqa: E501

        :param count_values: The count_values of this ArduinoSeriesResponse.  # noqa: E501
        :type: int
        """
        if count_values is None:
            raise ValueError("Invalid value for `count_values`, must not be `None`")  # noqa: E501

        self._count_values = count_values

    @property
    def from_date(self):
        """Gets the from_date of this ArduinoSeriesResponse.  # noqa: E501

        From date  # noqa: E501

        :return: The from_date of this ArduinoSeriesResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this ArduinoSeriesResponse.

        From date  # noqa: E501

        :param from_date: The from_date of this ArduinoSeriesResponse.  # noqa: E501
        :type: datetime
        """
        if from_date is None:
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501

        self._from_date = from_date

    @property
    def interval(self):
        """Gets the interval of this ArduinoSeriesResponse.  # noqa: E501

        Resolution in seconds  # noqa: E501

        :return: The interval of this ArduinoSeriesResponse.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ArduinoSeriesResponse.

        Resolution in seconds  # noqa: E501

        :param interval: The interval of this ArduinoSeriesResponse.  # noqa: E501
        :type: int
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def message(self):
        """Gets the message of this ArduinoSeriesResponse.  # noqa: E501

        If the response is different than 'ok'  # noqa: E501

        :return: The message of this ArduinoSeriesResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ArduinoSeriesResponse.

        If the response is different than 'ok'  # noqa: E501

        :param message: The message of this ArduinoSeriesResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def query(self):
        """Gets the query of this ArduinoSeriesResponse.  # noqa: E501

        Query of for the data  # noqa: E501

        :return: The query of this ArduinoSeriesResponse.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ArduinoSeriesResponse.

        Query of for the data  # noqa: E501

        :param query: The query of this ArduinoSeriesResponse.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def resp_version(self):
        """Gets the resp_version of this ArduinoSeriesResponse.  # noqa: E501

        Response version  # noqa: E501

        :return: The resp_version of this ArduinoSeriesResponse.  # noqa: E501
        :rtype: int
        """
        return self._resp_version

    @resp_version.setter
    def resp_version(self, resp_version):
        """Sets the resp_version of this ArduinoSeriesResponse.

        Response version  # noqa: E501

        :param resp_version: The resp_version of this ArduinoSeriesResponse.  # noqa: E501
        :type: int
        """
        if resp_version is None:
            raise ValueError("Invalid value for `resp_version`, must not be `None`")  # noqa: E501

        self._resp_version = resp_version

    @property
    def series_limit(self):
        """Gets the series_limit of this ArduinoSeriesResponse.  # noqa: E501

        Max of values  # noqa: E501

        :return: The series_limit of this ArduinoSeriesResponse.  # noqa: E501
        :rtype: int
        """
        return self._series_limit

    @series_limit.setter
    def series_limit(self, series_limit):
        """Sets the series_limit of this ArduinoSeriesResponse.

        Max of values  # noqa: E501

        :param series_limit: The series_limit of this ArduinoSeriesResponse.  # noqa: E501
        :type: int
        """

        self._series_limit = series_limit

    @property
    def status(self):
        """Gets the status of this ArduinoSeriesResponse.  # noqa: E501

        Status of the response  # noqa: E501

        :return: The status of this ArduinoSeriesResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ArduinoSeriesResponse.

        Status of the response  # noqa: E501

        :param status: The status of this ArduinoSeriesResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def times(self):
        """Gets the times of this ArduinoSeriesResponse.  # noqa: E501

        Timestamp in RFC3339  # noqa: E501

        :return: The times of this ArduinoSeriesResponse.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._times

    @times.setter
    def times(self, times):
        """Sets the times of this ArduinoSeriesResponse.

        Timestamp in RFC3339  # noqa: E501

        :param times: The times of this ArduinoSeriesResponse.  # noqa: E501
        :type: list[datetime]
        """
        if times is None:
            raise ValueError("Invalid value for `times`, must not be `None`")  # noqa: E501

        self._times = times

    @property
    def to_date(self):
        """Gets the to_date of this ArduinoSeriesResponse.  # noqa: E501

        To date  # noqa: E501

        :return: The to_date of this ArduinoSeriesResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this ArduinoSeriesResponse.

        To date  # noqa: E501

        :param to_date: The to_date of this ArduinoSeriesResponse.  # noqa: E501
        :type: datetime
        """
        if to_date is None:
            raise ValueError("Invalid value for `to_date`, must not be `None`")  # noqa: E501

        self._to_date = to_date

    @property
    def values(self):
        """Gets the values of this ArduinoSeriesResponse.  # noqa: E501

        Values in Float  # noqa: E501

        :return: The values of this ArduinoSeriesResponse.  # noqa: E501
        :rtype: list[float]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ArduinoSeriesResponse.

        Values in Float  # noqa: E501

        :param values: The values of this ArduinoSeriesResponse.  # noqa: E501
        :type: list[float]
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArduinoSeriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

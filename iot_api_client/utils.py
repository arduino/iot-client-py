# coding: utf-8

"""
    Arduino IoT Cloud API

    Utility package
"""

import frozendict
from iot_api_client.schemas import *

class DecodeUtils(object):

    def decode_value(self, value):
        """
            Decode value from API provided DynamicSchema object to its supported subclass (like Decimal, dictionary, boolean, string)
        """
        if issubclass(value.__class__, decimal.Decimal):
            return decimal.Decimal(value)   
        if issubclass(value.__class__, str):
            return str(value)
        if issubclass(value.__class__, frozendict.frozendict):
            dict = frozendict.frozendict(value)
            decodedvals = {}
            for key in dict.keys():
                decodedvals[key] = self.decode_value(dict[key])
            return decodedvals
        if issubclass(value.__class__, BoolClass):
            relval = value.is_true_oapg()
            return relval
        return value

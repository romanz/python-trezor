# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p


class CipherKeyValue(p.MessageType):
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('key', p.UnicodeType, 0),
        3: ('value', p.BytesType, 0),
        4: ('encrypt', p.BoolType, 0),
        5: ('ask_on_encrypt', p.BoolType, 0),
        6: ('ask_on_decrypt', p.BoolType, 0),
        7: ('iv', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 23

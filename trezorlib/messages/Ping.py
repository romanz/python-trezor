# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p


class Ping(p.MessageType):
    FIELDS = {
        1: ('message', p.UnicodeType, 0),
        2: ('button_protection', p.BoolType, 0),
        3: ('pin_protection', p.BoolType, 0),
        4: ('passphrase_protection', p.BoolType, 0),
    }
    MESSAGE_WIRE_TYPE = 1

# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p
from .NEMMosaicDefinition import NEMMosaicDefinition


class NEMMosaicCreation(p.MessageType):
    FIELDS = {
        1: ('definition', NEMMosaicDefinition, 0),
        2: ('sink', p.UnicodeType, 0),
        3: ('fee', p.UVarintType, 0),
    }

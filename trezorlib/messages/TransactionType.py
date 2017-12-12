# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p
from .TxInputType import TxInputType
from .TxOutputType import TxOutputType
from .TxOutputBinType import TxOutputBinType


class TransactionType(p.MessageType):
    FIELDS = {
        1: ('version', p.UVarintType, 0),
        2: ('inputs', TxInputType, p.FLAG_REPEATED),
        3: ('bin_outputs', TxOutputBinType, p.FLAG_REPEATED),
        4: ('lock_time', p.UVarintType, 0),
        5: ('outputs', TxOutputType, p.FLAG_REPEATED),
        6: ('inputs_cnt', p.UVarintType, 0),
        7: ('outputs_cnt', p.UVarintType, 0),
        8: ('extra_data', p.BytesType, 0),
        9: ('extra_data_len', p.UVarintType, 0),
    }

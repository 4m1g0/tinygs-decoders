# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Fees(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = Fees.Header(self._io, self, self._root)
        _on = self.header.msg_type_id1
        if _on == 254:
            self._raw_payload = self._io.read_bytes((self._io.size() - 3))
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = Fees.Tmi254(_io__raw_payload, self, self._root)
        else:
            self.payload = self._io.read_bytes((self._io.size() - 3))

    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.msg_type_id0 = self._io.read_bytes(1)
            if not self.msg_type_id0 == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.msg_type_id0, self._io, u"/types/header/seq/0")
            self.msg_type_id1 = self._io.read_u1()
            self.msg_type_id2 = self._io.read_u1()


    class Tmi254(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.frame_id = self._io.read_u2le()
            self.timestamp = self._io.read_u4le()
            self.unknown2 = self._io.read_u4le()
            self.unknown3 = self._io.read_u4le()
            self.unknown4 = self._io.read_u1()
            self.unknown5 = self._io.read_u2le()
            self.vacd_2v5 = self._io.read_u2le()
            self.vbat = self._io.read_u2le()
            self.vsol = self._io.read_u2le()
            self.unknown6 = self._io.read_u2le()
            self.unknown7 = self._io.read_u2le()
            self.unknown8 = self._io.read_u2le()
            self.unknown9 = self._io.read_u2le()
            self.iload = self._io.read_u2le()
            self.icharger = self._io.read_u2le()
            self.unknown10 = self._io.read_u2le()
            self.unknown11 = self._io.read_u2le()
            self.unknown12 = self._io.read_u2le()
            self.unknown13 = self._io.read_u1()
            self.unknown14 = self._io.read_u2le()




# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Sdsat(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.payload = Sdsat.Payload(self._io, self, self._root)

    class Payload(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(18)
            if not self.magic == b"\x53\x44\x53\x41\x54\x2C\x4C\x4F\x52\x41\x20\x41\x43\x54\x49\x56\x45\x3A":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x44\x53\x41\x54\x2C\x4C\x4F\x52\x41\x20\x41\x43\x54\x49\x56\x45\x3A", self.magic, self._io, u"/types/payload/seq/0")
            self.relay_msg = (self._io.read_bytes_full()).decode(u"UTF-8")




# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Grizu(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = Grizu.Header(self._io, self, self._root)

    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.teamid = (self._io.read_bytes(6)).decode(u"ASCII")
            self.year = self._io.read_u1()
            self.month = self._io.read_u1()
            self.date = self._io.read_u1()
            self.hour = self._io.read_u1()
            self.minute = self._io.read_u1()
            self.second = self._io.read_u1()
            self.temp = self._io.read_u2le()
            self.epstoobcina1_current = self._io.read_u2le()
            self.epstoobcina1_busvoltage = self._io.read_u2le()
            self.epsina2_current = self._io.read_u2le()
            self.epsina2_busvoltage = self._io.read_u2le()
            self.baseina3_current = self._io.read_u2le()
            self.baseina3_busvoltage = self._io.read_u2le()
            self.topina4_current = self._io.read_u2le()
            self.topina4_busvoltage = self._io.read_u2le()
            self.behindantenina5_current = self._io.read_u2le()
            self.behindantenina5_busvoltage = self._io.read_u2le()
            self.rightsideina6_current = self._io.read_u2le()
            self.rightsideina6_busvoltage = self._io.read_u2le()
            self.leftsideina7_current = self._io.read_u2le()
            self.leftsideina7_busvoltage = self._io.read_u2le()
            self.imumx = self._io.read_u2le()
            self.imumy = self._io.read_u2le()
            self.imumz = self._io.read_u2le()
            self.imuax = self._io.read_u2le()
            self.imuay = self._io.read_u2le()
            self.imuaz = self._io.read_u2le()
            self.imugx = self._io.read_u2le()
            self.imugy = self._io.read_u2le()
            self.imugz = self._io.read_u2le()





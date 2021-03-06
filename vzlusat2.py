# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Vzlusat2(KaitaiStruct):
    """:field csp_hdr_crc: csp_header.crc
    :field csp_hdr_rdp: csp_header.rdp
    :field csp_hdr_xtea: csp_header.xtea
    :field csp_hdr_hmac: csp_header.hmac
    :field csp_hdr_src_port: csp_header.source_port
    :field csp_hdr_dst_port: csp_header.destination_port
    :field csp_hdr_destination: csp_header.destination
    :field csp_hdr_source: csp_header.source
    :field csp_hdr_priority: csp_header.priority
    :field obc_timestamp: csp_data.payload.obc_timestamp
    :field obc_boot_count: csp_data.payload.obc_boot_count
    :field obc_reset_cause: csp_data.payload.obc_reset_cause
    :field eps_vbatt: csp_data.payload.eps_vbatt
    :field eps_cursun: csp_data.payload.eps_cursun
    :field eps_cursys: csp_data.payload.eps_cursys
    :field eps_temp_bat: csp_data.payload.eps_temp_bat
    :field radio_temp_pa: csp_data.payload.radio_temp_pa
    :field radio_tot_tx_count: csp_data.payload.radio_tot_tx_count
    :field radio_tot_rx_count: csp_data.payload.radio_tot_rx_count
    :field flag: csp_data.payload.flag
    :field chunk: csp_data.payload.chunk
    :field time: csp_data.payload.time
    :field data: csp_data.payload.data_raw.data.data_str
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.csp_header = Vzlusat2.CspHeaderT(self._io, self, self._root)
        self.csp_data = Vzlusat2.CspDataT(self._io, self, self._root)

    class CspHeaderT(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.csp_header_raw = self._io.read_u4be()

        @property
        def source(self):
            if hasattr(self, '_m_source'):
                return self._m_source if hasattr(self, '_m_source') else None

            self._m_source = ((self.csp_header_raw >> 25) & 31)
            return self._m_source if hasattr(self, '_m_source') else None

        @property
        def source_port(self):
            if hasattr(self, '_m_source_port'):
                return self._m_source_port if hasattr(self, '_m_source_port') else None

            self._m_source_port = ((self.csp_header_raw >> 8) & 63)
            return self._m_source_port if hasattr(self, '_m_source_port') else None

        @property
        def destination_port(self):
            if hasattr(self, '_m_destination_port'):
                return self._m_destination_port if hasattr(self, '_m_destination_port') else None

            self._m_destination_port = ((self.csp_header_raw >> 14) & 63)
            return self._m_destination_port if hasattr(self, '_m_destination_port') else None

        @property
        def rdp(self):
            if hasattr(self, '_m_rdp'):
                return self._m_rdp if hasattr(self, '_m_rdp') else None

            self._m_rdp = ((self.csp_header_raw & 2) >> 1)
            return self._m_rdp if hasattr(self, '_m_rdp') else None

        @property
        def destination(self):
            if hasattr(self, '_m_destination'):
                return self._m_destination if hasattr(self, '_m_destination') else None

            self._m_destination = ((self.csp_header_raw >> 20) & 31)
            return self._m_destination if hasattr(self, '_m_destination') else None

        @property
        def priority(self):
            if hasattr(self, '_m_priority'):
                return self._m_priority if hasattr(self, '_m_priority') else None

            self._m_priority = (self.csp_header_raw >> 30)
            return self._m_priority if hasattr(self, '_m_priority') else None

        @property
        def reserved(self):
            if hasattr(self, '_m_reserved'):
                return self._m_reserved if hasattr(self, '_m_reserved') else None

            self._m_reserved = ((self.csp_header_raw >> 4) & 15)
            return self._m_reserved if hasattr(self, '_m_reserved') else None

        @property
        def xtea(self):
            if hasattr(self, '_m_xtea'):
                return self._m_xtea if hasattr(self, '_m_xtea') else None

            self._m_xtea = ((self.csp_header_raw & 4) >> 2)
            return self._m_xtea if hasattr(self, '_m_xtea') else None

        @property
        def hmac(self):
            if hasattr(self, '_m_hmac'):
                return self._m_hmac if hasattr(self, '_m_hmac') else None

            self._m_hmac = ((self.csp_header_raw & 8) >> 3)
            return self._m_hmac if hasattr(self, '_m_hmac') else None

        @property
        def crc(self):
            if hasattr(self, '_m_crc'):
                return self._m_crc if hasattr(self, '_m_crc') else None

            self._m_crc = (self.csp_header_raw & 1)
            return self._m_crc if hasattr(self, '_m_crc') else None


    class CspDataT(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cmd = self._io.read_u1()
            if  ((self._parent.csp_header.source == 1) and (self._parent.csp_header.destination == 26) and (self._parent.csp_header.source_port == 18) and (self._parent.csp_header.destination_port == 18)) :
                _on = self.cmd
                if _on == 86:
                    self.payload = Vzlusat2.Vzlusat2BeaconT(self._io, self, self._root)
                elif _on == 3:
                    self.payload = Vzlusat2.Vzlusat2DropT(self._io, self, self._root)



    class Vzlusat2BeaconT(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.callsign = self._io.read_bytes(8)
            if not self.callsign == b"\x5A\x4C\x55\x53\x41\x54\x2D\x32":
                raise kaitaistruct.ValidationNotEqualError(b"\x5A\x4C\x55\x53\x41\x54\x2D\x32", self.callsign, self._io, u"/types/vzlusat2_beacon_t/seq/0")
            self.obc_timestamp = self._io.read_u4be()
            self.obc_boot_count = self._io.read_u4be()
            self.obc_reset_cause = self._io.read_u4be()
            self.eps_vbatt = self._io.read_u2be()
            self.eps_cursun = self._io.read_u2be()
            self.eps_cursys = self._io.read_u2be()
            self.eps_temp_bat = self._io.read_s2be()
            self.radio_temp_pa_raw = self._io.read_s2be()
            self.radio_tot_tx_count = self._io.read_u4be()
            self.radio_tot_rx_count = self._io.read_u4be()

        @property
        def radio_temp_pa(self):
            if hasattr(self, '_m_radio_temp_pa'):
                return self._m_radio_temp_pa if hasattr(self, '_m_radio_temp_pa') else None

            self._m_radio_temp_pa = (0.1 * self.radio_temp_pa_raw)
            return self._m_radio_temp_pa if hasattr(self, '_m_radio_temp_pa') else None


    class Vzlusat2DropT(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.flag = self._io.read_u1()
            self.chunk = self._io.read_u4be()
            self.time = self._io.read_u4be()
            self.data_raw = self._io.read_bytes_full()




# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Norby(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = Norby.Header(self._io, self, self._root)
        _on = self.header.msg_type_id
        if _on == 0:
            self._raw_payload = self._io.read_bytes((self.header.length - 14))
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = Norby.Tmi0(_io__raw_payload, self, self._root)
        else:
            self.payload = self._io.read_bytes((self.header.length - 14))

    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.length = self._io.read_u1()
            self.receiver_address = self._io.read_u4le()
            self.transmitter_address = self._io.read_u4le()
            self.transaction_number = self._io.read_u2le()
            self.reserved = self._io.read_bytes(2)
            self.msg_type_id = self._io.read_s2be()


    class Tmi0(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.frame_start_mark = self._io.read_bytes(2)
            if not self.frame_start_mark == b"\xF1\x0F":
                raise kaitaistruct.ValidationNotEqualError(b"\xF1\x0F", self.frame_start_mark, self._io, u"/types/tmi0/seq/0")
            self.frame_definition = self._io.read_u2le()
            self.frame_number = self._io.read_u2le()
            self.frame_generation_time = self._io.read_u4le()
            self.brk_title = (self._io.read_bytes(24)).decode(u"ASCII")
            self.brk_number_active = self._io.read_u1()
            self.brk_restarts_count_active = self._io.read_s4le()
            self.brk_current_mode_id = self._io.read_u1()
            self.brk_transmitter_power_active = self._io.read_s1()
            self.brk_temp_active = self._io.read_s1()
            self.brk_module_state_active = self._io.read_bytes(2)
            self.brk_voltage_offset_amplifier_active = self._io.read_u2le()
            self.brk_last_received_packet_rssi_active = self._io.read_s1()
            self.brk_last_received_packet_snr_active = self._io.read_s1()
            self.brk_archive_record_pointer = self._io.read_u2le()
            self.brk_last_received_packet_snr_inactive = self._io.read_s1()
            self.ms_module_state = self._io.read_bytes(2)
            self.ms_payload_state = self._io.read_bytes(2)
            self.ms_temp = self._io.read_s1()
            self.ms_pn_supply_state = self._io.read_u1()
            self.sop_altitude_glonass = self._io.read_s4le()
            self.sop_latitude_glonass = self._io.read_s4le()
            self.sop_longitude_glonass = self._io.read_s4le()
            self.sop_date_time_glonass = self._io.read_u4le()
            self.sop_magnetic_induction_module = self._io.read_u2le()
            self.sop_angular_velocity_vector = self._io.read_bytes(6)
            self.sop_angle_priority1 = self._io.read_u2le()
            self.sop_angle_priority2 = self._io.read_u2le()
            self.sop_mk_temp_dsg1 = self._io.read_s1()
            self.sop_mk_temp_dsg6 = self._io.read_s1()
            self.sop_board_temp = self._io.read_s1()
            self.sop_state = self._io.read_bytes(2)
            self.sop_state_dsg = self._io.read_bytes(6)
            self.sop_orientation_number = self._io.read_u1()
            self.ses_median_panel_x_temp_positive = self._io.read_s1()
            self.ses_median_panel_x_temp_negative = self._io.read_s1()
            self.ses_solar_panels_state = self._io.read_bytes(5)
            self.ses_charge_level_m_ah = self._io.read_u2le()
            self.ses_battery_state = self._io.read_bytes(3)
            self.ses_charging_keys_state = self._io.read_bytes(2)
            self.ses_power_line_state = self._io.read_u1()
            self.ses_total_charging_power = self._io.read_s2le()
            self.ses_total_generated_power = self._io.read_u2le()
            self.ses_total_power_load = self._io.read_u2le()
            self.ses_median_pmm_temp = self._io.read_s1()
            self.ses_median_pam_temp = self._io.read_s1()
            self.ses_median_pdm_temp = self._io.read_s1()
            self.ses_module_state = self._io.read_bytes(3)
            self.ses_voltage = self._io.read_u2le()
            self.crc16 = self._io.read_u2le()




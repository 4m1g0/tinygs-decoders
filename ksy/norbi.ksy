meta:
  id: norby
  file-extension: norby
  endian: le
seq:
  - id: header
    type: header
  - id: payload
    type:
      switch-on: header.msg_type_id
      cases:
        0: tmi0
    size: header.length - 14

types:
  header:
    seq:
      - id: length
        type: u1
      - id: receiver_address
        type: u4
      - id: transmitter_address
        type: u4
      - id: transaction_number
        type: u2
      - id: reserved
        size: 2
      - id: msg_type_id
        type: s2be
  tmi0:
    seq:
      - id: frame_start_mark
        contents: [0xf1, 0x0f]
      - id: frame_definition
        type: u2
      - id: frame_number
        type: u2
      - id: frame_generation_time
        type: u4
      - id: brk_title
        type: str
        size: 24
        encoding: ASCII
      - id: brk_number_active
        type: u1
      - id: brk_restarts_count_active
        type: s4
      - id: brk_current_mode_id
        type: u1
      - id: brk_transmitter_power_active
        type: s1
      - id: brk_temp_active
        type: s1
      - id: brk_module_state_active
        size: 2
      - id: brk_voltage_offset_amplifier_active
        type: u2
      - id: brk_last_received_packet_rssi_active
        type: s1
      - id: brk_last_received_packet_snr_active
        type: s1
      - id: brk_archive_record_pointer
        type: u2
      - id: brk_last_received_packet_snr_inactive
        type: s1
      - id: ms_module_state
        size: 2
      - id: ms_payload_state
        size: 2
      - id: ms_temp
        type: s1
      - id: ms_pn_supply_state
        type: u1
      - id: sop_altitude_glonass
        type: s4
      - id: sop_latitude_glonass
        type: s4
      - id: sop_longitude_glonass
        type: s4
      - id: sop_date_time_glonass
        type: u4
      - id: sop_magnetic_induction_module
        type: u2
      - id: sop_angular_velocity_vector
        size: 6
      - id: sop_angle_priority1
        type: u2
      - id: sop_angle_priority2
        type: u2
      - id: sop_mk_temp_dsg1
        type: s1
      - id: sop_mk_temp_dsg6
        type: s1
      - id: sop_board_temp
        type: s1
      - id: sop_state
        size: 2
      - id: sop_state_dsg
        size: 6
      - id: sop_orientation_number
        type: u1
      - id: ses_median_panel_x_temp_positive
        type: s1
      - id: ses_median_panel_x_temp_negative
        type: s1
      - id: ses_solar_panels_state
        size: 5
      - id: ses_charge_level_m_ah
        type: u2
      - id: ses_battery_state
        size: 3
      - id: ses_charging_keys_state
        size: 2
      - id: ses_power_line_state
        type: u1
      - id: ses_total_charging_power
        type: s2
      - id: ses_total_generated_power
        type: u2
      - id: ses_total_power_load
        type: u2
      - id: ses_median_pmm_temp
        type: s1
      - id: ses_median_pam_temp
        type: s1
      - id: ses_median_pdm_temp
        type: s1
      - id: ses_module_state
        size: 3
      - id: ses_voltage
        type: u2
      - id: crc16
        type: u2
          


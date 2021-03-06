---
meta:
  id: vzlusat2
  title: VZLUSAT-2 decoder struct
  endian: be

doc: |
  :field csp_hdr_crc: csp_header.crc
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

seq:
  - id: csp_header
    type: csp_header_t
  - id: csp_data
    type: csp_data_t

types:
  csp_header_t:
    seq:
      - id: csp_header_raw
        type: u4
    instances:
      priority:
        value: '(csp_header_raw >> 30)'
      source:
        value: '((csp_header_raw >> 25) & 0x1F)'
      destination:
        value: '((csp_header_raw >> 20) & 0x1F)'
      destination_port:
        value: '((csp_header_raw >> 14) & 0x3F)'
      source_port:
        value: '((csp_header_raw >> 8) & 0x3F)'
      reserved:
        value: '((csp_header_raw >> 4) & 0x0F)'
      hmac:
        value: '((csp_header_raw & 0x08) >> 3)'
      xtea:
        value: '((csp_header_raw & 0x04) >> 2)'
      rdp:
        value: '((csp_header_raw & 0x02) >> 1)'
      crc:
        value: '(csp_header_raw & 0x01)'

  csp_data_t:
    seq:
      - id: cmd
        type: u1
      - id: payload
        if: (_parent.csp_header.source == 1) and (_parent.csp_header.destination == 26) and (_parent.csp_header.source_port == 18) and (_parent.csp_header.destination_port == 18)
        type:
          switch-on: cmd
          cases:
            0x56: vzlusat2_beacon_t
            0x03: vzlusat2_drop_t

  # beacon
  vzlusat2_beacon_t:
    seq:
      - id: callsign
        contents: "ZLUSAT-2"
      - id: obc_timestamp
        type: u4
        doc: "OBC Time (Unix timestamp)"
      - id: obc_boot_count
        type: u4
        doc: "Total number of OBC reboots"
      - id: obc_reset_cause
        type: u4
        doc: "Cause of last OBC reboot"
      - id: eps_vbatt
        type: u2
        doc: "Battery voltage"
      - id: eps_cursun
        type: u2
        doc: "EPS battery photocurrent"
      - id: eps_cursys
        type: u2
        doc: "Total system current draw"
      - id: eps_temp_bat
        type: s2
        doc: "Battery temperature"
      - id: radio_temp_pa_raw
        type: s2
        doc: "Radio PA temperature"
      - id: radio_tot_tx_count
        type: u4
        doc: "Total number of sent packets"
      - id: radio_tot_rx_count
        type: u4
        doc: "Total number of received packets"
    instances:
      radio_temp_pa:
        value: 0.1 * radio_temp_pa_raw

  # drop
  vzlusat2_drop_t:
    seq:
      - id: flag
        type: u1
      - id: chunk
        type: u4
      - id: time
        type: u4
      - id: data_raw
        size-eos: true


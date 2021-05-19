meta:
 id: fees
 file-extension: custom
 endian: le

seq:
  - id: header
    type: header
  - id: payload   
    type:
      switch-on: header.msg_type_id1
      cases:
        254: tmi254
    size: _io.size -3

types:
 header:   
   seq:
      - id: msg_type_id0
        contents: [0x00]
      - id: msg_type_id1
        type: u1
      - id: msg_type_id2
        type: u1

 tmi254:
  seq:
    - id: frame_id
      type: u2
    - id: timestamp
      type: u4
    - id: unknown2
      type: u4
    - id: unknown3
      type: u4
    - id: unknown4
      type: u1
    - id: unknown5
      type: u2
    - id: vacd_2v5
      type: u2
    - id: vbat
      type: u2
    - id: vsol
      type: u2
    - id: unknown6
      type: u2
    - id: unknown7
      type: u2
    - id: unknown8
      type: u2
    - id: unknown9
      type: u2  
    - id: iload
      type: u2
    - id: icharger
      type: u2
    - id: unknown10
      type: u2  
    - id: unknown11
      type: u2  
    - id: unknown12
      type: u2  
    - id: unknown13
      type: u1
    - id: unknown14
      type: u2
      

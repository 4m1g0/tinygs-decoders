meta:
 id: sdsat
 file-extension: custom
 endian: le

seq:
 - id: payload
   type: payload

types:
 payload:
  seq:
    - id: magic
      contents: "SDSAT,LORA ACTIVE:"
    - id: relay_msg
      type: str
      encoding: UTF-8
      size-eos: true

 


    



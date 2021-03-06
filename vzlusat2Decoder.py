#!/usr/bin/python

import sys
import base64
import json
from vzlusat2 import Vzlusat2

def bytes2list(d):
    for key in d:
        if isinstance(d[key], bytes):
            d[key] = list(d[key])

def getHeader(vzlusat2Packet):
     packet = vzlusat2Packet.csp_header.__dict__.copy()
     del packet["_io"]
     del packet["_parent"]
     del packet["_root"]
     bytes2list(packet)
     return packet

def getPayload(vzlusat2Packet):
    if "payload" not in vzlusat2Packet:
        return None
    packet = vzlusat2Packet["payload"].__dict__.copy()
    del packet["_io"]
    del packet["_parent"]
    del packet["_root"]
    bytes2list(packet)
    return packet

def getData(vzlusat2Packet):
    packet = vzlusat2Packet.csp_data.__dict__.copy()
    del packet["_io"]
    del packet["_parent"]
    del packet["_root"]
    packet["payload"] = getPayload(packet)
    bytes2list(packet)
    return packet

def decode(packet_base64):
     base64_bytes = packet_base64.encode('ascii')
     message_bytes = base64.b64decode(base64_bytes)
     return Vzlusat2.from_bytes(message_bytes)

def main(argv):
    if len(argv) < 1:
        print('{"error": "Invalid arguments"}')
        return 1
    
    try:
        vzlusat2Packet = decode(argv[0])
    except Exception as e: 
        print('{"error":"' + str(e) + '"}')
        return 1
    
    parsedPacket = {
        "csp_header": getHeader(vzlusat2Packet),
        "csp_data": getData(vzlusat2Packet)
    }
    
    parsedPacket["telemetry"] = (parsedPacket["csp_data"]["cmd"] == 0x56)
    
    print(json.dumps(parsedPacket))
    return 0
        
if __name__ == "__main__":
   main(sys.argv[1:])

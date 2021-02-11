#!/usr/bin/python

import sys
import base64
import json
from norby import Norby

def bytes2list(d):
    for key in d:
        if isinstance(d[key], bytes):
            d[key] = list(d[key])

def getHeader(norbyPacket):
     packet = norbyPacket.header.__dict__.copy()
     del packet["_io"]
     del packet["_parent"]
     del packet["_root"]
     bytes2list(packet)
     return packet

def getPayload(norbyPacket):
    if isinstance(norbyPacket.payload, bytes):
        raw = {"raw": norbyPacket.payload}
        bytes2list(raw)
        return raw
    
    packet = norbyPacket.payload.__dict__.copy()
    del packet["_io"]
    del packet["_parent"]
    del packet["_root"]
    bytes2list(packet)
    return packet

def decode(packet_base64):
     base64_bytes = packet_base64.encode('ascii')
     message_bytes = base64.b64decode(base64_bytes)
     return Norby.from_bytes(message_bytes)

def main(argv):
    if len(argv) < 1:
        print('{"error": "Invalid arguments"}')
        return 1
    
    try:
        norbyPacket = decode(argv[0])
    except Exception as e: 
        print('{"error":"' + str(e) + '"}')
        return 1
    
    parsedPacket = {
        "header": getHeader(norbyPacket),
        "payload": getPayload(norbyPacket)
    }
    if "raw" in parsedPacket["payload"]:
        parsedPacket["telemetry"] = False
    else:
        parsedPacket["telemetry"] = True
    
    print(json.dumps(parsedPacket))
    return 0
        
if __name__ == "__main__":
   main(sys.argv[1:])

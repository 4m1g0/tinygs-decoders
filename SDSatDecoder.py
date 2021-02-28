#!/usr/bin/python

import sys
import base64
import json

def decode(packet_base64):
     base64_bytes = packet_base64.encode('ascii')
     message_bytes = base64.b64decode(base64_bytes)
     return message_bytes.decode('ascii')


def main(argv):
    if len(argv) < 1:
        print('{"error": "Invalid arguments"}')
        return 1

    try:
        SDSatPacket = decode(argv[0])
    except Exception as e:
        print('{"error":"' + str(e) + '"}')
        return 1

    print('{"payload":"' + SDSatPacket + '"}')

if __name__ == "__main__":
   main(sys.argv[1:])

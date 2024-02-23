"""
Beacon decoder for the PY4 mission.
Uses beacon parsing scheme from https://github.com/maholli/PY4_gs

Max Holliday 2024
"""

import struct, time
from collections import OrderedDict
import numpy as np
from pprint import pprint

sats = OrderedDict({
    0x49:'GS',
    0x4A:'Leo',
    0x4B:'Don',
    0x4C:'Raph',
    0x4D:'Mike'
    })
POWER_CONFIG = ('RF','SKY','SAMD','IRI','NOVA','RPI')
raw = bytearray(56)
view=memoryview(raw)

DSENSERES=25e-6 # 25uV resolution
SENSERES=0.02
MAG_SCALAR = (1/16) * 1e-6 # T
GYR_SCALAR = 1/65.6        # deg/s
# sat_X =  imu_Y, sat_Y = -imu_X, sat_Z = -imu_Z
R_sat_imu = np.array(
    (
        [0.0, 1.0, 0.0],
        [-1.0, 0.0, 0.0],
        [0.0, 0.0, -1.0],
    )
)

def parse_beacon(beacon,debug=False):
    if beacon[0] in sats:
        view[:]=beacon[4:]
        pwr_cfg = "".join(reversed(f'{view[9]:08b}'))
        pwr_cfg = [int(i) for i in pwr_cfg]
        parsed_beacon_data = {
            'sat_id'            :beacon[1],
            'pckt_crc'          :view[-1],
            'boot_cnt'          :view[0],
            'sc_err_cnt'        :view[1],
            'vlowb_cnt'         :view[3],
            'detumbling_f'      :bool(view[4]>>2&1),
            'lowbtout_f'        :bool(view[4]>>3&1),
            'tumbling_f'        :bool(view[4]>>4&1),
            'shutdown_f'        :bool(view[4]>>5&1),
            'deploy_f'          :bool(view[4]>>6&1),
            'deploy_wait'       :bool(view[4]>>7&1),
            'rpi_status'        :view[4]&3,
            'sc_time'           :int.from_bytes(view[5:9],"big"), # sec
            'pwr_rf'            :pwr_cfg[0],
            'pwr_sky'           :pwr_cfg[1],
            'pwr_SAMD'          :pwr_cfg[2],
            'pwr_iri'           :pwr_cfg[3],
            'pwr_nova'          :pwr_cfg[4],
            'pwr_rpi'           :pwr_cfg[5],
            'vbatt'             :view[10]/10, # V
            'ichrg'             :view[11]*4,  # mA
            'idraw'             :(((view[12]<<8)|view[13])>>4)*DSENSERES/SENSERES, # A
            'radio_rsps'        :list(view[14:19]), # [0x49,0x4A,0x4B,0x4C,0x4D]
            'uhf_err_cnt'       :view[2],
            'sc_last_rssi'      :view[19]-137,
            }
        # rotating dataset
        if view[20] == 0xA8:
            _ecef = struct.unpack('<ddd',view[29:53])
            parsed_beacon_data.update({
            # gps dataset
            'time_stat'         :view[21],
            'gps_week'          :int.from_bytes(view[22:24],"little"),
            'gps_time'          :int.from_bytes(view[24:28],"little")/1000, # sec
            'pos_stat'          :view[28],
            'ecef_x'            :_ecef[0], # meters
            'ecef_y'            :_ecef[1], # meters
            'ecef_z'            :_ecef[2], # meters
            'sv_in_sol'         :view[53],
            'sd_rpi_files'      :view[54],
            })
        elif view[20] == b'R'[0]:
            _imu_mag = np.frombuffer(view[25:31], dtype='int16') * MAG_SCALAR
            _imu_gyr = np.frombuffer(view[31:37], dtype='int16') * GYR_SCALAR
            # rotate to spacecraft frame
            _imu_mag = np.dot(R_sat_imu,_imu_mag)
            _imu_gyr = np.dot(R_sat_imu,_imu_gyr)
            _sun_lux = np.frombuffer(view[37:49],dtype='>u2')
            _sun_lux = 0.01 * (_sun_lux&-61441) * 2 ** ((_sun_lux & 61440) >> 12)
            _which_rad = f'{"rad_r1" if any(view[52:55]) else "rad_r2"}'
            _rt=0
            if _which_rad == "rad_r1":
                _rt=(int.from_bytes(view[52:55],"big")*1.49012e-07*1000)
                _rt=(-1*((129.00-_rt)*0.403)+25)
            else: _rt = 0
            parsed_beacon_data.update({
            # rad dataset
            'rng_file_cnt'      :int.from_bytes(view[21:23],"big"),
            'rad_file_cnt'      :int.from_bytes(view[23:25],"big"),
            'mag_x'             :_imu_mag[0],
            'mag_y'             :_imu_mag[1],
            'mag_z'             :_imu_mag[2],
            'gyr_x'             :_imu_gyr[0],
            'gyr_y'             :_imu_gyr[1],
            'gyr_z'             :_imu_gyr[2],
            'sun_xp'            :_sun_lux[0],
            'sun_yp'            :_sun_lux[1],
            'sun_zp'            :_sun_lux[2],
            'sun_xn'            :_sun_lux[3],
            'sun_yn'            :_sun_lux[4],
            'sun_zn'            :_sun_lux[5],
            _which_rad          :(2.5-(int.from_bytes(view[49:52],"big")*1.49012e-07)), # V
            'rad_t'             :_rt, # deg C
            })
        return parsed_beacon_data

def main(argv):
    if len(argv) < 1:
        print('{"error": "Invalid arguments"}')
        return 1
    base64_bytes = argv[0].encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    try:
        parsedPacket = parse_beacon(message_bytes)
    except:
        parsedPacket = None
    
    if parsedPacket is not None:
        parsedPacket['telemetry'] = True
    else:
        parsedPacket = {
            'raw': base64_bytes,
            'telemetry': False
        }
    print(json.dumps(parsedPacket))
    return 0
        
if __name__ == "__main__":
   main(sys.argv[1:])

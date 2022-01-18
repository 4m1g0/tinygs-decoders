meta:
  id: grizu
  file-extension: grizu
  endian: le
seq:
  - id: header
    type: header

types:
  header:
    seq:
      - id: teamid
        type: str
        size: 6
        encoding: ASCII
      - id: year
        type: u1
      - id: month
        type: u1
      - id: date
        type: u1
      - id: hour
        type: u1
      - id: minute
        type: u1
      - id: second
        type: u1
      - id: temp
        type: u2
      - id: epstoobcina1_current
        type: u2
      - id: epstoobcina1_busvoltage
        type: u2
      - id: epsina2_current
        type: u2
      - id: epsina2_busvoltage
        type: u2
      - id: baseina3_current
        type: u2
      - id: baseina3_busvoltage
        type: u2
      - id: topina4_current
        type: u2
      - id: topina4_busvoltage
        type: u2
      - id: behindantenina5_current
        type: u2
      - id: behindantenina5_busvoltage
        type: u2
      - id: rightsideina6_current
        type: u2
      - id: rightsideina6_busvoltage
        type: u2
      - id: leftsideina7_current
        type: u2
      - id: leftsideina7_busvoltage
        type: u2
      - id: imumx
        type: u2
      - id: imumy
        type: u2
      - id: imumz
        type: u2
      - id: imuax
        type: u2
      - id: imuay
        type: u2
      - id: imuaz
        type: u2
      - id: imugx
        type: u2
      - id: imugy
        type: u2
      - id: imugz
        type: u2


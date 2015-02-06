#!/usr/bin/python2.7

import argparse
import re

parser = argparse.ArgumentParser(description='Convierte de formato CodeGraphics a hex.')
parser.add_argument('archivo', type=argparse.FileType('r'),
                    help='archivo de entrada')

args = parser.parse_args()
values = []
for line in args.archivo.readlines():
           line = re.sub('\n','\r', line.rstrip())
           line = line.replace(";", "", 1)
           line = line.replace(",", "", 7)
           line = line.split()
           for value in line:
                      value = int(value,10)
                      value = hex(value)
                      value = value.replace("0x", "" , 1)
                      value = value.upper()
                      values.append(value)
                      

values = "".join(values)
values = re.findall('................................................................?', values)

addr = 0;
for value in values:
           addr = hex(addr)
           addr = addr.replace("0x", "", 1)
           while len(addr) < 3:
                      addr = "0" + addr
           print(":20" + addr + "000" + value)
           addr = int(addr, 16) + 0x02

print(':00000001FF')

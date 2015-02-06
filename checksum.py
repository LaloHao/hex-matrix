#!/usr/bin/python2.7

import argparse
import re

parser = argparse.ArgumentParser(description='Calcula el checksum.')
parser.add_argument('archivo', type=argparse.FileType('r'),
                    help='archivo de entrada')

args = parser.parse_args()
#print args.archivo.readlines().rstrip('\n')
for line in args.archivo.readlines():
           line = re.sub('\n','\r', line.rstrip())
           line = line.replace(":", "", 1)
           line = line[0:72]
           elements = re.findall('..', line)
           checksum = 0
           for word in elements:
                  checksum = (checksum + int(word, 16))
           checksum = ~checksum + 1
           checksum = checksum & 0xFF
           checksum = hex(checksum)
           checksum = checksum.replace("0x", "", 1)
           if len(checksum) == 1:
                  checksum = '0' + checksum
           checksum = checksum.upper()
           line = ':' + line
           if line == ':00000001FF':
                  print(line + '\r')
           else:
                  print(line+checksum + '\r')

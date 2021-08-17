#!/usr/bin/python3
# Created by Korey McKinley
 
# Parses .gnmap files for IPs and hostnames and outputs to designated file.

import re
import argparse
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument('inputfile', help='Path to .gnmap file.')
parser.add_argument('outputfile', help='Path to output file.')
args = parser.parse_args()

inputfile = open(args.inputfile, 'r')
outputfile = open(args.outputfile, 'w')
data = inputfile.read()
x = re.findall(r'Host: (.*?)\t', data)

outputfile.write('\n'.join(list(OrderedDict.fromkeys(x))))
outputfile.close()

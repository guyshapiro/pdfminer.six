#!/usr/bin/env python

import sys
import fileinput

def main(argv):
    print ('\nglyphname2unicode = {')
    for line in fileinput.input():
        line = line.strip()
        (name,x) = line.split(',')
        codes = x.split(' ')
        print (' %r: u\'%s\',' % (name, ''.join( '\\u%s' % code for code in codes )))
    print ('}\n')

if __name__ == '__main__': sys.exit(main(sys.argv))

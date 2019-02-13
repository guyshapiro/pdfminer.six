#!/usr/bin/env python
"""
Generate python code with mapping of glyph names to the Unicode characters,
based on GhostScript decoding file.
"""

import sys
import fileinput
import logging

logging.basicConfig()
log = logging.getLogger(__name__)

def parseGlyphLine(line):
    parts = line.split()
    code = parts[0]
    names = parts[1:]
    ustr = codeToUstr(code)

    for name in names:
        if name:
            print (' %r: %s,'% (name, ustr))

def codeToUstr(code):
    # remove the '16#' or '%L#' prefix
    no_prefix = code[3:]
    # in case of '%L#' lines, the chars are separated with '_'
    # example: '%L#05DA_05B0    finalkafsheva finalkafshevahebrew'
    chars = no_prefix.split('_')
    # add \u to each char, to make a char from 16-bit hex value
    chars = [ '\\u' + c for c in chars ]
    # warp with string literal, and return
    return 'u\''+ ''.join(chars) +'\''

def main(argv):
    print ('\nglyphname2unicode = {')
    for line in fileinput.input():
        line = line.strip()
        if line.startswith("16#") or line.startswith("%L#"):
            parseGlyphLine(line)
            continue
        if line.startswith("%"):
            continue
        if line == "":
            continue
        log.warning("line skipped: %s",line)
    print ('}\n')
        

if __name__ == '__main__': sys.exit(main(sys.argv))

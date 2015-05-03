#!/usr/bin/env python

#This is for pythonchallenge.com #1

# The clue given is an image directing that the alphabet is to be shifted
# 3 letters down, such that k->m, o->q, etc


# The script will attempt to shift whatever text is passed to it, but in the absense
# of such data, the string from the web page for this step is used.



from string import translate, maketrans
import sys





in_string = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

table = maketrans('abcdefghijklmnopqrstuvwxyz',
    'cdefghijklmnopqrstuvwkyzab')

try:
    in_string = sys.argv[1]
except IndexError:
    pass
def shift_letter(c):
    # This we eventually be capable of returning shifted letters
    return translate(c,table)

out = [] #Make it a string later, for now use mutable list for performance 
for idx, val in enumerate( in_string):
    out.append(shift_letter(val))

print ''.join(out)


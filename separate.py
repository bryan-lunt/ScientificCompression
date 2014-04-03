#!/usr/bin/env python

import scipy as S

import quoter as q

import sys
import cPickle as P

FILENAME = sys.argv[1]

input_data = open(FILENAME).read()

text, floats, format_table = q.quote_split(input_data)

with open(FILENAME+"_text", "w") as outtxt:
	outtxt.write(text)

with open(FILENAME+"_table", "w") as outtable:
	P.dump(format_table, outtable)

with open(FILENAME+"_numeric", "w") as outnumeric:
	S.save(outnumeric,S.array(floats,S.float32))

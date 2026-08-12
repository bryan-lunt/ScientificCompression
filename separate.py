#!/usr/bin/env python

import numpy as np

import quoter as q

import sys
import pickle as P

FILENAME = sys.argv[1]

input_data = open(FILENAME).read()

text, floats, format_table = q.quote_split(input_data)

with open(FILENAME+"_text", "w") as outtxt:
	outtxt.write(text)

with open(FILENAME+"_table", "w") as outtable:
	P.dump(format_table, outtable)

with open(FILENAME+"_numeric", "w") as outnumeric:
	np.save(outnumeric,np.array(floats,np.float64))
#	np.savez_compressed(outnumeric,np.array(floats,np.float64))

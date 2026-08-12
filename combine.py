#!/usr/bin/env python

import numpy as np

import quoter as q

import sys
import pickle as P

TEXT, FLOATS, FORMAT = sys.argv[1:4]

TEXT_data = open(TEXT).read()

FLOATS_data = np.load(FLOATS).tolist()
####
#a = S.load(FLOATS)
#FLOATS_data = a['arr_0'].tolist()
####

FORMAT_TABLE = P.load(open(FORMAT,"rb"))



result = q.quote_combine(TEXT_data, FLOATS_data, FORMAT_TABLE)

sys.stdout.write(result)

#!/usr/bin/env python

import scipy as S

import quoter as q

import sys
import cPickle as P

TEXT, FLOATS, FORMAT = sys.argv[1:4]

TEXT_data = open(TEXT).read()

FLOATS_data = S.load(open(FLOATS)).tolist()
####
#a = S.load(FLOATS)
#FLOATS_data = a['arr_0'].tolist()
####

FORMAT_TABLE = P.load(open(FORMAT))



result = q.quote_combine(TEXT_data, FLOATS_data, FORMAT_TABLE)

sys.stdout.write(result)

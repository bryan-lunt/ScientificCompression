#!/usr/bin/env python
import sys
import scipy as S

data = S.randn(1000, 10)
S.savetxt(sys.stdout,data)

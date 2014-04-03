#!/usr/bin/env python
import scipy as S

data = S.randn(10000)
S.savetxt("test2",data)

#!/usr/bin/env python
import scipy as S

data = S.randn(1000, 10)
S.savetxt("test2",data)

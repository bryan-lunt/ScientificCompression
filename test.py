#!/usr/bin/env python
import scipy as S

data = S.randn(100, 100)
S.savetxt("test2",data)

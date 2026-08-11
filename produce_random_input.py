#!/usr/bin/env python
import sys
import scipy as S
import numpy as np

data = np.random.randn(1000, 10)
np.savetxt(sys.stdout,data)

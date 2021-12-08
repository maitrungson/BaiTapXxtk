import pandas as pd
import numpy as np
data = {'a' : -1.3, 'b' : 11.7, 'd' : 2.0, 'f': 10, 'g': 5}
ser = pd.Series(data,index=['a','c','b','d','e','f'])

a = np.asarray(ser)
print(a)

# Output:
#
# [-1.3  NaN 11.7  2.0  NaN 10 ]
© 2021 GitHub, Inc.
Terms
Privacy


import pandas as pd

# tao dict tu các series
s = {'mot': pd.Series([1., 2., 3., 5.], index=['a', 'b', 'c', 'e']),
     'hai': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

# tai DataFrame tu dict
df = pd.DataFrame(s)

print(df)

# Output:
#
#    mot  hai
# a  1.0  1.0
# b  2.0  2.0
# c  3.0  3.0
# d  NaN  4.0
# e  5.0  NaN

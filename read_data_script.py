# practice reading in files

import numpy as np

print('lets load some files')
#my_data = np.loadtxt(fname = 'data_file.csv', delimiter = ',')
f = open('data_file.csv', 'r')
lines = f.readlines()
print('data is')
print lines
line = lines[0]
split_line= lines[0].split(',')
print split_line

for element in split_line:
    num = int(element)
    print num

import glob
import os
import numpy as np

data = []

for file in glob.glob("./Data/raw/*"):
    data.append(np.loadtxt(file, skiprows=2, delimiter=";", usecols = (0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)))

    if not os.path.exists('./Data/cleaned'):
        os.makedirs('./Data/cleaned')

    np.savetxt('./Data/cleaned/' + os.path.basename(file), data[-1], delimiter='\t', fmt='%s', comments='')
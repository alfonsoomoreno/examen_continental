import h5py
import pandas as pd
import numpy as np

filename = '/home/jesus-alfonso/Documentos/Examen_continental/madrid.h5'
key = '28079059'
file = pd.read_hdf(filename, key)
print(file)
#data = h5py.File(filename, 'r')
#data.close()
#for file in data.keys():
	#file = pd.read_hdf(filename, key=file)
	#print(file) #Names of the groups in HDF5 file.

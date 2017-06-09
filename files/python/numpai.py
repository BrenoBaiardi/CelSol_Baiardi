#TESTES DA BIBLIOTECA NUMPY
import numpy as np
"""
a=np.arange(10)
print("Retorna:"+str(a)+" Tipo:"+str(type(a)))

print("5,2\n",a.reshape(5,2))
print("2,5\n",a.reshape(2,5))
a=a.reshape(2,5)


print("dim:"+str(a.ndim))
print("itemsize:"+str(a.itemsize)+"->Tamanho ocupado por cada elemento em armazenamento")
print("size:"+str(a.size))
print("dtype:"+str(a.dtype))

print("criar numpy.array dados números")
b = np.array([6, 7, 8])
print("7,8,9 -> "+str(b))

'''
>>> a = np.array(1,2,3,4)    # WRONG
>>> a = np.array([1,2,3,4])  # RIGHT
'''

c = np.array( [ [0.000000000000001,2], [3,4] ], dtype=complex )
"""

#################
#hora de prática#
#################

file=open("S2_081217_1400.dat")

#data = np.genfromtxt('S2_081217_1400.dat',dtype=complex,skip_header=1)

data = np.genfromtxt('CPA16_306a017.dat',dtype=complex,skip_header=4,delimiter=",")
print(data)

import pandas as pd
fields = ["TIMESTAMP","RECORD"]

df = pd.read_csv('CPA16_306a017.dat', skipinitialspace=True,header=1, usecols=fields)
# See the keys
print(df.keys())
# See content in 'star_name'
print (df.TIMESTAMP)

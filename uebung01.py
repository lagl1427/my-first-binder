import numpy as np

name = "whDatadat.sec"
data = np.loadtxt(name, dtype=np.object, comments='#', delimiter=None)
# Um die w und h Daten aus dem array data auszulesen, k¨onnen Sie so vorgehen
w = data[:,0].astype(float)
h = data[:,1].astype(float)

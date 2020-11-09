import numpy as np
import matplotlib.pyplot as plt

name = "whDatadat.sec"
data = np.loadtxt(name, dtype=np.object, comments='#', delimiter=None)
# Um die w und h Daten aus dem array data auszulesen, k¨onnen Sie so vorgehen
w = data[:,0].astype(float)
h = data[:,1].astype(float)


fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
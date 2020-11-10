import numpy as np
import matplotlib.pyplot as plt

name = "whDatadat.sec"
data = np.loadtxt(name, dtype=np.object, comments='#', delimiter=None)
# Um die w und h Daten aus dem array data auszulesen, k¨onnen Sie so vorgehen
w = data[:,0].astype(float)
h = data[:,1].astype(float)

print(w)
print(h)


h = np.delete(h, np.where(w == -1))
w = np.delete(w, np.where(w == -1))

#print(w)
#print(h)

#h = np.append(h, [float(158), float(195)])
#w = np.append(w, [float(58.79), float(90.25)])

#print(w)
#print(h)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(h, w, ".")  # Plot some data on the axes.
ax.set_xlabel("body height (cm)", fontsize=18)
ax.set_ylabel("body weight (kg)", fontsize=18)
ax.plot([float(158), float(195)], [float(58.79), float(90.25)], "bs", color='red', linestyle='-')

#w = np.append(w, [float(3), float(4)])
#print(w)

print("Arithmetisches Mittel Größe: ", np.mean(h))
print("Varianz Größe: ", np.var(h))
print("Standardabweichung Größe: ", np.std(h))

print("Arithmetisches Mittel Gewicht: ", np.mean(w))
print("Varianz Gewicht: ", np.var(w))
print("Standardabweichung Gewicht: ", np.std(w))
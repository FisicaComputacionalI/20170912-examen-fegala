#Importamos las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
#Definimos la funcion
def f(t):
 return ((2 * np.cos(t)) + 2015)
#definimo el intervalo que va a recorrer y arreglamos cada cuanto se va a agregar un valor
t1 = np.arange(0.0, 8.0, 0.1)
#Dividimos en 2 graficas que ocupan una columna cada una
plt.subplot(121)
plt.plot(t1, f(t1), 'k+')
plt.subplot(122)
plt.plot(t1, f(t1), t1, f(t1), 'r*')
#Finalmente se guarda la imagen
plt.savefig('ejercicio2.png')

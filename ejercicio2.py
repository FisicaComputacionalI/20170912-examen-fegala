#Importamos las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
#Definimos la funcion
def f(t):
 return ((2 * np.cos(t)) + 2015)
#definimo el intervalo que va a recorrer y arreglamos cada cuanto se va a agregar un valor
t1 = np.arange(0.0, 15.0, 0.1)
#Definimos la grafica, color y detalles
plt.plot(t1, f(t1), 'k+')
#Finalmente se guarda la imagen
plt.savefig('ejercicio2.png')

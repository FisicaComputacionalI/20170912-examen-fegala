#Importamos las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
#Definimos la funcion del ejercicio 2
def f(t):
 return ((2 * np.cos(t)) + 2015)
#Valores de la funcion del ejercicio1
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
y = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
#definimo el intervalo que va a recorrer y arreglamos cada cuanto se va a agregar un valor
t1 = np.arange(0.0, 15.0, 0.1)
#Dividimos en 2 graficas que ocupan una columna cada una, donde en el primer espacio van las graficas del ejercicio 1 y 2
plt.subplot(121)
plt.plot(t1, f(t1), 'k+', x, y)
plt.subplot(122)
plt.plot(t1, f(t1), t1, f(t1), 'r*')
#Finalmente se guarda la imagen
plt.savefig('ejercicio3.png')

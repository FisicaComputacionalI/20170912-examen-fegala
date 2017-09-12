#Primero importamos las librerias para hacer la grafica y guardarla como imagen 
import numpy as np
import pylab as pl
#Agregamos los valores a 'x' y 'y'
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
y = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
#Definimos la grafica
pl.plot(x, y, 'r--')
#Agregamos titulo
pl.title('Fernando')
#Colocamos la leyenda 'edad' y 'anio' a 'x' y a 'y' respectivamente
pl.xlabel('edad')
pl.ylabel('anio')
#La grafica resultante se guarda con formato .png
pl.savefig('Fernando1.png')

import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal

datos_2008 = pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2008.txt', header = None, sep=";")
datos_2009 = pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2009.txt', header = None, sep=";")
datos_2010 = pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_2/Fourier/Datos/transacciones2010.txt', header = None, sep=";")

datos_2008 ["Fecha nueva"] = pd.to_datetime(datos_2008[0].astype(str).str[:-8] + " " + datos_2008[1].astype(str).str[11:], format='%d/%m/%Y %H:%M:%S')

datos_2009 ["Fecha nueva"] = pd.to_datetime(datos_2009[0].astype(str).str[:-8] + " " + datos_2009[1].astype(str).str[11:], format='%d/%m/%Y %H:%M:%S')

datos_2010 ["Fecha nueva"] = pd.to_datetime(datos_2010[0].astype(str).str[:-8] + " " + datos_2010[1].astype(str).str[11:], format='%d/%m/%Y %H:%M:%S')

datos_2008.set_index(["Fecha nueva"], inplace=True)
datos_2009.set_index(["Fecha nueva"], inplace=True)
datos_2010.set_index(["Fecha nueva"], inplace=True)
a = pd.concat([datos_2008, datos_2009, datos_2010])
a[2] = (a[2].replace(",", ".", regex=True)).astype(float)


a.plot(y=2)
a.show()

date = a[0]
v = a[2]

N  = 1   # Orden del filtro
Wn = 0.01 # Corte de frecuencia
B, A = signal.butter(N, Wn)


v_filtrada = signal.filtfilt(B,A, a[2])


fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(date,v, 'b-')
plt.plot(date,v_filtrada, 'r-',linewidth=2)
plt.ylabel("valor")
plt.legend(['Original','Filtrado'])
plt.title("valor")
ax1.axes.get_xaxis().set_visible(False)
ax1 = fig.add_subplot(212)
plt.plot(date,v-v_filtrada, 'b-')
plt.ylabel("valor")
plt.xlabel("Fecha")
plt.legend(['Residuales'])
plt.savefig("1")


N  = 1   # Orden del filtro
Wn = 0.0001 # Corte de frecuencia
B, A = signal.butter(N, Wn)


v_filtrada = signal.filtfilt(B,A, a[2])


fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(date,v, 'b-')
plt.plot(date,v_filtrada, 'r-',linewidth=2)
plt.ylabel("valor")
plt.legend(['Original','Filtrado'])
plt.title("valor")
ax1.axes.get_xaxis().set_visible(False)
ax1 = fig.add_subplot(212)
plt.plot(date,v-v_filtrada, 'b-')
plt.ylabel("valor")
plt.xlabel("Fecha")
plt.legend(['Residuales'])
plt.savefig("2")


N  = 4   # Orden del filtro
Wn = 0.01 # Corte de frecuencia
B, A = signal.butter(N, Wn)


v_filtrada = signal.filtfilt(B,A, a[2])


fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(date,v, 'b-')
plt.plot(date,v_filtrada, 'r-',linewidth=2)
plt.ylabel("valor")
plt.legend(['Original','Filtrado'])
plt.title("valor")
ax1.axes.get_xaxis().set_visible(False)
ax1 = fig.add_subplot(212)
plt.plot(date,v-v_filtrada, 'b-')
plt.ylabel("valor")
plt.xlabel("Fecha")
plt.legend(['Residuales'])
plt.savefig("3")


N  = 4   # Orden del filtro
Wn = 0.0001 # Corte de frecuencia
B, A = signal.butter(N, Wn)


v_filtrada = signal.filtfilt(B,A, a[2])


fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
plt.plot(date,v, 'b-')
plt.plot(date,v_filtrada, 'r-',linewidth=2)
plt.ylabel("valor")
plt.legend(['Original','Filtrado'])
plt.title("valor")
ax1.axes.get_xaxis().set_visible(False)
ax1 = fig.add_subplot(212)
plt.plot(date,v-v_filtrada, 'b-')
plt.ylabel("valor")
plt.xlabel("Fecha")
plt.legend(['Residuales'])
plt.savefig("3")


plt.figure(figsize=(20,7))
ruido=v-v_filtrada
corr=signal.correlate(ruido,ruido,mode="full")
plt.plot(corr[len(corr)//2:])
plt.savefig("rel1")


plt.figure(figsize=(20,7))
corr=np.correlate(ruido,ruido,mode="full")
plt.plot(corr[len(corr)//2:])
plt.savefig("rel2")


plt.figure(figsize=(20,7))
corr=np.correlate(ruido,ruido,mode="full")
plt.plot(np.abs(corr[len(corr)//2:]))
plt.savefig("rel3")

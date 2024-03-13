import pandas as pd 
import numpy as np
import os
import re

def explorar_directorio(directorio):
  # Iterar sobre las subcarpetas y archivos en el directorio, devuelve una listo de archivos .csv ordenados por nombre
  lista_archivos = []
  for dirpath, dirnames, filenames in os.walk(directorio):
    for filename in filenames:
      if filename.endswith('.csv'):
        lista_archivos.append(os.path.join(dirpath, filename))

  return(sorted(lista_archivos , key=lambda x: x.lower()))

def cargar_muestras_paciente(df1, df2, df3, directorio):
  '''
  Lee muestras alojadas en un directorio y las anexa al dataframe indicado
  IMPORTANTE: el nombre del archivo debe ser "Nombre del paciente o ID + ndia de tratamiento"
  Especificar en NoMuestra el tipo de muestra tomada (PRE - PRP1 - PRP2) y el ID del paciente donde corresponde
  '''

  lista_archivos = explorar_directorio(directorio)

  for archivo in lista_archivos:
      # Leer cada archivo y obtener la primera fila
      nueva_fil = pd.read_csv(archivo, encoding='latin1').iloc[0].tolist()
      dia, IDpac = nueva_fil[1], nueva_fil[8]
      muestra = nueva_fil[5]
      nombre_fil = f"{IDpac} {dia}"

      if re.match(r'^[123]Pre$', muestra, re.IGNORECASE):
          df1.loc[nombre_fil] = nueva_fil
      
      if re.match(r'^[123]Prp1$', muestra, re.IGNORECASE):
          df2.loc[nombre_fil] = nueva_fil
      
      if re.match(r'^[123]Prp2$', muestra, re.IGNORECASE):
          df3.loc[nombre_fil] = nueva_fil

import pandas as pd

def leer_archivo_csv(ruta):
   
    #Lee un archivo CSV y devuelve un DataFrame de pandas
    
    try:
        df = pd.read_csv(ruta)                  #ruta es un parametro el cual es el string del archivo CSV
        return df
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en la ruta '{ruta}'")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo CSV en '{ruta}' está vacío.")
        return None
    except pd.errors.ParserError as e:
        print(f"Error al leer el archivo CSV: {e}")
        return None                                         # pd.DataFrame me va a devolver los datos del archivo CSV, o None si hay algun error
    


#Ejemplo de uso 

ruta_csv = "ruta/al/archivo.csv"
df = leer_archivo_csv(ruta_csv)

if df is not None:
    print(df.head())  # Muestra las primeras filas del DataFrame
else:
    print("No se pudo leer el archivo CSV.")

#Funcion de correccion de errores 

import pandas as pd
import numpy as np

def correct_csv_errors(df): #Corrige los errores comunes en un DataFrame de pandas, como filas desalineadas y tipos de datos incorrectos.
  
    #Parametros: df (pd.DataFrame): DataFrame a corregir.

    #Returns: pd.DataFrame: DataFrame corregido.
   
    # Eliminar filas desalineadas (si hay valores NaN en filas completas, eliminarlas)
    df.dropna(how='all', inplace=True)
    
    # Arreglar los tipos de datos de las columnas
    for column in df.columns:
        # Intentar convertir a números (si no se puede, mantener como string)
        try:
            df[column] = pd.to_numeric(df[column], errors='ignore')
        except:
            pass

    # Identificar columnas que deberían ser fechas
    date_columns = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
    for col in date_columns:
        try:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        except:
            pass

    # Reemplazar NaN en columnas numéricas por un valor representativo, como 0 o la media
    num_columns = df.select_dtypes(include=[np.number]).columns
    for col in num_columns:
        df[col].fillna(0, inplace=True)

    return df

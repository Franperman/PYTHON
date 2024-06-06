import pandas as pd

# Load the CSV file
df = pd.read_csv('C:\Proyectos\datos.csv')

df_media = (df["corriente"].mean())

df_maxi = (df["potencia"].max())

print("la media de la corriente es: ", round(df_media, 2))
print("la maxima de la potencia es: ", df_maxi)


import pandas as pd
#Crear datos (simulación estudiantes)
datos={
    "nombre":["ana","luis","carlos","sofia","pedro"],
    "edad":[30,70,18,21,22],
    "nota":[3.5,4.2,2.8,4.8,3.0]
    }

df =pd.DataFrame(datos)
print(df)

#Promedio de notas
print("Promedio:",df["nota"].mean())

#Promedio de edades
print("Promedio:",df["edad"].mean())
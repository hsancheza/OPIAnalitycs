"Examen Ciencia de Datos OPI Analitycs - Código Python"

"##################################"
"Cargamos los packages necesarios"
import pandas as pd
from matplotlib import pyplot as plt

"##################################"
"Importampos la el archivo descargado en formato csv"

data = pd.read_csv('C:/Users/HSANCHEZA/Downloads/datoscdmx.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode',header=0)

print(list(data))
print(len(data.categoria_delito.unique()))

"##################################"
"Creamos la Tabla para la Preguna 02"

preg02=pd.pivot_table(data,index=['categoria_delito'],values=['delito'],columns=['ao_hechos'],aggfunc='count')
print(preg02)

"Creamos un archivo en excel para poder análizar y visualizar mejor los resultados
"
writer=pd.ExcelWriter('ExamenOPIAnalitycs.xlsx')
preg02.to_excel(writer,'Pregunta02')
writer.save()

"##################################"
"Creamos la Tabla para la Preguna 03"

preg03A=pd.pivot_table(data,index=['alcaldia_hechos'],values=['delito'],columns=['ao_hechos'],aggfunc='count')
print(preg03A)
"Guardamos en una hoja del mismo archivo excel creado"
preg03A.to_excel(writer,'Pregunta03A')
writer.save()

preg03B=pd.pivot_table(data,index=['alcaldia_hechos'],values=['delito'],aggfunc='count')
preg03B.to_excel(writer,'Pregunta03B')
writer.save()

"##################################"
"Creamos la Tabla para la Preguna 04"

preg04=pd.pivot_table(data,values=['delito'],columns=['fecha_hechos'],aggfunc='count')
preg04.to_excel(writer,'Pregunta04')
writer.save()

"##################################"
"Creamos la Tabla para la Preguna 05"

preg05=pd.pivot_table(data,index=['alcaldia_hechos'],values=['delito'],columns=['categoria_delito'],aggfunc='count')
preg05.to_excel(writer,'Pregunta05')
writer.save()


"##################################"
"Creamos la Tabla para la Preguna 06"

preg06=pd.pivot_table(data,index=['alcaldia_hechos'],values=['delito'],columns=['ao_hechos','mes_hechos'],aggfunc='count')
preg06.to_excel(writer,'Pregunta06')
writer.save()

#LIBRERÍAS UTILIZADAS
import math

#CALCULAR EL NÚMERO DE ESTACIONES QUE TIENE LA INDUSTRIA 
n_estaciones = int(input("¿Cuántas estaciones quieres que tenga tu industria?: "))
print ("")
producciones = []
tiempos_ciclo = []
for i in range(1, n_estaciones + 1):
    #CALCULAR LA PRODUCCIÓN QUE HACE CADA ESTACIÓN (U/H)
    produccion = float(input(f"Introduce la producción en unidades/hora (u/h) de la estación {i}: "))
    producciones.append(produccion)
    #Calcular el tiempo de ciclo por cada estación
    calcular_tiempo_ciclo = 60 / produccion
    tiempos_ciclo.append(calcular_tiempo_ciclo)
    #Calcular el lead time de la industria
    lead_time = sum(tiempos_ciclo)

#TIEMPOS DE CICLO
print("TIEMPOS DE CICLO:")
for i in range(len(tiempos_ciclo)):
    print(f"El tiempo de ciclo de la Estación {i+1}: {tiempos_ciclo[i]:.0f} min/uni")
  
#LEAD TIME
print("LEAD TIME:")
print (f"El lead time es de : {lead_time:.1f} minutos")

#TAKT TIME
takt_time = max(tiempos_ciclo)
print ("TAKT TIME")
print ("El takt time de la industria es de :",takt_time,"minutos")

#CUELLO DE BOTELLA
cuello_de_botella = tiempos_ciclo.index(max(tiempos_ciclo)) + 1
print ("CUELLO DE BOTELLA")
print ("La estación que está haciendo cuello de botella es la estación:",cuello_de_botella)

#WORK IN PROGRESS
wip = lead_time * 1/takt_time
print (f"El work in progress de tu industria es de : {wip:.2f} unidades")

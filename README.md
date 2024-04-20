# Sequential-Ordering-Problem (SOP)

## 1.-Introducción ##

El ordenamiento secuencial es un problema fundamental en diversos ámbitos, desde la informática hasta la logística y la ingeniería, donde la eficiencia en la organización de datos es esencial para optimizar procesos y mejorar el rendimiento de sistemas y aplicaciones. Este problema consiste en la disposición ordenada de una secuencia de elementos de acuerdo con algún criterio específico, como el valor numérico, alfabético o alguna otra medida relevante.

En la era actual, caracterizada por el crecimiento exponencial de la cantidad de datos generados y procesados, la necesidad de algoritmos eficientes de ordenamiento se ha vuelto más acuciante que nunca. A medida que enfrentamos conjuntos de datos cada vez más grandes y complejos, la búsqueda de métodos de ordenamiento óptimos se convierte en un desafío crucial para garantizar el rendimiento y la escalabilidad de los sistemas informáticos y logísticos.

En este contexto, el presente documento propone una solución innovadora para abordar el problema de ordenamiento secuencial mediante la aplicación de la metodología de recocido simulado. El recocido simulado es una técnica inspirada en los procesos de enfriamiento metalúrgico, que busca encontrar soluciones óptimas explorando el espacio de búsqueda de manera probabilística y adaptativa.

A través de la aplicación de recocido simulado, se pretende desarrollar un algoritmo eficiente y flexible capaz de manejar grandes conjuntos de datos y adaptarse a diferentes criterios de ordenamiento. Esta propuesta busca no solo ofrecer una solución efectiva al problema de ordenamiento secuencial, sino también explorar nuevas perspectivas en la aplicación de técnicas de optimización en el ámbito de la ciencia de la computación y la ingeniería.

En las siguientes secciones, se presentará en detalle la formulación del problema, la descripción del algoritmo de recocido simulado propuesto y los resultados de su aplicación en diferentes escenarios de prueba. Se espera que este trabajo contribuya al avance en el campo del ordenamiento secuencial y sirva como base para futuras investigaciones en el desarrollo de algoritmos de optimización.


## 2.-Problema ##

### 2.1.-Definición del problema ###

El problema de ordenamiento secuencial consiste en encontrar un camino hamiltoniano de costo mínimo, esto quiere decir que se debe encontrar un camino que conecte todos los nodos con el menor costo. La representación del grafo debe ser un grafo dirigido con costos asociados a los ejes y relaciones de precedencia entre los nodos. Al hablar de relaciones de precedencia, nos referimos a una o más reglas en el grafo que indican que nodos se deben visitar primero.Este problema puede verse como una variante del TSP, la diferencia principal recae en que el grafo debe ser asícrono debido a la precedencia. Pero tampoco podemos decir que se trata de un problema ATSP.
De manera formal el problema se define de la siguiente forma;

Sea G=(V,E) un grafo dirigido completo, donde V={0,1,2,3...} es el conjunto de nodos y E={(i,j)|i,j E,V/=j}.) Cada eje (i,j) perteneciente a E tiene un costo asociado Cij>=0 Además, se define el grafo de precedencias P=(V,R) con el mismo conjunto de nodos V.
 
Un camino que recorre todos los nodos sin repetirlos, comenzando en el 0 y terminando en n, y satisface todas las condiciones de precedencia es una solución factible del SOP. El objetivo del SOP es encontrar una solución factible de mínimo costo, donde el costo está dado por la sumatoria de los costos de los ejes que componen el camino.


### 2.2 Aplicaciones ###
Una de las aplicaciones de este problema cuando encontramos alguna situacion como mejoramiento en cadenas de produccion, planificacion y ruteo, por ejemplo:

*Planificacion de produccion:* Minimizar el tiempo de ejecución de varios trabajos, que deben ser procesados en cierto orden por una máquina.

*Optimización:* En el uso de una grúa portuaria eliminando cuellos de botella.

*Problemas de transporte* por ejemplo, minimizar la distancia recorrida por un helicóptero que debe transportar personal técnico entre diferentes plataformas en una compañía petrolera.

*Optimizaciones en fábricas* por ejemplo, en la manufactura del automotor, en el sistema de pintado de los autos, para minimizar costos de cambio de color de la pintura.



### 2.3 Ejemplo ### 
*GRAFO DE EJEMPLO*

![Grafo de ejemplo.](https://github.com/2022B-UTC-IC-Metaheuristics/Sequential-Ordering-Problem/blob/main/Img/Grafo.jpg?raw=true).
*SOLUCION DE GRAFO DE EJEMPLO*

![Solucion de Grafo de ejemplo.]()

*Vector Solucion*

[0, 2, 3, 4, 5, 6, 1, 7]

*Matriz de costo*


| |0 |1 |2 |3 |4 |5 |6 |7 |
|--|--|--|--|--|--|--|--|--|
|*0* |0 |1 |7 |2 |6 |7 |1 |5 |
|*1* |8 |0 |2 |3 |8 |4 | 6 | 7 |
|*2* |9 |1000 |0 |4 |1 |6 |9 |1 |
|*3* |6 |3 |3 |0 |3 |5 |4 |3 |
|*4* |8 |2 |3 |5 |0 |3 |7 |5 |
|*5* |1 |5 |6 |3 |8 |0 |6 |1 |
|*6* |7 |1000 |3 |8 |3 |6 |0 |9 |
|*7* |4 |6 |7 |8 |3 |2 |1 |0 |


## 3.- Modelo
### Función objetivo
La función objetivo para el problema de ordenamiento secuencial es la siguiente: ![](https://latex.codecogs.com/svg.image?\sum&space;C_{ij}&space;&plus;&space;(n&space;*&space;penalizacion))

Donde la *penalización* será igual al costo mayor de toda la matriz de costos y *n* representa el número de reglas de precedencia que no se cumplen.

### Restricciones

Las restricciones con las que cuenta este problema se dividen en dos:
1. Las reglas de precedencia son aquella que indican si un nodo debe visitarse antes que otro, la forma en la que se visitan no es necesariamente consecutiva. Se representa de la siguiente manera: (i < j)
2. La solución que se genera debe de iniciar visitando el nodo cero y terminar con el nodo N

### Representación de la solución
Para poder generar la solución inicial, se debe realizar los siguientes pasos:
- Generar un arreglo de (N - 2) números aleatorios en un intervalo de ([0,1])
- Ordenar de forma ascendente el arreglo de acuerdo al valor.
- Tomar los índices del arreglo ordenado para generar la solución inicial.
- Por último, para completar los nodos a visitar y cumplir con la segunda restricción se añade al inicio del arreglo el nodo (0) y al final el nodo (N)


# No usar imagenes no se ve en fondo negro y dificulta la coompreción

Para el ejemplo que mostramos se tienen (N=8), por lo que se generaron 6 números aleatorios, el vector sin ordenar es el siguiente: 

(0.4661691533999429 => 1)

(0.9900212085683265 => 2)

(0.4876416060768133 => 3)

(0.6887360248200161 => 4)

(0.027874235454644403 => 5)

(0.7609657561616946 => 6)

Una vez ordenado de forma ascendente  tenemos: 

(0.027874235454644403 => 5)

(0.4661691533999429 => 1)

(0.4876416060768133 => 3)

(0.6887360248200161 => 4)

(0.7609657561616946 => 6)

(0.9900212085683265 => 2)

Por lo que la representación de la solución inicial, una vez agregados los nodos inicial y final quedaría de la siguiente manera: ([0, 5, 1, 3, 4, 6, 2, 7]) . Esto indica el orden en el que se deben ir visitando los nodos.

### Solución vecino
Una vez ya obtenida la solución inicial, para generar su solución vecino se debe realizar lo siguiente:
- Obtener dos números aleatorios entre 1 y N-2 (para no alterar el primer y último nodo), que representaran los indices de los nodos a intercambiar.
- Proceder a realizar el intercambio entre los nodos.

Números generados (2) y  (6)
Solución inicial: ([0, 5, 1, 3, 4, 6, 2, 7]) Solución vecina: ([0, 5, 1, 2, 4, 6, 3, 7])

## 3.5- Vecindad como penalización

Otra forma de penalizar es checar la distancia entre los nodos en su valor numérico, es decir entre más alejado estén dos números mayor es la penalización

## 4.- Instancias

### 4.1 Propuesta de instancias ###

- NAME: ESC11.sop
- TYPE: SOP
- COMMENT: Received by Norbert Ascheuer / Laureano Escudero

| |0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |10 |11 |12 |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|*0* |0   |0  |0  |0  |0  |0  |0  |0  |0  |0  |0  |0  |1000000  |
|*1* |-1    |0  |387  |440  |682  |657  |584  |688  |708  |362  |357  |927    |0|
|*2* |-1   |-1    |0   |10  |935  |439  |127  |769  |498  |836  |341  |956    |0|
|*3* |-1   |-1   |-1    |0  |596  |865   |70  |513  |512  |373  |824  |220    |0|
|*4* |-1  |319  |277  |439    |0  |428  |212  |412  |771  |620  |651  |605    |0|
|*5* |-1   |-1   |-1   |60  |988    |0  |326  |279  |687  |295  |738  |270    |0|
|*6* |-1  |312  |158  |704  |881  |696    |0  |277 |413  |396  |268  |156    |0|
|*7* |-1  |512  |939  |784  |271  |432  |771    |0  |279 |436   |31  |444    |0|
|*8* |-1  |875  |927  |364  |629  |419  |788  |923    |0  |858  |761  |139    |0|
|*9* |-1  |365   |43  |766  |924  |845  |437  |395  |991    |0  |980  |359    |0|
|*10* |-1  |978  |839  |918  |822  |885  |276   |96  |537  |211    |0  |608    |0|
|*11* |-1  |864  |168  |211  |455  |543  |904  |412  |535  |954  |971    |0    |0|
|*12* |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1    |0|

- NAME: ESC07.sop
- TYPE: SOP
- COMMENT: Received by Norbert Ascheuer / Laureano Escudero

| |0 |1 |2 |3 |4 |5 |6 |7 |8 |
|--|--|--|--|--|--|--|--|--|--|
|*0*|0    |0    |0    |0    |0    |0    |0    |0 |1000000|
|*1*|-1    |0  |100  |200   |75    |0  |300  |100    |0|
|*2*|-1  |400    |0  |500  |325  |400  |600    |0    |0|
|*3*|-1  |700  |800    |0  |550  |700  |900  |800    |0|
|*4*|-1   |-1  |250  |225    |0  |275  |525  |250    |0|
|*5*|-1   |-1  |100  |200   |-1    |0   |-1   |-1    |0|
|*6*|-1   |-1 |1100 |1200 |1075 |1000    |0 |1100    |0|
|*7*|-1   |-1    |0  |500  |325  |400  |600    |0    |0|
|*8*|-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1    |0|

- NAME: ESC25.sop
- TYPE: SOP
- COMMENT: Received by Norbert Ascheuer / Laureano Escudero

| |0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|*0*|0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0    |0 |1000000|
|*1*|-1    |0  |423  |465  |762  |945  |294  |513  |656  |873  |356  |503    |0   |39  |610  |675  |308  |926  |512    |0  |660  |541  |949  |482  |860  |904    |0|
|*2*|-1  |666    |0  |401  |800  |535  |685  |204  |504  |277  |136  |357  |122   |50  |939  |709  |480  |545  |365  |270  |219   |67  |875  |696  |300  |909    |0|
|*3*|-1  |133  |638    |0  |484  |438  |602  |548  |399   |49  |279  |187  |919  |393  |625  |960   |89  |952  |853  |459  |491  |597  |491  |981  |697  |351    |0|
|*4*|-1  |521  |266  |402    |0  |472  |492   |44   |49  |990  |841   |12  |932  |386  |750  |382  |353  |913   |44  |251  |300  |243  |550  |938  |210  |709    |0|
|*5*|-1    |3  |155  |120  |104    |0  |504   |17   |66  |811  |114  |191   |91  |385  |474  |675  |180   |90  |662  |823  |895  |699  |248  |591  |823  |410    |0|
|*6*|-1   |-1  |251  |652   |70  |953    |0  |586  |940  |885  |798  |479  |445  |433  |404  |921  |108  |686  |688  |768  |590  |229  |251  |562  |756  |257    |0|
|*7*|-1  |753  |347  |527  |501  |440    |8    |0  |987  |342  |579  |489  |948  |654   |75  |900  |685  |961  |871  |440  |769  |673  |202  |631  |678  |876    |0|
|*8*|-1  |276  |197  |758    |7  |765  |893  |403    |0  |344  |380  |691  |553  |653  |473  |507  |511  |844  |890  |865  |779  |658  |344  |662  |967  |731    |0|
|*9*|-1   |30  |408  |554  |613  |611  |468  |899  |503    |0  |821  |317  |491  |758  |668  |879  |971  |893  |713  |357  |947  |484  |161  |679  |976  |237    |0|
|*10*|-1  |867  |691  |536   |82  |655  |266  |185  |185  |520    |0  |891  |381  |774  |333  |386  |614  |840  |691   |86  |313  |329  |734  |415  |298  |728    |0|
|*11*|-1   |-1  |816  |623  |582  |585  |768  |181  |211  |234  |966    |0  |681  |420  |334  |814   |34  |647  |744  |968  |417  |983  |914  |444  |235  |725    |0|
|*12*|-1   |-1   |80  |814  |233  |668   |-1  |931   |-1  |374  |929  |331    |0  |112  |481  |177  |984  |940  |484  |618  |386  |356  |703  |869  |967    |6    |0|
|*13*|-1  |745  |574  |683  |803  |313  |736   |89  |458  |196  |640  |510  |271    |0  |445  |904  |542  |430  |288  |437   |48  |926  |210  |119  |900  |710    |0|
|*14*|-1  |494  |811  |381  |447  |149   |58  |968  |679  |973  |580  |785  |921  |202    |0  |740  |974  |480  |860  |680  |449  |779  |491  |623  |457  |219    |0|
|*15*|-1  |385  |749   |80  |389   |53  |247  |892   |68  |789  |619  |876  |489   |-1  |458    |0  |571  |661  |127  |649  |150   |46  |954  |934  |869  |926    |0|
|*16*|-1   |-1   |20  |562  |188   |76  |907  |303  |635  |279  |848  |169  |661  |563  |802  |344    |0  |940  |608   |56  |917  |320  |703  |302  |886  |816    |0|
|*17*|-1  |212  |723  |738  |723  |374  |300   |84  |510   |80  |919   |18  |598  |576  |915  |169  |352    |0  |584  |234   |50  |497  |174  |394   |38  |892    |0|
|*18*|-1  |562  |918  |325  |646  |449  |856  |109  |810  |494  |736  |581   |62  |661  |721  |149  |565  |143    |0  |986  |496  |938   |46  |237  |627  |652    |0|
|*19*|-1   |-1  |994  |787  |374  |103  |178  |333  |578   |74  |850   |-1  |712  |199  |493  |253  |572  |751  |854    |0  |611  |545  |460  |266  |420  |974    |0|
|*20*|-1  |350  |838  |240  |436  |482   |87  |750   |30  |644  |317  |989  |417  |968  |358  |926   |69  |831  |144  |342    |0  |204  |197  |795  |683  |717    |0|
|*21*|-1  |291  |425  |637  |836   |79  |349  |365   |30  |906  |613  |157  |249   |33  |878  |424  |742    |9  |193  |754  |260    |0  |753  |252  |990  |823    |0|
|*22*|-1  |659  |125  |452   |41  |654  |805  |632  |848  |950  |576  |986  |570  |573  |926  |635  |932   |-1  |819  |483  |603  |639    |0  |148  |818  |107    |0|
|*23*|-1  |917  |792  |684  |536  |515  |645  |121  |830  |365  |693  |758  |222  |160  |622  |383  |975  |859  |694  |404  |441  |141  |109    |0  |191  |185    |0|
|*24*|-1  |664  |773  |577  |682  |281  |310  |352  |846  |858  |674  |540  |707  |516  |630  |866  |449  |430  |797  |938  |936   |22  |372  |930    |0   |59    |0|
|*25*|-1  |746  |126   |68  |487   |-1  |224  |978  |405  |796  |858  |205  |107  |386  |243  |596  |258  |272   |85  |234  |385  |978  |292  |449  |242    |0    |0|
|*26*|-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1    |0|

### 4.2 Ejemplo ###
El formato del archivo es csv en el que se encuentran almacenados la matriz de costos y la matriz de precedencia.

Dentro de este repositorio se encuentran 2 archivos, el primer archivo es un ejemplo con 100 nodos el segundo con 2500 nodos y con 15 000 nodos, este último está en la siguiente [liga](https://drive.google.com/file/d/1qvtI9ea8AAPUGQeJUUcDSoUcB3g6PM-f/view?usp=sharing).

Python
#funcion para obtener el costo

def obtenerCosto (solucion, costos, reglas):
  #obtener el total de nodos -1 (no es necesario revisar el ultimo nodo)
  nodos = len(solucion) -1

  #se obtine el costo máximo de la tabla
  costoMax = max (max(fila) for fila in costos)
  costoTotal = 0

  #se suman los costos C de la solución
  for i in range(nodos):
    costoTotal += costos[solucion[i]][solucion[i+1]]
  n =  presedencia(solucion, reglas)
  costoTotal += n* costoMax  
  return costoTotal


Python
def presedencia(solucion, rules):
  #tiene que variar estos arreglos dependiendo de la cantidad de reglas
  auxB = np.zeros(len(rules))
  cont = 0

  for i in range (len(solucion)):
    for j in range(len(rules)):
      if rules[j][0] == solucion[i]:
        auxB[j]+=1
      if auxB[j]== 1:
        if rules[j][1] == solucion[i]:
          auxB[j]+=1
  for i in range(len(auxB)):
    if auxB[i] <2:
      cont +=1
  return cont


Python
def solucionInicial(numNodos,reglas):
    solucionTemp = []
    solucion = []
    #generacion de numeros aleatorios con su indice para obtener la primera solucion
    for i in range(numNodos-2):
        solucionTemp.append([i+1,random.random()])
    #Se reordenan para poder decidir en que orden visitar los nodos
    solucionTemp.sort(key=itemgetter(1))
    # El primero nodo debe ser siempre el cero
    solucion.append(0)
    #agregar los demas nodos
    for i in list(solucionTemp):
        solucion.append(i[0])
    #El ultimo nodo debe ser numNodos-1
    solucion.append(numNodos-1)
    solucion = corregirPrecedencia(solucion[:],reglas,numNodos)
    return solucion
     


Python
def solucionVecino(solucion,reglas):
    #generar las posiciones a cambiar
    vecino = solcion.copy()
    pos1 = random.randint(1,len(solucion)-2)
    pos2 = random.randint(1,len(solucion)-2)
    while (pos1 == pos2):
        pos2 = random.randint(1,len(solucion)-2)
    #print(pos1, ',', pos2)
    #Relizamos el cambio de acuerdo a los indices 
    vecino[pos1],vecino[pos2] = vecino[pos2],vecino[pos1]
    vecino = corregirPrecedencia(vecino[:],reglas,len(vecino))
    return vecino


Python
def corregirPrecedencia(solucion, reglas, numNodos):
    # Se recorre la lista de reglas
    for regla in reglas:
        nodoA = regla[0]
        nodoB = regla[1]

        # Se busca la posición de los nodos en la solución actual
        posA = solucion.index(nodoA)
        posB = solucion.index(nodoB)

        # Si la posición de B es menor que la de A, se intercambian los nodos
        if posB < posA:
            solucion[posA], solucion[posB] = solucion[posB], solucion[posA]

    # Se verifica que la solución corregida contenga todos los nodos
    assert set(solucion) == set(range(numNodos))

    return solucion



Python
def readFile(size, name):
    m = np.zeros((0), dtype=int)
    m_prec = np.zeros((0), dtype=int)
    
    with open(name, newline='') as File:  
        reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
        i=0
        for row in File:
            
            row = row.rstrip()
            separador = ","
            row = row.split(",")
            row = list(map(int, row))
            m_np = np.array(row)
            
            if i < size :
                m = np.append(m, m_np, axis=0)
                #print(m_np)
            else:
                m_prec = np.append(m_prec, m_np, axis=0)
            i+=1
    
    m = np.array(m).reshape(size,size)
    m_prec = np.array(m_prec).reshape(int((len(m_prec)/2)),2)
    return m, m_prec


Python
#Lectura de los datos
name = '100.txt'
nodos = 100
m, m_prec = readFile(nodos, name)

print(f'{m}')



Python
def local_search(cost_matrix, reglas, numNodos, max_iterations):
    # Algoritmo de búsqueda local para el SO con matriz de costos
    
    best_seq = solucionInicial(numNodos, reglas)
    best_cost = obtenerCosto(best_seq, cost_matrix, reglas )
    for i in range(max_iterations):
        # Intercambia  nodos aleatorios en la secuencia
        new_sol = solucionVecino(best_seq, reglas)
        # Calcula el costo de la nueva secuencia
        cost = obtenerCosto(new_sol,cost_matrix,reglas)
        # Si la nueva secuencia es mejor, actualiza la mejor solución
        if cost < best_cost:
            best_seq = new_sol.copy()
            best_cost = cost
    return best_seq, best_cost



Python


best_seq, best_cost = local_search(m, m_prec, 100, 10000)

print (f'El mejor costo es {best_cost} con la siguiente secuencia \n{best_seq}')


Los ejemplos de las instancias están en archivos con extensión .csv.


Para la primera instancia con *100 nodos* nuestros resultados fueron:
- Costo 747
- Tiempo 0.76108 seg.

## 5.- Ejemplo de ejecución
Como ejemplo de ejecución, ocuparemos la red mostrada en la sección *2.3 Ejemplo*

Los parametros ocupados para el recocido simulado fueron;

- temperatura 100
- alpha 0.5

y las salidas fueron las siguientes;
- Solucion: [0, 1, 5, 3, 6, 2, 4, 7]
- Costo: 21
- Tiempo 0.012 seg.

Con el simple hecho de visualizar la red de nodos se puede deducir el costo menor, por lo que tiene una solución exacta y es *[0, 1, 3, 6, 2, 4, 5, 7]* con un costo mínimo de *16*

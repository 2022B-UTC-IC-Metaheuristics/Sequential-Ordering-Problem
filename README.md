# Sequential-Ordering-Problem

## 1.-Introducción ##

El presente documento plantea una propuesta de solucion para la codificacion del problema de ordenamiento secuencial, en el cual se utiliza la metodología de recocido simulado.


## 2.-Problema ##

### 2.1.-Definición del problema ###

El problema de ordenamiento secuencial consiste en encontrar un camino hamiltoniano de costo mínimo, esto quiere decir que se debe encontrar un camino que conecte todos los nodos con el menor costo. La representación del grafo debe ser un grafo dirigido con costos asociados a los ejes y relaciones de precedencia entre los nodos. Al hablar de relaciones de precedencia, nos referimos a una o más reglas en el grafo que indican que nodos se deben visitar primero.Este problema puede verse como una variante del TSP, la diferencia principal recae en que el grafo debe ser asícrono debido a la precedencia. Pero tampoco podemos decir que se trata de un problema ATSP.
De manera formal el problema se define de la siguiente forma;

Sea ![](https://latex.codecogs.com/svg.image?G=(V,E)) un grafo dirigido completo, donde ![](https://latex.codecogs.com/svg.image?V={0,1,2,3...}) es el conjunto de nodos y ![](https://latex.codecogs.com/svg.image?E={(i,j)|&space;i,j&space;E&space;V,/=j}.) Cada eje ![](https://latex.codecogs.com/svg.image?(i,j)&space;\in&space;&space;E) tiene un costo asociado ![](https://latex.codecogs.com/svg.image?Cij>=0.) Además, se define el grafo de precedencias ![](https://latex.codecogs.com/svg.image?P=(V,R)) con el mismo conjunto de nodos V.

Un camino que recorre todos los nodos sin repetirlos, comenzando en el 0 y terminando en n, y satisface todas las condiciones de precedencia es una solución factible del SOP. El objetivo del SOP es encontrar una solución factible de mínimo costo, donde el costo está dado por la sumatoria de los costos de los ejes que componen el camino.


### 2.2 Aplicaciones ###
Una de las aplicaciones de este problema cuando encontramos alguna situacion como mejoramiento en cadenas de produccion, planificacion y ruteo, por ejemplo:

**Planificacion de produccion:** Minimizar el tiempo de ejecución de varios trabajos, que deben ser procesados en cierto orden por una máquina.

**Optimización:** En el uso de una grúa portuaria eliminando cuellos de botella.

**Problemas de transporte** por ejemplo, minimizar la distancia recorrida por un helicóptero que debe transportar personal técnico entre diferentes plataformas en una compañía petrolera.

**Optimizaciones en fábricas** por ejemplo, en la manufactura del automotor, en el sistema de pintado de los autos, para minimizar costos de cambio de color de la pintura.


### 2.3 Ejemplo ### 
**GRAFO DE EJEMPLO**

![Grafo de ejemplo.](https://graphonline.ru/tmp/saved/hh/hhFcwtLeeqzqzogz.png)  

**SOLUCION DE GRAFO DE EJEMPLO**

![Solucion de Grafo de ejemplo.](https://graphonline.ru/tmp/saved/gY/gYHqUXAsCVVxnMec.png)

**Vector Solucion**

[0, 2, 3, 4, 5, 6, 1, 7]

**Matriz de costo**


| |0 |1 |2 |3 |4 |5 |6 |7 |
|--|--|--|--|--|--|--|--|--|
|**0** |0 |1 |7 |2 |6 |7 |1 |5 |
|**1** |8 |0 |2 |3 |8 |4 | 6 | 7 |
|**2** |9 |1000 |0 |4 |1 |6 |9 |1 |
|**3** |6 |3 |3 |0 |3 |5 |4 |3 |
|**4** |8 |2 |3 |5 |0 |3 |7 |5 |
|**5** |1 |5 |6 |3 |8 |0 |6 |1 |
|**6** |7 |1000 |3 |8 |3 |6 |0 |9 |
|**7** |4 |6 |7 |8 |3 |2 |1 |0 |


## 3.- Modelo
### Función objetivo
La función objetivo para el problema de ordenamiento secuencial es la siguiente: ![](https://latex.codecogs.com/svg.image?\sum&space;C_{ij}&space;&plus;&space;(n&space;*&space;penalizacion))

Donde la **penalización** será igual al costo mayor de toda la matriz de costos y **n** representa el número de reglas de precedencia que no se cumplen.

El siguiente fragmento de código indica el proceso para calcular el valor de la función objetivo.

```Python
def obtenerCosto(solucion,costos,reglas):
    #obtener el total de nodos, se pone -1 porque no es necesario recorrer el ultimo
    nodos = len(solucion)-1 
    #Se obtiene el costo maximo de la tabla (es el que se usara para la penalización)
    costoMax = max(max(fila) for fila in a)
    costoTotal = 0
    # su suman los costos C de la solución
    for i in range(nodos):
        costoTotal += costos[solucion[i]][solucion[i+1]] 
    n = presedencia(solucion,reglas)
    costoTotal += n * costoMax
    return costoTotal
```
Para revisar las precedencias se utilizo la siguiente función

```Python
def presedencia(solucion,rules):
    #tiene que variar estos arreglos dependiendo de cuantas reglas aya.
    auxB = np.zeros(len(rules))
    cont = 0
    for i in range(len(solucion)):
        for j in range(len(rules)):       
            if rules[j][0] == solucion[i] :
                auxB[j]+=1       
            if auxB[j] == 1 :
                if rules[j][1] == solucion[i] :
                    auxB[j]+=1               
    for i in range(len(auxB)):
        if auxB[i] < 2 :
            cont+=1
    return cont
```

### Restricciones

Las restricciones con las que cuenta este problema se dividen en dos:
1. Las reglas de precedencia son aquella que indican si un nodo debe visitarse antes que otro, la forma en la que se visitan no es necesariamente consecutiva. Se representa de la siguiente manera: ![](https://latex.codecogs.com/svg.image?i&space;<&space;j&space;)
2. La solución que se genera debe de iniciar visitando el nodo cero y terminar con el nodo N

### Representación de la solución
Para poder generar la solución inicial, se debe realizar los siguientes pasos:
- Generar un arreglo de ![](https://latex.codecogs.com/svg.image?N&space;-&space;2) números aleatorios en un intervalo de ![](https://latex.codecogs.com/svg.image?[0,1])
- Ordenar de forma ascendente el arreglo de acuerdo al valor.
- Tomar los índices del arreglo ordenado para generar la solución inicial.
- Por último, para completar los nodos a visitar y cumplir con la segunda restricción se añade al inicio del arreglo el nodo ![](https://latex.codecogs.com/svg.image?0) y al final el nodo ![](https://latex.codecogs.com/svg.image?N)

```Python
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
```

Para el ejemplo que mostramos se tienen ![](https://latex.codecogs.com/svg.image?N=8), por lo que se generaron 6 números aleatorios, el vector sin ordenar es el siguiente: 

![](https://latex.codecogs.com/svg.image?0.4661691533999429&space;\to&space;1)

![](https://latex.codecogs.com/svg.image?0.9900212085683265&space;\to&space;2)

![](https://latex.codecogs.com/svg.image?0.4876416060768133&space;\to&space;3)

![](https://latex.codecogs.com/svg.image?0.6887360248200161&space;\to&space;4)

![](https://latex.codecogs.com/svg.image?0.027874235454644403&space;\to&space;5)

![](https://latex.codecogs.com/svg.image?0.7609657561616946&space;\to&space;6)

Una vez ordenado de forma ascendente  tenemos: 

![](https://latex.codecogs.com/svg.image?0.027874235454644403&space;\to&space;5)

![](https://latex.codecogs.com/svg.image?0.4661691533999429&space;\to&space;1)

![](https://latex.codecogs.com/svg.image?0.4876416060768133&space;\to&space;3)

![](https://latex.codecogs.com/svg.image?0.6887360248200161&space;\to&space;4)

![](https://latex.codecogs.com/svg.image?0.7609657561616946&space;\to&space;6)

![](https://latex.codecogs.com/svg.image?0.9900212085683265&space;\to&space;2)

Por lo que la representación de la solución inicial, una vez agregados los nodos inicial y final quedaría de la siguiente manera: ![](https://latex.codecogs.com/svg.image?[0,&space;5,&space;1,&space;3,&space;4,&space;6,&space;2,&space;7]) . Esto indica el orden en el que se deben ir visitando los nodos.

### Solución vecino
Una vez ya obtenida la solución inicial, para generar su solución vecino se debe realizar lo siguiente:
- Obtener dos números aleatorios entre 1 y N-2 (para no alterar el primer y último nodo), que representaran los indices de los nodos a intercambiar.
- Proceder a realizar el intercambio entre los nodos.

```Python
def solucionVecino(solucion,reglas):
    #generar las posiciones a cambiar
    pos1 = random.randint(1,len(solucion)-2)
    pos2 = random.randint(1,len(solucion)-2)
    while (pos1 == pos2):
        pos2 = random.randint(1,len(solucion)-2)
    #print(pos1, ',', pos2)
    #Relizamos el cambio de acuerdo a los indices 
    solucion[pos1],solucion[pos2] = solucion[pos2],solucion[pos1]
    solucion = corregirPrecedencia(solucion[:],reglas,len(solucion))
    return solucion
```

Números generados ![](https://latex.codecogs.com/svg.image?2) y  ![](https://latex.codecogs.com/svg.image?6)
Solución inicial: ![](https://latex.codecogs.com/svg.image?[0,&space;5,&space;1,&space;3,&space;4,&space;6,&space;2,&space;7]) Solución vecina: ![](https://latex.codecogs.com/svg.image?[0,&space;5,&space;1,&space;2,&space;4,&space;6,&space;3,&space;7])

## 4.- Instancias

### 4.1 Propuesta de instancias ###

NAME: ESC11.sop
TYPE: SOP
COMMENT: Received by Norbert Ascheuer / Laureano Escudero

| |0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |10 |11 |12 |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|**0** |0   |0  |0  |0  |0  |0  |0  |0  |0  |0  |0  |0  |1000000  |
|**1** |-1    |0  |387  |440  |682  |657  |584  |688  |708  |362  |357  |927    |0|
|**2** |-1   |-1    |0   |10  |935  |439  |127  |769  |498  |836  |341  |956    |0|
|**3** |-1   |-1   |-1    |0  |596  |865   |70  |513  |512  |373  |824  |220    |0|
|**4** |-1  |319  |277  |439    |0  |428  |212  |412  |771  |620  |651  |605    |0|
|**5** |-1   |-1   |-1   |60  |988    |0  |326  |279  |687  |295  |738  |270    |0|
|**6** |-1  |312  |158  |704  |881  |696    |0  |277 |413  |396  |268  |156    |0|
|**7** |-1  |512  |939  |784  |271  |432  |771    |0  |279 |436   |31  |444    |0|
|**8** |-1  |875  |927  |364  |629  |419  |788  |923    |0  |858  |761  |139    |0|
|**9** |-1  |365   |43  |766  |924  |845  |437  |395  |991    |0  |980  |359    |0|
|**10** |-1  |978  |839  |918  |822  |885  |276   |96  |537  |211    |0  |608    |0|
|**11** |-1  |864  |168  |211  |455  |543  |904  |412  |535  |954  |971    |0    |0|
|**12** |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1   |-1    |0|
El formato del archivo es csv en el que se encuentran almacenados la matriz de costos y la matriz de precedencia.

Dentro de este repositorio se encuentran 2 archivos, el primer archivo es un ejemplo con 100 nodos el segundo con 2500 nodos y con 15 000 nodos, este último está en la siguiente [liga](https://drive.google.com/file/d/1qvtI9ea8AAPUGQeJUUcDSoUcB3g6PM-f/view?usp=sharing).

```Python
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
```

Los ejemplos de las instancias están en archivos con extensión .csv para leer los datos deberá hacerlo como en el siguiente ejemplo:
El archivo .csv debe estár en el directorio de trabajo.
```Python
name = 'datos50.csv'
m, m_prec = readFile(nodos, name)
```
**donde:** 
- m es la matriz de costos.
- m_prec es el arreglo de precedencias.
- name es el nombre del archivo con todo y extensión.

Para la primera instancia con **100 nodos** nuestros resultados fueron:
- Costo 1059
- Tiempo 0.76108 seg.

## 5.- Ejemplo de ejecución
Como ejemplo de ejecución, ocuparemos la red mostrada en la sección **2.3 Ejemplo**

Los parametros ocupados para el recocido simulado fueron;

- temperatura 100
- alpha 0.5

y las salidas fueron las siguientes;
- Solucion: [0, 1, 5, 3, 6, 2, 4, 7]
- Costo: 21
- Tiempo 0.012 seg.

Con el simple hecho de visualizar la red de nodos se puede deducir el costo menor, por lo que tiene una solución exacta y es **[0, 1, 3, 6, 2, 4, 5, 7]** con un costo mínimo de **16**

# **Sistema de recomendación: Métodos de filtrado colaborativo**
## Luciano Sekulic Gregoris

# **Código**

### **Argumentos**
Para el correcto funcionamiento es necesario introducir los siguientes argumentos apreciados en el fragmento de código.

```python
ps.add_argument("-f", "--file", required=True)
ps.add_argument("-n", "--neighbours", required=True)
ps.add_argument("-m", "--metric", choices=["pearson", "coseno", "euclidea"], required=True)
ps.add_argument("-p", "--prediction", choices=["simple", "media",], required=True)
```


### **Matriz de predicciones**
Una vez creada la matriz de predicciones, se convierten los numeros a enteros y en el caso de que hubiesen proyecciones vacías, se sustituyen por un -1. Esto se realiza para poder trabajar con un solo tipo de dato. A continuación se deja el fragmento de código referido a la creación de la matriz.

```python
mat: list = list(np.loadtxt(open(args.file), delimiter=" ", dtype=str))
for i in range(len(mat)):
  mat[i] = list(mat[i]) 
  for j in range(len(mat[i])):
    if mat[i][j].isdigit() == False:
      mat[i][j] = int(-1)
    else:
      mat[i][j] = int(mat[i][j])
```

### **Resultados**
El resultado final dependerá de la opción que elija el usuario ya que será el encargado de elegir las funciones de predicción. Si nos encontramos con un -1, se sustituirá por el elemento que devuelva la predicción. Para su correcto funcionamiento se le deberá pasar loq eu aparece en el fragmento de código más abajo que sería la posicion del elemento en la matriz, la matriz, numero de vecinos y la función de similitud que se va a usar.

```python
mat[i][j] = pred.prediccion_simple(i, j, mat, int(args.neighbours), metric)
```


## **Funciones**
Se han creado dos funciones fundamentales que son la prediccion simple y la diferencia con la media. Ambas funcionan en un principio de la misma forma, primero se calculan los vecinos con la funcion `get_neighbours` y segundo se eliminan las columnas con predicciones vacías. Posteriormente cambian su funcionamiento de la siguiente manera:
   * predicción simple: Se suma el producto calculado de la similitud con el valor del vecino y se divide el resultado por el sumatorio del valor absoluto de las predicciones.
   * diferencia con la media: Se suma el producto calculado de la similitud con el valor del vecino, menos el valor medio de las predicciones, luego se dividirá el resultado por el sumatorio del valor absoluto de las predicciones. Por último  se realizala suma entre la media de las predicciones y lo que dio anteriormente.  

Luego se han creado otras funciones para poder calcular lo anterior tales como:
* get_neighbours: devuelve los vecinos que se desean
* get_avg: devuelve la media de las predicciones sobre la posición a evaluar.

Se han creado tres funciones de similitud para poder realizar el calculo de similitud entre los vecinos. Son las siguientes:
* Correlación de pearson que calcula la relacion lineal entre dos variables
* Distancia del coseno que calcula el prodcuto normalizado entre dos variables
* Distancia euclidea que calcula la distancia trigonometrica entre dos puntos
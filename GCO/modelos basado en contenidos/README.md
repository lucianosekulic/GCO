# **Sistema de recomendación: Modelos basados en contenido**
## Luciano Sekulic Gregoris

# **Código**

### **Funciones y argumentos**
Para el correcto funcionamiento es necesario introducir el siguiente argumento como se aprecia en el fragmento de código, para poder intriducir el fichero.

```python
ps.add_argument("-f", "--file", required=True)
```

Luego para poder trabajar con una matriz de palabras para crear una oración es necesario eliminar las stopwords en ingles y ponerlas todas en minusculas, mediante `eliminar_stopwords` y `.lower`respectivamente.

```python
matrix.append(ev.eliminar_stopwords(re.sub(r'[^\w]', ' ', line).lower()))
```

Después para evaluar el documento después de realizar un procesado previo, se usan las funciones `freq_term` `freq_inversa_doc` y `tf_idf` donde se realiza lo siguiente:
* freq_term: Calcula la frecuencia de las palabras en el documento dado por el usuario.
* freq_inversa_doc: Realiza el calculo de la frecuencia inversa de las palabras del documento.
* tf_idf: expresa numericamente la frecuencia de los terminos 


Por ultimo al imprimir el resultado  de los terminos dicho anteriormente, se imprime también la similitud del coseno que viene dada por la siguiente función llamada `calcular_similitud`:

```python
def calcular_similitud(w: list[dict[str]]) -> list[list[int]]:
    resultado: list[list[int]] = list[list[int]]()
    for documento_original in w:
        original: list[int] = list(documento_original.values())
        values: list[int]() = list[int]()
        for documento_comparado in w:
            sim: int = 0
            comparacion: list[int] = list(documento_comparado.values())
            if len(original) > len(comparacion):
                for i in range(len(comparacion)):
                    sim += comparacion[i] * original[i]
            else:
                for i in range(len(original)):
                    sim += comparacion[i] * original[i]
            values.append(sim)
        resultado.append(values)
    return resultado
```
En esta función se puede apreciar que para calcular la similitud del coseno, el documento_original y el documento_comparado se recorren y luego se compara mediante un iterador sim, para saber que palabras se repiten.

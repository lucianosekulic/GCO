from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from math import log



# Calcula el termino de la frecuencia de las palabras en el documento
def freq_term(documento: list[str]) -> dict[str]:
    tf: dict[str] = dict[str]()
    for term in documento:
        if term in tf:
            tf[term] += 1
        else:
            tf[term] = 1
    for term in documento:
        tf[term] /= len(documento)
    return tf


# Calcula la frecuencia del documento de los terminos en la matriz
def freq_documento(term: str, matrix: list[list[str]]) -> int:
    count: int = 0
    for documento in matrix:
        for word in documento:
            if word == term:
                count += 1
    return count

# Realiza el calculo de la inversa de la frecuencia de las palabras del documento
def freq_inversa_doc(documento: list[str], matrix: list[list[str]]) -> dict[str]:
    idf: dict[str] = dict[str]()
    for term in documento:
        if term not in idf:
            idf[term] = log(len(matrix) / freq_documento(term, matrix))
    return idf


# Calcula los tf-idf d los terminos en la matriz
def tf_idf(documento: list[str], tf: dict[str], idf: dict[str]) -> dict[str]:
    w: dict[str] = dict[str]()
    for term in documento:
        if term not in w:
            w[term] = tf[term] * idf[term]
    return w


# Elimina las stopwords del alfabeto en ingles del texto
def eliminar_stopwords(line: str) -> list[str]:
    sentencia: list[str] = list[str]()
    for term in word_tokenize(line):
        if term not in set(stopwords.words('english')):
            sentencia.append(term)
    return sentencia


# Calcula la similitud
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
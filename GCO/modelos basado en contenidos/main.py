import argparse
import re
import modelo_contenido as ev

def main():

    #Se analizan los argumentos, se hace un pre-proceso del texto y se evalua

    ps: argparse.ArgumentParser = argparse.ArgumentParser()
    ps.add_argument("-f", "--file", required=True)
    filename = ps.parse_args().file
    file = open(filename, "r")
    matrix: list[list[str]] = list[list[str]]()
    line: str = file.readline()
    while len(line) > 0:
        matrix.append(ev.eliminar_stopwords(re.sub(r'[^\w]', ' ', line).lower()))
        line = file.readline()

    tf: list[dict[str]] = list[dict[str]]()
    idf: list[dict[str]] = list[dict[str]]()
    w: list[dict[str]] = list[dict[str]]()

    for documento in matrix:
        documento_tf: dict[str] = ev.freq_term(documento)
        documento_idf: dict[str] = ev.freq_inversa_doc(documento, matrix)
        documento_w: dict[str] = ev.tf_idf(documento, documento_tf, documento_idf)
        tf.append(documento_tf)
        idf.append(documento_idf)
        w.append(documento_w)

    # Se imprime el resultado
    filename = filename.split('\\')[-1]
    print("\n")
    print(f"    Modelo basado en contenido - {filename}      ".center(120, "#"))
    print("")
    term = "Term_freq"
    doc = "Doc_freq"
    res = "tf + idf"
    for i in range(len(matrix)):
        print(f"    Articulo {i+1}    ".center(40, "-"))
        print("")
        print("{:>20}{:>10}{:>10}".format(term, doc, res))
        for key, value in tf[i].items():
            print("{:<14}{}{:>10}{:>10}".format(key, "{:.2f}".format(value),
                                                "{:.2f}".format(idf[i][key]),
                                                "{:.2f}".format(w[i][key])))
        print("\n")
    coseno: list[list[int]] = ev.calcular_similitud(w)
    print("")
    print(f"    Similitud del coseno    ".center(40, "-"))
    print("")
    for i in range(len(coseno)):
        for j in range(len(coseno[i])):
            if j != i:
                print(f"cos(A{i+1}, A{j+1}) = {coseno[i][j]}")
    print("")


main()

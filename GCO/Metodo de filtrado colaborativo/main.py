import argparse
import prediccion as pred
import similitud as sim
import numpy as np


# Se procede a evaluar los argumentos
def main():
  ps = argparse.ArgumentParser()
  ps.add_argument("-f", "--file", required=True)
  ps.add_argument("-n", "--neighbours", required=True)
  ps.add_argument("-m", "--metric", choices=["pearson", "coseno", "euclidea"],
                  required=True)
  ps.add_argument("-p", "--prediction", choices=["simple", "media",],
                  required=True)
  args = ps.parse_args()

  if args.metric == "pearson":
    metric = sim.correlacion_pearson
  elif args.metric == "coseno":
    metric = sim.distancia_coseno
  else:
    metric = sim.distancia_euclidea

# creacion de la matriz
  mat: list = list(np.loadtxt(open(args.file), delimiter=" ", dtype=str))
  for i in range(len(mat)):
    mat[i] = list(mat[i]) 
    for j in range(len(mat[i])):
      if mat[i][j].isdigit() == False:
        mat[i][j] = int(-1)
      else:
        mat[i][j] = int(mat[i][j])

  for i in range(len(mat)):
    for j in range(len(mat[i])):
      if mat[i][j] == -1:
        print(f"\n-----------------------------------------------------------")
        print(f"\nse evalua: [{i}, {j}]:")
        if args.prediction == "simple":
          mat[i][j] = pred.prediccion_simple(i, j, mat, int(args.neighbours), metric)
        else:
          mat[i][j] = pred.diferencia_media(i, j, mat, int(args.neighbours), metric)
        print(f"\nse calcula la prediccion para [{i}, {j}]:")
        print(mat[i][j])

  print("\n\n    -Matriz de resultado-    \n")
  for line in mat:
    print(line)
  print("\n")
  

# Arranca el main
main()

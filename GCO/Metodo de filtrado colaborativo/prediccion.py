from numpy.lib.function_base import append, diff
import similitud as sim
import numpy as np


# Realiza la prediccion simple 
def prediccion_simple(i: int, j: int, matrix: list, n: int, metric) -> float:
  neighbours: list = get_neighbours(i, matrix, n)
  simple_neighbours: list = neighbours.copy()
  line: list = matrix[i].copy()
  simple_line: list = line.copy()
  not_nums: list = list()
  num: int = 0
  den: int = 0
  for pos in range(len(line)):
    if line[pos] == -1:
      not_nums.append(pos)
  for n in neighbours:
    for pos in range(len(n)):
      if n[pos] == -1:
        not_nums.append(pos)
  not_nums = list(dict.fromkeys(not_nums))

  simple_line =  np.delete(simple_line, not_nums)
  for i in range(len(neighbours)):
    simple_neighbours[i] =  list(np.delete(simple_neighbours[i], not_nums))

  for n in range(len(simple_neighbours)):
    simil = metric(simple_line, simple_neighbours[n])
    print(f"\nSimilitud entre {line} y {neighbours[n]}")
    print(abs(simil))
    num += simil * neighbours[n][j]
    den += abs(simil)
  return abs(round(num / den))

# Se realiza la diferencia con la media
def diferencia_media(i: int, j: int, matrix: list, n: int, metric) -> float:
  neighbours: list = get_neighbours(i, matrix, n)
  simple_neighbours: list = neighbours.copy()
  line: list = matrix[i].copy()
  simple_line: list = line.copy()
  not_nums: list = list()
  num: int = 0
  den: int = 0
  for pos in range(len(line)):
    if line[pos] == -1:
      not_nums.append(pos)
  for n in neighbours:
    for pos in range(len(n)):
      if n[pos] == -1:
        not_nums.append(pos)
  not_nums = list(dict.fromkeys(not_nums))

  simple_line =  np.delete(simple_line, not_nums)
  for i in range(len(neighbours)):
    simple_neighbours[i] =  list(np.delete(simple_neighbours[i], not_nums))
  
  avg = get_avg(j, matrix)
  for n in range(len(simple_neighbours)):
    simil = metric(simple_line, simple_neighbours[n])
    print(f"\nSimilitud entre {line} y {neighbours[n]}")
    print(abs(simil))
    num += simil * (neighbours[n][j] - avg)
    den += abs(simil)
  return abs(round(avg + (num / den)))


def get_avg(j: int, matrix: list) -> float:
  count: int = 0
  for list in matrix:
    if list[j] != -1:
      count += 1
  return count / len(matrix)

# Calcula los vecinos
def get_neighbours(i: int, matrix: list, n: int) -> list:
  print(f"\nVecinos de: {matrix[i]}")
  neighbours: list = list()
  mat: list = list(matrix.copy())
  numUp: int = round(n / 2)
  numDown: int = round(n - numUp)
  if numUp > i:
    diff = numUp - i
    numDown += diff
    numUp -= diff
  if numDown > (len(matrix) - i - 1):
    diff = numDown - (len(matrix) - i - 1)
    numUp += diff
    numDown -= diff
  for j in range(numDown):
    neighbours.append(list(mat[i + j + 1]))
    print(matrix[i + j + 1])
  for j in range(numUp):
    neighbours.append(list(mat[i - j - 1]))
    print(matrix[i - j - 1])
  return neighbours
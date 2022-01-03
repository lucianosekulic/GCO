from typing import List
from scipy import spatial
import numpy as np



def correlacion_pearson(mainList: list, compareList: list) -> float:
  return np.corrcoef(mainList, compareList)[1][0]

def distancia_euclidea(mainList: list, compareList: list) -> float:
  return spatial.distance.euclidean(mainList, compareList)
  
def distancia_coseno(mainList: list, compareList: list) -> float:
  return 1 - spatial.distance.cosine(mainList, compareList)


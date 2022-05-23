import sys
sys.path.append('')

from identifyOverlap import identifyOverlap
import teste

fotos = [[2, 9, 4, 7], [4, 9, 6, 7], [6, 9, 8, 7]]
overlap = True

while (overlap == True):
    fotos = teste.teste(fotos)
    overlap = fotos[0]
    fotos = fotos[1]
   
print(len(fotos))         
print(fotos)
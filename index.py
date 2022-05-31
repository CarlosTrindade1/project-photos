import sys
sys.path.append('c:/Users/carlo/OneDrive/Documentos/UFMS/1º Semestre/Algoritmos e Programação/project-photos/functions/')

from identifyOverlap import identifyOverlap
from checkOverlapPhotoByPhoto import checkOverlapPhotoByPhoto

fotos = [[3, 9, 6, 3], [2, 4, 7, 1], [4, 12, 10, 7], [11, 5, 17, 2]]
overlap = True

while (overlap == True):
    fotos = checkOverlapPhotoByPhoto(fotos)
    overlap = fotos[0]
    fotos = fotos[1]
   
print(len(fotos))         
print(fotos)
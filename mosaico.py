'''
   Programa: mosaico.py
     Função: Gerar um mosaico de fotos a partir das fotos fornecidas 
        Uso: python mosaico.py <caminho_arquivo_entrada>
             Programador: Carlos Eduardo da Silva Trindade
       Data: 04/06/2022.
'''

# Importação das bibliotecas que contém funcionalidades úteis para o funcionamento do programa
import sys
# Incluir o caminho das bibliotecas internas
sys.path.append('')
from checkOverlapPhotoByPhoto import checkOverlapPhotoByPhoto
from outputCoords import outputCoords


# Lendo o caminho do arquivo que contém os dados de entrada
path = sys.argv[1]

# Definindo as estruturas de dados para armazenar as coordenadas das fotos
photos = []
lines = []

# Realizando a leitura do arquivo
with open(path) as fotos:

    lines = fotos.readlines()

# Adicionando as coordenadas das fotos no vetor 'photos'
for line in lines:
    photos.append(list(map(int, line.split())))

# Definindo controlador de fluxo
overlap = True

# Repetição para realizar a checagem de sobreposição entre as fotos enquanto houver sobreposição
while (overlap == True):
    photos = checkOverlapPhotoByPhoto(photos)
    overlap = photos[0]
    photos = photos[1]

# Realiza a formatação para a saída dos dados
print(len(photos))         
outputCoords(photos)
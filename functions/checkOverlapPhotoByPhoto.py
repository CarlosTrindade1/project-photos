# Importação dos módulos necessários para o funcionamento do programa
from identifyOverlap import identifyOverlap
from deleteDuplicates import deleteDuplicates

'''
# Funcionalidade para checar sobreposição foto por foto
# Recebe um vetor contendo N fotos
# Retorna um indicador de sobreposição e um vetor com as coordenadas das sobreposições
'''
def checkOverlapPhotoByPhoto(photos = []):

    # Definição das estruturas de dados para armazenar as sobreposições, não-sobreposições e um indicador
    overlaps = []
    noOverlaps = []
    overlap = False

    # Itera sobre cada foto do vetor fotos
    for i in range(len(photos)):
        # Inicia o contador de não-sobreposição
        cont = 0

        # Itera sobre cada foto do vetor fotos
        for j in range(len(photos)):
            # Verifica se as fotos comparadas são diferentes
            if (i != j):
                # Checa se há sobreposição entre duas fotos
                # Caso haja, retorna um indicador de sobreposiçao e o menor retângulo que contenha as duas fotos
                result = identifyOverlap(photos[i], photos[j])

                # Verifica o valor do indicador de sobreposição
                if (result[0]):
                    # Caso verdadeiro, adiciona a sobreposição ao vetor sobreposições
                    overlaps.append(result)
                    # Altera para 'verdadeiro' o indicador de sobreposição do módulo
                    overlap = True
                else:
                    # Caso falso, adiciona 1 no contador de não-sobreposição
                    cont += 1
        
        # Verifica se a foto não está em sobreposição com nenhuma outra
        if (cont == len(photos) - 1):
            # Caso verdadeiro, adiciona-a ao vetor de não-sobreposições
            noOverlaps.append(photos[i])

    # Redefine o vetor de fotos
    photos = []
    # Elimina os valores duplicados no vetor de sobreposições
    overlaps = deleteDuplicates(overlaps)

    # Adiciona as sobreposições ao vetor fotos
    for i in range(len(overlaps)):
        photos.append(overlaps[i][1])
    
    # Adiciona as fotos de não-sobreposições ao vetor fotos
    if (len(noOverlaps) > 0):
        for i in range(len(noOverlaps)):
            photos.append(noOverlaps[i])

    # Retorna o marcador de sobreposição e o novo vetor fotos
    return [overlap, photos]
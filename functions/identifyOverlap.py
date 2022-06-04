# Funcionalidade para ordenar as coodenadas em um vetor
# Recebe um vetor com as coordenadas
def orderCoords(photo = []):
    if (photo[0] > photo[1]):
        aux = photo[0]
        photo[0] = photo[1]
        photo[1] = aux
    
    # Retorna o vetor ordenado
    return photo

# Funcionalidade para identificar sobreposição entre duas fotos em um dos eixos cartesianos
# Recebe como parâmentro dois vetores contendo coordenadas de fotos distintas
# Retorna 'verdadeiro' ou 'falso'
def identifyOverlapAxis(photo1 = [], photo2 = []):
    # Ordena as coordenadas dos vetores
    photo1 = orderCoords(photo1)
    photo2 = orderCoords(photo2)

    # Calcula a largura (em relação ao eixo) das fotos
    gapPhoto1 = abs(photo1[0] - photo1[1])
    gapPhoto2 = abs(photo2[0] - photo2[1])

    # Define as estruturas de dados necessárias para o armazenamento das coordenadas
    coordsI = []
    coordsJ = []
    # Define um indicador de sobreposição
    result = False

    # Condição para identificar a maior largura das fotos
    if (gapPhoto1 > gapPhoto2):
        coordsI = photo1
        coordsJ = photo2
    else:
        coordsI = photo2
        coordsJ = photo1
    
    # Condição para identificar sobreposição entre as fotos no determinado eixo cartesiano
    if (coordsI[0] <= coordsJ[0] <= coordsI[1] or coordsI[0] <= coordsJ[1] <= coordsI[1]):
        result = True
    
    # Retorna o indicador de sobreposição
    return result

# Funcionalidade para identificar sobreposição entre duas fotos
# Recebe como parâmetros dois vetores contendo as coordenadas de duas fotos
# Retorna um vetor contendo um indicador de sobreposição e o menor retângulo que contém as fotos
def identifyOverlap(photo1 = [], photo2 = []):
    # Identifica sobreposição entre as fotos nos eixos das abscissas e ordenadas
    value1 = identifyOverlapAxis([photo1[0], photo1[2]], [photo2[0], photo2[2]])
    value2 = identifyOverlapAxis([photo1[1], photo1[3]], [photo2[1], photo2[3]])

    # Condição para que haja sobreposição entre as fotos
    if (value1 and value2):
        # Definindo a coordenada do ponto superior esquerdo do novo retângulo
        firstCoordX = min(photo1[0], photo1[2], photo2[0], photo2[2])
        firstCoordY = max(photo1[1], photo1[3], photo2[1], photo2[3])

        # Definindo a coordenada do ponto inferior direito do novo retângulo
        secondCoordX = max(photo1[0], photo1[2], photo2[0], photo2[2])
        secondCoordY = min(photo1[1], photo1[3], photo2[1], photo2[3])

        # Retorna o indicador de sobreposição e o novo retângulo
        return [True, [firstCoordX, firstCoordY, secondCoordX, secondCoordY]]
    else:
        # Retorna o indicador de sobreposição e um vetor vazio
        return [False, []]
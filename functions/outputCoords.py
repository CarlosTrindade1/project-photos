# Realiza a formatação para a saída dos dados
# Recebe um vetor contendo as coordenadas das fotos
def outputCoords(photos = []):
    for photo in photos:
        # Realiza a formatação
        print('(%i, %i), (%i, %i)' %(photo[0], photo[1], photo[2], photo[3]))
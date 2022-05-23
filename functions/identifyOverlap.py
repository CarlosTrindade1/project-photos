def orderCoords(photo = []):
    if (photo[0] > photo[1]):
        aux = photo[0]
        photo[0] = photo[1]
        photo[1] = aux
    
    return photo

def identifyOverlapAxis(photo1 = [], photo2 = []):
    photo1 = orderCoords(photo1)
    photo2 = orderCoords(photo2)

    gapPhoto1 = abs(photo1[0] - photo1[1])
    gapPhoto2 = abs(photo2[0] - photo2[1])

    coordsI = []
    coordsJ = []
    result = False

    if (gapPhoto1 > gapPhoto2):
        coordsI = photo1
        coordsJ = photo2
    else:
        coordsI = photo2
        coordsJ = photo1
    
    for i in range(coordsI[0], coordsI[1] + 1):
        for j in range(coordsJ[0], coordsJ[1] + 1):
            if (i == j):
                result = True
                break
    
    return result

def identifyOverlap(photo1 = [], photo2 = []):
    value1 = identifyOverlapAxis([photo1[0], photo1[2]], [photo2[0], photo2[2]])
    value2 = identifyOverlapAxis([photo1[1], photo1[3]], [photo2[1], photo2[3]])

    if (value1 and value2):
        firstCoordX = min(photo1[0], photo1[2], photo2[0], photo2[2])
        firstCoordY = max(photo1[1], photo1[3], photo2[1], photo2[3])

        secondCoordX = max(photo1[0], photo1[2], photo2[0], photo2[2])
        secondCoordY = min(photo1[1], photo1[3], photo2[1], photo2[3])

        return [True, [firstCoordX, firstCoordY, secondCoordX, secondCoordY]]
    else:
        return [False, []]
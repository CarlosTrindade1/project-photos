from identifyOverlap import identifyOverlap
from deleteDuplicates import deleteDuplicates

def teste(photos = []):
    overlaps = []
    noOverlaps = []
    overlap = False

    for i in range(len(photos)):
        cont = 0
        for j in range(len(photos)):
            if (i != j):
                result = identifyOverlap(photos[i], photos[j])
                if (result[0]):
                    overlaps.append(result)
                    overlap = True
                else:
                    cont += 1
        if (cont == len(photos) - 1):
            noOverlaps.append(photos[i])

    photos = []
    overlaps = deleteDuplicates(overlaps)

    for i in range(len(overlaps)):
        photos.append(overlaps[i][1])
    
    if (len(noOverlaps) > 0):
        for i in range(len(noOverlaps)):
            photos.append(noOverlaps[i])

    return [overlap, photos]
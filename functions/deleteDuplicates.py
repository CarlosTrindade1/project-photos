def deleteDuplicates(array = []):
    _array = []

    for elemento in array:
        if (elemento not in _array):
            _array.append(elemento)

    return _array
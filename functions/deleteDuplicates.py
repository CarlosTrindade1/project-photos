# Funcionalidade para retirar valores duplicados em um vetor
# Recebe um vetor como parâmetro
def deleteDuplicates(array = []):
    # Define um novo vetor para armazenar os novos valores (sem duplicações)
    _array = []

    # Itera sobre cada elemento do vetor recebido
    for elemento in array:
        # Verifica se o elemento não existe no novo vetor
        # Caso ainda não exista, adiciona o elemento ao novo vetor
        if (elemento not in _array):
            _array.append(elemento)
            
    # Retorna o novo vetor
    return _array
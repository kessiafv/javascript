def mergeSort(arr):
    #se o tamanho da lista for menor ou igual a 1 ela já está ordenada
    if len(arr) <= 1:
        return arr

    #dividir o array ao meio
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    #mergeSort para ordernar as metades
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    #combinar as duas metades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    #combinar os elementos das duas metades até uma delas ficar vazia
    while left_index < len(left) and right_index < len(right):
        if left[left_index] >= right[right_index]: #aqui altera para ordem crescente
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    #adiciona os elementos restantes da metade que não está vazia
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

arr = [54, 26, 93, 17, 77, 31, 44, 55]
print(mergeSort(arr))


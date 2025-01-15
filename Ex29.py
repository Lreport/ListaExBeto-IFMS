def deletduplicates(list_aninhada):
    return [list(set(sublist) for sublist in list_aninhada)]
aninhadaList = [[1, 2, 2], [4, 4, 5], [6, 6, 7]]
print(deletduplicates(aninhadaList))
def sumKeys(dictionary1, dictionary2):
    s = {}
    for key in set(list(dictionary1.keys()) + list(dictionary2.keys())):
        s[key] = dictionary1.get(key, 0) + dictionary2.get(key, 0)
    return s

dictionary1 = {'a':1, 'b':2}
dictionary2 = {'a':3, 'b':4}
dictionary3 = {**dictionary1, **dictionary2}
print(sumKeys(dictionary1, dictionary2))
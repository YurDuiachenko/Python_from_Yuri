def types(*soap):
    a = []
    for i in soap:
        a.append(type(i))
    return a
print(types('1', 2, "234", [34,43], {1, 4}, {'t':'xx'}))
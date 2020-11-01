keys = input().split() 
vals = input().split()
dict = {keys[i]: vals[len(keys) * i :len(keys)*i + len(keys)] for i in range(len(keys))}
print(dict)
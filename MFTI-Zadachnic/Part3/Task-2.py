def write_array(array, file_name):  
    with open(file_name, "w") as file:
        file.write(str(array))
a = ['23', 'trh', 87]
write_array(a, "test.txt")
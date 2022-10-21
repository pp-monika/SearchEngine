import ast
from sortedcontainers import sorteddict

# print(ast.literal_eval("{'test': [[3,1]]}"))
with open("/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/index_subset_Sorted100.txt", "r") as file:
    line = file.readline()
    dictionary1 = line[11:-1]
    d1 = ast.literal_eval(dictionary1)
    # print(dictionary1)

    name = "dictionary10.txt"
    with open(name, 'w') as index_size:
        for key in d1:
            index_size.write(str(key))
            index_size.write(str("\n"))


print("\n")
with open("/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/index_subset_Sorted200.txt", "r") as file:
    line = file.readline()
    dictionary2 = line[11:-1]
    d2 = ast.literal_eval(dictionary2)
    # print(dictionary2)

    name = "dictionary20.txt"
    with open(name, 'w') as index_size:
        for key in d2:
            index_size.write(str(key))
            index_size.write(str("\n"))


import json
import os
import ast
from collections import OrderedDict

def mergeDicts():

    with open("/Users/abhimadduri/Documents/UCI/Fall2021/CS121/Assignment3/combineddictionary54000.txt", "r") as f:
        print("opening 1")
        data1 = f.read()
        # data1 = data1[11:-1]
        # print(data1)
        dict1 = ast.literal_eval(data1)
        print("finish opening 1")
        print("\n")

    with open("/sorted1500/index_size_final1500.txt", "r") as f:
        print("opening 2")
        data2 = f.read()
        # data2 = data2[11:-1]
        # print(data2)
        dict2 = ast.literal_eval(data2)
        print("finish opening 2")

    print("\n")
    # dict1 = OrderedDict(sorted(dict1.items()))
    # dict2 = OrderedDict(sorted(dict2.items()))
    counter = 0
    new_dict = dict1
    for k,v in dict2.items():
        if k in new_dict:
            new_dict[k] = new_dict[k] + v
            counter = counter + 1
            print(counter)
        else:
            new_dict[k] = v
            counter = counter + 1
            print(counter)

    name = "final55393.txt"
    with open(name, 'w') as index_size:
        index_size.write(str(new_dict))
    print(new_dict)
    print(len(new_dict))

if __name__ == "__main__":
    mergeDicts()

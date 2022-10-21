import ast
import os
from io import TextIOWrapper
import time

def mergeIndexes(index1:str,index2:str): #index1and2 are paths to lblindexes
    i1file = open(index1,'r')
    i2file = open(index2,'r')
    temp_merge_file = "/Users/kenny/Documents/cs121/Assignment3/1500Split/lblfolder/merged_index.txt"
    merged_file = open(temp_merge_file, "w")
    
    temp_variable1 = next(i1file, None)
    temp_variable2 = next(i2file, None)
    merged_dict = dict()

    line1 = ast.literal_eval(temp_variable1)
    line2 = ast.literal_eval(temp_variable2)

    print(index2)
    while line1 and line2:
        line1_key = next(iter(line1.keys()))
        line2_key = next(iter(line2.keys()))
        if line1_key == line2_key:
            #print("same keys")
            merged_dict[line1_key] = sorted(line1[line1_key] + line2[line2_key], key=lambda x:x[0])
            merged_file.write(str(merged_dict) + "\n")
            merged_dict = dict()
            temp_variable1 = next(i1file, None)
            temp_variable2 = next(i2file, None)
        elif line1_key < line2_key:
            #print("line1 comes before line2")
            merged_file.write(str(line1)  + "\n")
            temp_variable1 = next(i1file, None)
        elif line1_key > line2_key:
            #print("line2 comes before line1")
            merged_file.write(str(line2)  + "\n")
            temp_variable2 = next(i2file, None)

        if temp_variable1 == None:
            merged_file.close()
            mergeIndexesHelper(temp_merge_file, i2file,temp_variable2)
            i1file.close()
            i2file.close()
            break
        elif temp_variable2 == None:
            merged_file.close()
            mergeIndexesHelper(temp_merge_file, i1file,temp_variable1)
            i1file.close()
            i2file.close()
            break
        
        line1 = ast.literal_eval(temp_variable1)
        line2 = ast.literal_eval(temp_variable2)
    
    os.replace(temp_merge_file, index1)


def mergeIndexesHelper(merged_index:str,unfinished_index:TextIOWrapper,line:str):
    try:
        with open(merged_index, "a") as index:
            while line != None:
                index.write(line)
                line = next(unfinished_index, None)
    except StopIteration:
        pass
    finally:
        unfinished_index.close()



if __name__ =="__main__":
    file_name = "/Users/kenny/Documents/cs121/Assignment3/1500Split/lblfolder/"
    start_time = time.perf_counter()

    counter = 2
    file_1 = file_name + "lblIndex1.txt"
    file_2 = file_name + "lblIndex" + str(counter) + ".txt"
    
    for i in range(35):
        mergeIndexes(file_1, file_2)
        counter += 1
        file_2 = file_name + "lblIndex" + str(counter) + ".txt"
        
        
    end_time = time.perf_counter()
    print(end_time - start_time)


#create temp merge_file
#replace initial file with merge file
#delete temp merge_file

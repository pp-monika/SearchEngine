import ast
import os
def convert_index(file1:str, file2:str):
    """
    TAKE PATH TO INDEX TO CONVERT into file1 
    file2 is new file name
    """
    input_file = open(file1, 'r')
    #print("before ast")
    temp = ast.literal_eval(input_file.read()[11:-1])
    #print("after ast")
    input_file.close()

    
    counter = 1
    new_file = open(file2, 'w')
    for key, value in temp.items():
        #if counter%1000 == 0:
        #    print(counter)
        out_text = "{" + "'" + key + "'" + " : " + str(value) + "}\n"
        new_file.write(out_text)
        counter = counter + 1

    new_file.close()

if __name__ == "__main__":
    pathToIndexes = os.path.abspath("/Users/kenny/Documents/cs121/Assignment3/1500Split") #string
    files = os.listdir(pathToIndexes)
    os.mkdir(pathToIndexes+os.path.sep+"lblfolder")
    counter = 1
    for index in files:
        temp = pathToIndexes + os.path.sep + index
        convert_index(temp, pathToIndexes + os.path.sep + "lblfolder" +os.path.sep + "lblIndex" +str(counter) + ".txt")
        counter+=1
        

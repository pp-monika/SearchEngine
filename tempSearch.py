import re
import ast
from sortedcontainers import SortedDict
from main import tokenize

sorted_dict = dict()

def get_query():
    query = input("what is your query?\n")
    return query


def search_files():
    global sorted_dict
    query = get_query()
    # tokenize the query so that we can use it for the index dict
    tokens = tokenize(query)
    # file location, need to change this
    file = "[file directory]"
    with open(file, 'r') as index:
        # ast.literal_eval turns the string into a dict
        # [11:-1] removes the SortedDict part of the string
        print("before ast")
        temp = ast.literal_eval(index.read())
        print("after ast")
        # go through the query tokens and only keep the dictionary items that match these tokens
        a = temp.keys()
        for token in tokens:
            print(token)
            if token in a:
                sorted_dict[token] = temp[token]


def match_documents():
    global sorted_dict
    # create a sorted list of the keys based on the how many documents are matched with that token
    # i.e. b: [[1,2]] comes before a: [[1,2],[2,3]]
    # this is so that we can more quickly search for the matches
    a = sorted(sorted_dict, key=lambda k: len(sorted_dict[k]))
    matched = None

    i = 1

    # works with AND only rn
    # i.e. only if ALL the query tokens are in a doc it returns that doc

    # if there is only one query token we can just return it since theres nothing we need to match
    if len(a) == 1:
        matched = sorted_dict[a[0]]
    else:
        while i < len(a):
            # if there is only one query token we can just return it since theres nothing we need to match
            if matched != None:
                print("matching")
                # print(matched)
                matched = match_list_dict(matched, sorted_dict[a[i]])
            else:
                print("matching2")
                # print(matched)
                matched = match_list_dict(sorted_dict[a[i - 1]], sorted_dict[a[i]])
            i += 1
    matched.sort(key=lambda matched: matched[1], reverse=True)
    print(matched[0:5])


def match_list_dict(list1, list2):
    matched = []
    i = 0
    j = 0

    while (i < len(list1) and j < len(list2)):
        # print(list1[i][0])
        # print(list2[j][0])
        if list1[i][0] == list2[j][0]:
            total_freq = list1[i][1] + list2[j][1]
            matched.append([list1[i][0], total_freq])
            i += 1
            j += 1
        elif list1[i][0] <= list2[j][0]:
            i += 1
        elif list1[i][0] >= list2[j][0]:
            j += 1

    return matched


if __name__ == "__main__":
    print("searching through file")
    search_files()
    print("searching complete")
    print("matching docs")
    match_documents()
    print("matching complete")

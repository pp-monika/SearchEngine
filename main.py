import os
import json
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from collections import OrderedDict
from sortedcontainers import SortedDict
import re

index = dict()
unique_words = set()
def tokenize(text: str):
    lowerText = text.lower()  # lowercase text
    splitted_newText = re.split("[\s-]+", lowerText)  # split text on whitespace and hyphens

    stemmer = PorterStemmer()
    tokens = []
    for token in splitted_newText:
        newToken = re.sub('[^A-Za-z0-9]+', '', token)  # remove any non alphanumeric characters from token
        if len(newToken) > 0:
            tokens.append(stemmer.stem(newToken))  # stem the token using PorterStemmer and add it to a set
    return tokens


def createList():
    folders_location = os.listdir("[file directory]")

    folders_list = []
    temp = ''
    final = ''
    for folder in folders_location:
        # print(folder)
        temp = os.getcwd() + os.path.sep + "DEV" + os.path.sep + folder
        if os.path.isdir(temp):
            final = temp
            for filename in os.listdir(final):
                # print(filename)
                folders_list.append(final + os.path.sep + filename)


    with open("url.txt", 'w') as url_hashtable:
        counter = 1

        # for location in folders_list[0:950]:
        for location in folders_list:
            words_list = extract_content(location, "content")
            temp_url = extract_content(location, "url")
            print("extracted content")
            url_hashtable.write(str(counter) + " " + temp_url + "\n")
            print(location)
            print(temp_url)
            # print(words_list)
            print(counter)
            create_indexer(words_list, counter)
            counter += 1

            if counter % 18500 == 0:
                name = "index_subset_Sorted_18500_" + str(counter) + ".txt"
                with open(name, 'w') as index_subset:
                    # sorted_index = sorted(index)
                    sorted_index = SortedDict(index)
                    print("writing start")
                    index_subset.write(str(sorted_index))

            
                index.clear()





def create_indexer(list_of_words, url):
    print("indexer start")
    global index
    global unique_words
    for word in list_of_words:
        if word not in index:
            unique_words.add(word)
            index[word] = []
            index[word].append([url, 1])
        else:
            flag = False
            for posting in index[word]:
                if url == posting[0]:
                    index[word][len(index[word]) - 1][1] += 1
                    flag = True
                    break
            if not flag:
                index[word].append([url, 1])

    print("indexer end")


def extract_content(location, type):
    with open(location) as f:
        data = json.load(f)
    HTML_tags = ['h1', 'h2', 'h3', 'title', 'p', 'b', 'strong']
    soup = BeautifulSoup(data['content'], 'lxml')

    temp_words_list = []

    if type == "content":
        for tag in HTML_tags:
            for content in soup.find_all(tag):
                # print(tag)
                # print(content.get_text())
                temp = content.get_text()
                # print(tokenize(temp))
                # print("\n")
                temp_words_list = temp_words_list + tokenize(temp)
    elif type == 'url':
        return data['url']

    return temp_words_list

def test_extract():
    with open("[file directory]") as f:
        data = json.load(f)
        print("1")
    HTML_tags = ['h1', 'h2', 'h3', 'title', 'p', 'b', 'strong']
    soup = BeautifulSoup(data['content'], 'lxml')
    type = "content"
    temp_words_list = []

    if type == "content":
        for tag in HTML_tags:
            for content in soup.find_all(tag):
                print(content.get_text())
                temp = content.get_text()
                temp_words_list = temp_words_list + tokenize(temp)
    elif type == 'url':
        return data['url']

    print(temp_words_list)





if __name__ == "__main__":
    print("test")
    createList()

    name = "index_size_final18500.txt"
    with open(name, 'w') as index_size:
        index_size.write(str(index))

    # print("Number of unique tokens: ", len(index))
    print(len(unique_words))
    

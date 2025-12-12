#counts words of a file}

def number_of_words(book_str):
    list_of_text = book_str.split()
   # print(list_of_text)
    return len(list_of_text)


def number_of_characters(book_str):
    abc = {}
    list_of_text  = book_str.split()
    for word in list_of_text:
        for char in word:
            if char.lower() in abc:
               abc[char.lower()] = (abc[char.lower()]) + 1
            else:
               abc[char.lower()] = 1
    return abc 


def make_list(dict):
    new_list = []
    for item in dict:
        new_list.append({"char": item, "num": dict[item]})
    return new_list



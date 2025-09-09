def get_num_words(strbook):
    word_count = 0

    split_book = strbook.split()
    word_count = len(split_book)

    return word_count

def get_num_char(strbook):
    #Initialize dictionary
    dict_num_char = {}

    #Parse file and update dict
    for c in strbook:
        #Check if string exists in dictionary
        if c.lower() in dict_num_char:
            #if exists, increment by one
            dict_num_char[c.lower()] += 1
        else:
            # if not, create as a new entry
            dict_num_char[c.lower()] = 1

    #return result
    return dict_num_char

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def convert_dict_to_sortedlistdict(dict_letters):
    sortedlist_letters = []
    temp_dict = {'char': 'a', 'num':  0}

    # Create a list of dictionaries
    for c in dict_letters:
        temp_dict = {'char': c, 'num':  dict_letters[c]}
        sortedlist_letters.append(temp_dict)

    # Now sort the list
    sortedlist_letters.sort(reverse=True, key=sort_on)

    return sortedlist_letters


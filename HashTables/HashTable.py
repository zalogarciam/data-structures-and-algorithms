class HashTable():
    pass

def find_first_non_repated_character(string):
    dict = {}
    for i in string:
        if i != ' ':
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
    for i in dict:
        if dict[i] == 1:
            return i
            
print(find_first_non_repated_character('a green apple'))

my_set = set((1, 1, 2 ,3 ,4, 5 , 6))
print(my_set)
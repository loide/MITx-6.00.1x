'''
This function returns the sublist of strings in input list that contains
fewer than 4 caracters.
'''

def lessThan4(a_list):
    lessThan4List = []
    for x in a_list:
        if len(x) < 4:
            lessThan4List.append(x)
    return lessThan4List
    

if __name__ == '__main__':
    a_list = ["apple", "cat", "dog", "banana"]
    print lessThan4(a_list)

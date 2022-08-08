# Exploring the concept of deep copy and shallow copy.
# By creating two dictionaries a list with the dictionaries as element
# and a copy of the list. 

import copy

def checkCopy():

    d1 = {
        1 : "one",
        2 : "two",
        3 : "three"
    }

    d2 = {
        4 : "four",
        5 : "five",
        6 : "six"
    }

    l1 = [d1, d2]

    l2 = copy.deepcopy(l1)  # Deep copy, does not update l2 when d1 updated.
    l2 = l1[:]              # Shallow copy, updates l2 when d1 updated.
 
    d1[1] = "updated"

    print(f'Dictionay {d1} \n list {l2}')

checkCopy()

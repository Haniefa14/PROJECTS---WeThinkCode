def find_min(element):
    """TODO: complete for Step 1"""

    if len(element) == 0:
        return -1
    if len(element) == 1:
        return element[0]

    for i in element:
        if type(i) != int:
            return -1

    else:        
        min_no = find_min(element[1:])
        min1 = element[0]
        if min_no < min1:
            min1 = min_no
    return min1
def sum_all(element):
    """TODO: complete for Step 2"""    

    for a in element:
        if type(a) != int:
            return -1
    if len(element) == 0:
        return -1
    if len(element) == 1:
        return element[0]
    
    else:        
        add_up = element[1:]
        sum1 = element[0]
        return sum1 + sum_all(add_up)

def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""

    if len(character_set) == 0:     
            return []
    if n < 0:
            return []
    if n == 0:
            return [""]

    for a in character_set:
        if type(a) != str: #check individually
            return []
        
        

        set1 = []
        for a in character_set:
            for j in find_possible_strings(character_set, n-1):
                set1.append(a + j)
        return set1
    
my_list = [3,6,8,9,3,11]
print(sum_all(my_list))
print(find_min(my_list))

character_set = []
print(find_possible_strings(character_set, 3))

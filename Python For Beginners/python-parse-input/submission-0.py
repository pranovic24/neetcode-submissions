from typing import List

def read_integers() -> List[int]:
    line = input()
    string_list = line.split(",")
    nums_list = []

    for s in string_list:
        nums_list.append(int(s))
    
    return nums_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

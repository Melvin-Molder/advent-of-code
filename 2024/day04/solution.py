def get_list(file):
    lst = []
    for line in file:
        lst.append(list(line.strip()))
    return lst

with open("input.txt", "r") as file_in:
    lsts = get_list(file_in)

count1 = 0
count2 = 0

for i in range(len(lsts)):
    
    lst1 = lsts[i]
    
    if i+3 < len(lsts):
        lst2 = lsts[i+1]
        lst3 = lsts[i+2]
        lst4 = lsts[i+3]    
    elif i+2 < len(lsts):
        lst2 = lsts[i+1]
        lst3 = lsts[i+2]
        lst4 = []
    else:
        lst2 = []
        lst3 = []
        lst4 = []
    
    for j in range(len(lst1)):
        if 'XMAS' in ''.join(lst1[j:j+4]) or 'SAMX' in ''.join(lst1[j:j+4]):
            count1 += 1
        if len(lst2) > 0 and len(lst3) > 0 and len(lst4) > 0:
            if lst1[j] == 'X' and lst2[j] == 'M' and lst3[j] == 'A' and lst4[j] == 'S':
                    count1 += 1
            if lst1[j] == 'S' and lst2[j] == 'A' and lst3[j] == 'M' and lst4[j] == 'X':
                    count1 += 1
            if j+3 < len(lst4):
                if lst1[j] == 'X' and lst2[j+1] == 'M' and lst3[j+2] == 'A' and lst4[j+3] == 'S':
                        count1 += 1
                if lst1[j] == 'S' and lst2[j+1] == 'A' and lst3[j+2] == 'M' and lst4[j+3] == 'X':
                        count1 += 1
                if j-3 >= 0:
                    if lst1[j] == 'S' and lst2[j-1] == 'A' and lst3[j-2] == 'M' and lst4[j-3] == 'X':
                            count1 += 1
                    if lst1[j] == 'X' and lst2[j-1] == 'M' and lst3[j-2] == 'A' and lst4[j-3] == 'S':
                            count1 += 1
        if len(lst2) > 0 and len(lst3) > 0:
            if j+2 < len(lst1):         
                if lst1[j] == 'M' and lst2[j+1] == 'A' and lst3[j+2] == 'S':
                    if lst1[j+2] == 'M':
                        if lst3[j] == 'S':
                            count2 += 1
                    if lst1[j+2] == 'S':
                        if lst3[j] == 'M':
                            count2 += 1
                if lst1[j] == 'S' and lst2[j+1] == 'A' and lst3[j+2] == 'M':
                    if lst1[j+2] == 'S':
                        if lst3[j] == 'M':
                            count2 += 1
                    if lst1[j+2] == 'M':
                        if lst3[j] == 'S':
                            count2 += 1

print(f"Part 1: {count1}")
print(f"Part 2: {count2}")
def check_order(lst):
    if all(lst[i] < lst[i+1] for i in range(len(lst) - 1)):
        return "Increasing"
    elif all(lst[i] > lst[i+1] for i in range(len(lst) - 1)):
        return "Decreasing"
    else:
        return "Unordered"

def is_safe(lst):
    if all(1 <= abs(lst[i] - lst[i+1]) <= 3 for i in range(len(lst) - 1)):
        return True
    return False

def get_list(file):
    lst = []
    for line in file:
        lst.append(list(map(int, line.split())))
    return lst

with open("input.txt", "r") as file_in:
    lsts = get_list(file_in)

safe_count = 0

for lst in lsts:
    if check_order(lst) != "Unordered" and is_safe(lst):
        safe_count += 1

# Part 1
print(safe_count)
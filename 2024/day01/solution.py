def get_lists(file):
    # Returns the list input as 2 lists sorted in ascending order
    l1 = []
    l2 = []
    for line in file:
        l1.append(int(line.split()[0]))
        l2.append(int(line.split()[1]))
    
    l1.sort() 
    l2.sort()
    return l1, l2
    
def get_dist(l1, l2):
    # Returns the total differance between the 2 lists entrys
    dist = 0
    for i in range(len(l1)):
        dist += abs(l1[i] - l2[i])
    return dist

def get_freq(list):
    # Returns a dictionary of the frequency of the list
    freq_dict = {}
    for i in range(len(list)):
        id = list[i]
        if id not in freq_dict:
            freq_dict[id] = 1
        else:
            freq_dict[id] += 1
    return freq_dict

def get_sim(list, dict):
    # Returns the total number of times id from list appears in dictionary as a similarity score
    sim = 0
    for i in range(len(list)):
        id = list[i]
        if id in dict:
            sim += id * dict[id]
    return sim

try:
    with open("input.txt", "r") as file_in:
        list1, list2 = get_lists(file_in)

    freq_dict = get_freq(list2)

    # Part 1
    print(get_dist(list1, list2))

    # Part 2
    print(get_sim(list1, freq_dict))
    
except Exception as e:
    print(f"An error occured: {e}")
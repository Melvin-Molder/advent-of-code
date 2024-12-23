def multiply(a, b):
    return a * b

with open("input.txt", "r") as file_in:
    chars = file_in.read()

p1_total = 0
p2_total = 0
mul = True

for i in range(len(chars)):
    do_str = chars[i:i+4]
    dont_str = chars[i:i+7]
    mul_str = chars[i:i+4]

    if do_str == "do()":
        mul = True
    elif dont_str == "don't()":
        mul = False
    elif mul_str == "mul(":
        tst_str = chars[i:i+12]
        end_index = tst_str.find(")")
        if end_index != -1:
            nums = tst_str[4:end_index].split(",")
            try:
                sum = multiply(int(nums[0]), int(nums[1]))
                p1_total += sum
                if mul:
                    p2_total += sum
            except:
                pass

print(f"Part 1: {p1_total}")
print(f"Part 2: {p2_total}")
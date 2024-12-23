def multiply(a, b):
    return a * b

with open("input.txt", "r") as file_in:
    chars = file_in.read()

total = 0
mul = True

for i in range(len(chars)):
    do_str = chars[i:i+4]
    dont_str = chars[i:i+7]
    if do_str == "do()":
        mul = True
        print("do()")
    if dont_str == "don't()":
        mul = False
        print("don't()")
    mul_str = chars[i:i+4]
    if mul_str == "mul(" and mul == True:
        tst_str = chars[i:i+12]
        end_index = tst_str.find(")")
        if end_index != -1:
            # print(tst_str)
            nums = tst_str[4:end_index].split(",")
            try:
                # print(multiply(int(nums[0]), int(nums[1])))
                total += multiply(int(nums[0]), int(nums[1]))
            except Exception as e:
                print(f"An error occured: {e}")

print(total)
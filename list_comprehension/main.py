with open("file1.txt") as f:
    f1 = f.readlines()

with open("file2.txt") as f:
    f2 = f.readlines()

result = [int(n) for n in f1 if n in f2]
print(result)


# f1_list = [n.strip() for n in f1]
# f2_list = [n.strip() for n in f2]
#                                                               easier method exists
# # print(f1_list)
# # print(f2_list)
#
# result = [n for n in f1_list if n in f2_list]
# print(result)



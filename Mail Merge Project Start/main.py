#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# method - 1:
# with open("./Input/Letters/starting_letter.txt") as f:
#     template = f.read()
#
# with open("./Input/Names/invited_names.txt") as f:
#     names = f.readlines()
#
# name_list = []
# for items in names:
#     t = str.split(items)
#     if len(t) == 1:
#         name_list.append(t[0])
#     else:
#         n = ""
#         for parts in t:
#             n = n  + parts + " "
#         name_list.append(n[0:-1])
#
# for name in name_list:
#     with open(f"./Output/ReadyToSend/{name}.txt","w") as f:
#         letter = template.replace("[name]",f"{name}")
#         f.write(letter)
#
# print(name_list)


with open("./Input/Names/invited_names.txt","r") as f:
    names = f.readlines()

with open("./Input/Letters/starting_letter.txt") as f:
    template = f.read()

for name in names:
    t = name.strip()
    with open(f"./Output/ReadyToSend/{t}.txt", "w") as f:
        letter = template.replace("[name]",f"{t}")
        f.write(letter)

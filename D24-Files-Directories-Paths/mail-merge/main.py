#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open("./Input/Names/invited_names.txt") as invite_list:
    invitees = invite_list.readlines()
    for invitee in invitees:
        names.append(invitee.rstrip())



# with open("./Input/Letters/starting_letter.txt") as draft_letter:
#     starting_letter = draft_letter.readlines()

# placeholder = "Dear [name],\n"
#
# for name in names:
#     if placeholder in starting_letter:
#         placeholder_index = starting_letter.index(placeholder)
#         custom_letter = starting_letter.copy()
#         custom_letter[placeholder_index] = f"Dear {name},\n"
#         with open(f"./Output/ReadyToSend/{name}.txt", 'w') as out_letter:
#             for custom_chunk in custom_letter:
#                 out_letter.write(custom_chunk)

with open("./Input/Letters/starting_letter.txt") as draft_letter:
    starting_letter = draft_letter.read()

placeholder = "[name]"

for name in names:
    if placeholder in starting_letter:
        custom_letter = starting_letter.replace(placeholder, name)
        with open(f"./Output/ReadyToSend/{name}.txt", 'w') as out_letter:
            out_letter.write(custom_letter)

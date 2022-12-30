from functions.occurences import occurence
user_input = input("What is your sequence")
user_substring = input("What is your substring?")
for x in range(len(occurence(user_input, user_substring))):
    print (occurence(user_input, user_substring)[x])
#print (occurence(user_input, user_substring))

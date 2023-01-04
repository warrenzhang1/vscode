from functions.frequent_words import frequent
user_text = input('What is your text?')
user_k = int(input('How many k-mers?'))
user_dict = frequent(user_text, user_k)
print(user_dict)

sorted_user_dict = dict(sorted(user_dict.items(), key = lambda x:x[1], reverse = True ))
maximum_value  = (list(sorted_user_dict.values())[0])

for key, value in sorted_user_dict.items() :
    
    if maximum_value == value :
        print (key + " " + str(value))

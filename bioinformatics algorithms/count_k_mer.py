from functions.frequent_words import frequent
user_text = input('What is your text?')
user_k = int(input('How many k-mers?'))
user_dict = frequent(user_text, user_k)
print(user_dict)
for key, value in user_dict.items() :
    count = 0 
    if value > count :
        print (key + " " + str(value))

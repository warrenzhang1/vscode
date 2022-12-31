i = 0
count = 0
word_count = {}

list = input().split()

for i in range (len(list)): 
    for item in list :
        if list[i] == item :
            count += 1 
    word_count[list[i]] = count
    count = 0

print (word_count)
for (key, value) in word_count.items():
    print (str(key) + (' ') +  str(value))
    
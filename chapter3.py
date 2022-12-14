guest_list = ['mom','dani','me']
for item in guest_list :
    print('Will you come to dinner with me ' + item)

guest_list.pop(1)
guest_list.insert(1,'gary')
print('Will you come to dinner with me ' + guest_list[1])
months = int(input('How many months'))
k = int(input(['Litter size?']))
#n = i 
#fn = fn-1 + fn-2
#F1 = F2 = 1
#F1 = 1
#F2 = 1
#F3 = F1 + F2 
#F4 = f2 + F3
n_month = 0
number_of_pairs = 0
for x in range (0,months) :
    first_month = 1 #pair
    number_of_pairs = first_month
    second_month = first_month + number_of_pairs #pair
    third_month = second_month + second_month*k
    n_month = first_month + third_month + n_month #number of pairs
    #variable_month = first_month + second_month
print(n_month)
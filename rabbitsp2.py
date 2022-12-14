months = int(input('How many months'))

k = int(input('Litter size?'))

#1, 1, 4, 7, 
#function_n = function_n_minus_1 + function_n_minus_2
#current_month_count = last_month + two_months_ago
#month 1 = 1
#month 2 = 1
#month 3 = 1 + month(2)*3 = 4
#month 4 = month 3 + month(2)*3 = 7
#month 5 = month 4 + month (3) *3 = 7 +12
month_last = 1 
month_last_last = 1
for x in range (1,months-1) :
    month_n = month_last + (month_last_last * k)
    month_last_last = month_last
    month_last = month_n
    
print(month_n)
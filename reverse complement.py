dna_sequence = []
user_input = input()
reverse_sequence = []
dna_sequence = list(user_input.upper())
reverse_sequence = dna_sequence
print(reverse_sequence)
length_list = len(reverse_sequence)
for i in range(length_list) :
    if reverse_sequence[i] == "T" :
        del reverse_sequence[i]
        reverse_sequence.insert(i  , "A")
        continue
    elif reverse_sequence[i] == "A" : 
        del reverse_sequence[i]
        reverse_sequence.insert(i , "T")
        continue
    elif reverse_sequence[i] == "C" : 
        del reverse_sequence[i]
        reverse_sequence.insert(i , "G")
        continue
    elif reverse_sequence[i] == "G" : 
        del reverse_sequence[i]
        reverse_sequence.insert(i , "C")
        continue

    
   
reverse_sequence.reverse()
print(''.join(reverse_sequence))
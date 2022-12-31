dna_sequence = []
user_input = input()

dna_sequence = list(user_input.upper())

for item in dna_sequence :
    if item == "T" :
        item_location = dna_sequence.index(item)
        dna_sequence.remove(item)
        dna_sequence.insert(item_location , "U")

print (''.join(dna_sequence))
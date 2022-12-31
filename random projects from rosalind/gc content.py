
#dna_dictionary = {}
#dna_sequence_name = ''
#while dna_sequence_name != 'quit' :
#    dna_sequence_name = input("What is your sequence name")
#    dna_sequence = list(input("What is your sequence?"))
#    dna_dictionary[dna_sequence_name] = dna_sequence
#    dna_sequence_name = input("Do you have another sequence name? Or enter quit to stop the program")

#print(dna_dictionary)
#Dna dictionary function
from functions.dna_dictionary import dna_repository 
dna_sequence = []
dna_sequence_name = ''
dna_dictionary = dna_repository( dna_sequence_name, dna_sequence)
dna_gc_count = {}

print(dna_dictionary)
for key, value in dna_dictionary.items() :
    count = 0
    gc_count_name = str(key)
    print (gc_count_name)
   # sequence_name = dna_dictionary
    for item in value :
            if item == 'C' :
                count += 1
           
            if item == 'G' :
                count += 1
                
    dna_gc_count[gc_count_name] = (count/len(value))
    print(count)
print(dna_gc_count)
for key, value in dna_gc_count.items() :
    highest_average = 0
    key_name = str(key)
    if highest_average <= dna_gc_count[key] :
        highest_average = dna_gc_count[key]
        key_name = key
highest_average_percent = (highest_average * 100)
print (key +": " +str(highest_average_percent))
def dna_repository(dna_sequence_name,dna_sequence) :
    dna_dictionary = {}
    dna_sequence_name = ''
    active = True
    while active:
        dna_sequence_name = input("What is your sequence name")
        dna_sequence = list(input("What is your sequence?"))
        dna_dictionary[dna_sequence_name] = dna_sequence
        repeat = input("Do you have another sequence? (yes/no)")
        if repeat == 'no' :
            active = False

    return dna_dictionary


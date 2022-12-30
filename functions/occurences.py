def occurence(string, substring) :
    pattern_occurence = [] 
    for i in range (len(string)-len(substring)+1) :
        if string[i:i+len(substring)] == substring :
            pattern_occurence.append(i)
    return pattern_occurence
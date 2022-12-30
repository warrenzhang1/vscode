def frequent(text, k) :
    frequent_patterns = {}
    for i in range (len(text)-k) :
        pattern =  text[i:k]   
        count = 0
        if pattern in frequent_patterns :
            frequent_patterns[pattern] += 1
        else :
            frequent_patterns[pattern] = count
        k= k+1
    return frequent_patterns